import random

from Databases.Models import Trigger, Answer, TriggerAnswer, Permission
from Permissions import PermissionChecker
from utils.WorkWithUtils.WorkWithAuth import AuthTools
from utils.WorkWithUtils.WorkWithUpload import PhotoUpload
from .MainWorkWith import BaseWorkWith
from utils.RegexUtils import compare_add_text, compare_ban, compare_ban_command, \
    compare_unban_command, compare_unban, compare_remove_text, compare_add_simple


class DataBaseTrigger(BaseWorkWith):
    """
    Все что вы хотели узнать о работе с базой данных но боялись спросить
    Класс с реализацией функций, адрессующихся к БД
    """

    def __init__(self, obj, vk):
        super().__init__(obj, vk)
        self.permission = PermissionChecker(obj, vk)

    def _params_list_to_dict(self, params_list) -> dict:
        """
        Превращает список параметров в словарь для последующего добавления в БД
        :param params_list: список параметров из сообщения.
        params_list[0] - триггер для сообщения
        params_list[1] - текстовый ответ на сообщение
        :return: return_dict (снизу) с обработнными параметрами или вызывает IndexError, ValueError
        """
        # Словарь с дефолтными значениями настроек для сообщения
        return_dict = {
            "trigger": params_list[0],
            "answer_txt": params_list[1],
            "set_chance": 0,
            "strict": 0,
            "set_global": self.obj.peer_id
        }
        # Проверка, есть ли доп. настройки для триггера. Если нет, то возвращаем словарь
        try:
            list_of_sub_params = params_list[2].split(" ")
        except IndexError:
            return return_dict
        # Если настройки есть, то собираем их всех
        for param in list_of_sub_params:
            # Формат настройки: наименование_условия=значение
            key_value_split = param.split("=")
            if key_value_split[0] in ["set_chance", "strict"]:
                if key_value_split[0] == "strict" and int(key_value_split[1]) not in [0, 1]:
                    raise IndexError
                return_dict[key_value_split[0]] = int(key_value_split[1])
            elif key_value_split[0] == "set_global":
                if self.permission.is_user_admin():
                    return_dict[key_value_split[0]] = None
                else:
                    raise ValueError
            else:
                return_dict[key_value_split[0]] = key_value_split[1]
        return return_dict

    def _find_trigger(self, dict_of_parameters: dict) -> Trigger:
        """
        Функиця для поиска нужного триггера, если не находим то создаем новый
        :param dict_of_parameters: словарь, генерируемый _params_list_to_dict()
        :return: Объект таблицы Trigger
        """
        find_trigger = Trigger.get_or_none(Trigger.trigger_text == dict_of_parameters["trigger"],
                                           Trigger.conference_id == dict_of_parameters["set_global"],
                                           Trigger.trigger_type == dict_of_parameters["strict"],
                                           Trigger.trigger_chance == dict_of_parameters["set_chance"]
                                           )
        if not find_trigger:
            find_trigger = Trigger.create(trigger_text=dict_of_parameters["trigger"],
                                          trigger_chance=dict_of_parameters["set_chance"],
                                          trigger_type=dict_of_parameters["strict"],
                                          conference_id=dict_of_parameters["set_global"])
        return find_trigger

    def add_to_db(self) -> str:
        """
        Внутренняя кухня функции !добавить
        :return: Сообщение о добавлении/ошибке добавления
        """
        msg_text = str(self.obj.text)
        # Подходит ли наше сообшение критерию добавления
        if compare_add_simple(self.obj.text):
            attach_object = None  # Возможно будущий словарь с аттачментом, а возможно нет

            if len(self.obj.attachments) == 1:  # Пока такая проверка, в будущем можно будет делать разные аттачи
                attach_object = self.obj.attachments[0]
                # Пока работаем только с фото
                if attach_object["type"] != "photo":
                    return "Пока такого функционала нету"

            # Обрезаем !добавить от всего сообщения
            trigger_base = msg_text[10:]
            # получем список с триггером, ответом и параметрами
            trigger_split = trigger_base.split("|")

            # Если есть что-то помимо текста триггера
            if len(trigger_split) != 1:
                try:
                    # Пропускаем сообщение через генерацию словаря с параметрами
                    dict_of_parameters = self._params_list_to_dict(trigger_split)
                    # Одинарные скобочки означают пропуск текста, в случае добавления параметров
                    if trigger_split[1] == "''":
                        dict_of_parameters["answer_txt"] = ""
                # Если генерация словаря вернула ошибки
                except ValueError:
                    return "Ну ты и свинья, конечно"
                except IndexError:
                    return "Кажется кто-то хочет нагадить мне в душу."
            elif attach_object:
                # Если у нас нет ничего кроме триггера и аттачмента
                dict_of_parameters = {
                    "trigger": trigger_base,
                    "answer_txt": "",
                    "set_chance": 0,
                    "strict": 0,
                    "set_global": self.obj.peer_id
                }
            else:
                # Не доводи меня, пучеглазый
                return "Не доводи меня, пучеглазый"
            # Ищем, существует ли такой триггер с такими настройками, есси нет - создаем
            find_trigger = self._find_trigger(dict_of_parameters)
            # Если у нас есть объекты аттачмента
            if attach_object:
                attach_url = attach_object["photo"]["sizes"][-1]["url"]
                attach = PhotoUpload.load_img(AuthTools.authByGroup()[2], attach_url)
                dict_of_parameters["images"] = attach
                answer = Answer.create(answer_text=dict_of_parameters["answer_txt"], answer_picture=attach)
            else:
                answer = Answer.create(answer_text=dict_of_parameters["answer_txt"])
            TriggerAnswer.create(trigger_link=find_trigger.trigger_id, answer_link=answer.answer_id)
            return f"Условие {dict_of_parameters['trigger']} успешно добавлено!"
        else:
            return "Ты хрюня)"

    def remove_from_db(self):
        msg_text = str(self.obj.text)
        if compare_remove_text(msg_text):
            try:
                msg_splitted = msg_text[8:].split("|")
                base_list = [msg_splitted[0], "самый идиотский котсыль в мире"]
                base_list.extend(msg_splitted[1:])
                dict_of_parameters = self._params_list_to_dict(base_list)
                # print(dict_of_parameters)
            except ValueError:
                return "Вы дегенерат"
            except IndexError:
                return "Всем хрю, с вами мегахрю (что-то было сделано НЕ ТАК)"
            # result = ResultOfTrigger.objects.create(type_media=1, result_of_trigger=list_of_parameters[1])
            find_trigger = Trigger.get_or_none(Trigger.trigger_text == dict_of_parameters["trigger"],
                                               Trigger.conference_id == dict_of_parameters["set_global"],
                                               Trigger.trigger_type == dict_of_parameters["strict"],
                                               Trigger.trigger_chance == dict_of_parameters["set_chance"])
            if not find_trigger:
                return "Ну и рыготина, пиши нормально"
            trigger_to_answers = TriggerAnswer.select().where(TriggerAnswer.trigger_link == find_trigger.trigger_id)

            for i_hate_fucking_peewee in trigger_to_answers:
                # print(i_hate_fucking_peewee.answer_link, Answer.answer_id)
                Answer.delete().where(Answer.answer_id == i_hate_fucking_peewee.answer_link).execute()
            find_trigger.delete_instance()
            return f"Условие {dict_of_parameters['trigger']} успешно удалено!"
        else:
            return "Вы сделали какую-то тупую хуйню и все сломалось"

    def get_list_of_triggers(self) -> str:
        """
        Получаем список триггеров конфереции или во всем боте
        :return: Сообщение со всеми триггерами
        """
        list_of_params = self.obj.text.split(" ")
        if len(list_of_params) in [1, 2] and list_of_params[0] == "!триггеры":
            if len(list_of_params) == 1:
                trigger_filter = int(self.obj.peer_id)
            elif list_of_params[1] in ["конфы", "конференции"]:
                trigger_filter = int(self.obj.peer_id)
            elif list_of_params[1] in ["глобальные", "общие"]:
                trigger_filter = None
            else:
                return "Вообще не то написал, чел. Полная хуйня"
            trigger_set = Trigger.filter(conference_id=trigger_filter).execute()
            if not trigger_set:
                return "а тутачки ничего нет)))"
            response_text = ""
            for trigger in trigger_set:
                response_text += f"Триггер: {trigger.trigger_text} | set_chance={trigger.trigger_chance} " \
                                 f"strict={trigger.trigger_type}\n"
            return response_text
        else:
            raise KeyError

    def get_trigger(self) -> (int, int, str):

        trigger_set_in_conference = Trigger.filter(conference_id=int(self.obj.peer_id)).execute()
        trigger_set_global = Trigger.filter(conference_id=None).execute()
        for trigger in trigger_set_in_conference:
            if (trigger.trigger_type == 0 and trigger.trigger_text == self.obj.text) or \
                    (trigger.trigger_type == 1 and self.obj.text.lower().find(trigger.trigger_text) != -1):
                return trigger.trigger_id, trigger.trigger_chance, trigger.trigger_text
        for trigger in trigger_set_global:
            if (trigger.trigger_type == 0 and trigger.trigger_text == self.obj.text) or \
                    (trigger.trigger_type == 1 and self.obj.text.lower().find(trigger.trigger_text) != -1):
                return trigger.trigger_id, trigger.trigger_chance, trigger.trigger_text
        return None, None, None

    @staticmethod
    def get_answer_from_db(id_trigger):
        trigger_obj = Trigger.get_by_id(id_trigger)
        answers_set = Answer.select().join(TriggerAnswer).where(TriggerAnswer.trigger_link == trigger_obj.trigger_id)
        answers_return_list = []
        for answer in answers_set:
            answers_return_list.append(

                {
                    "text": answer.answer_text,
                    "picture": answer.answer_picture,
                    "doc": answer.answer_doc,
                    "answer_video": answer.answer_video,
                    "answer_music": answer.answer_music
                }
            )
        return random.choice(answers_return_list)


class PermissionsWorker(BaseWorkWith):
    def __init__(self, obj, vk):
        super().__init__(obj, vk)
        self.permission = PermissionChecker(obj, vk)

    def _params_str_to_dict(self, params_str) -> dict:
        string_to_work = params_str[:params_str.find(" ")]
        params_str = params_str[params_str.find(" ") + 1:]
        user_id = None
        conference_id = self.obj.peer_id
        command_to_ban = None
        if string_to_work in ["!бан", "!разбан"]:
            if params_str.count("|") > 1:
                if not self.permission.is_user_admin():
                    raise ValueError
                conference_id = None

            user_id = params_str[1:params_str.find("|")]
            user_id = int(user_id[2:]) if user_id.find("id") + 1 else -int(user_id[6:])
        elif string_to_work in ["!бан_ком", "!разбан_ком"]:
            command_to_ban = params_str
            if params_str.count("|") > 0:
                if not self.permission.is_user_admin():
                    raise ValueError
                conference_id = None
                command_to_ban = command_to_ban[:params_str.find("|")]
        return \
            {
                "user_id": user_id,
                "conference_id": conference_id,
                "command_to_ban": command_to_ban
            }

    def ban(self):
        msg_text = str(self.obj.text)
        if (compare_ban(msg_text) or compare_ban_command(msg_text)) and (
                self.permission.is_user_admin() or self.permission.is_user_admin_in_conference()):
            try:
                dict_of_parameters = self._params_str_to_dict(msg_text)
            except ValueError:
                return "Ну и че ты натворил? Иди чини эту хуйню теперь"

            Permission.create(user_vk_id=dict_of_parameters["user_id"],
                              conference_id=dict_of_parameters["conference_id"],
                              command_name=dict_of_parameters["command_to_ban"])
            return "Бан!"
        else:
            return "Nigger"

    def unban(self):
        msg_text = str(self.obj.text)
        if (compare_unban(msg_text) or compare_unban_command(msg_text)) and (
                self.permission.is_user_admin() or self.permission.is_user_admin_in_conference()):
            try:
                dict_of_parameters = self._params_str_to_dict(msg_text)
            except ValueError:
                return "Объясни мне вот ЧТО ты делаешь?????????????"

            if Permission.delete().where(Permission.user_vk_id == dict_of_parameters["user_id"],
                                         Permission.conference_id == dict_of_parameters["conference_id"],
                                         Permission.command_name == dict_of_parameters["command_to_ban"]).execute():
                return "Разбан!"
            else:
                return "Такого не существует, вы ГЛУПЫЙ ЧЕЛОВЕК"
        else:
            return "Скорее всего вы не являетесь модератором или что-то пошло не так"
