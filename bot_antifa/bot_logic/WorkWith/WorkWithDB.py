from bot_logic.Databases.Models import Trigger, Answer, TriggerAnswer
from bot_logic.consts.login_consts import admin_id
from bot_logic.utils.RegexUtils import compare_add_text, compare_add_media


class DataBaseTrigger:
    def __init__(self, obj, vk):
        self.obj = obj
        self.vk = vk

    def _params_list_to_dict(self, params_list) -> dict:
        try:
            strict_data = params_list[2]
        except IndexError:
            strict_data = 0
        try:
            set_chance = params_list[3]
        except IndexError:
            set_chance = 1
        try:
            if int(self.obj.from_id) == int(admin_id):
                set_global = None
            else:
                set_global = self.obj.peer_id
        except IndexError:
            set_global = self.obj.peer_id
        if int(strict_data) in [0, 1] and int(set_chance) > 0:
            strict_data = int(strict_data)
            set_chance = int(set_chance)
        else:
            raise ValueError

        return {
            "trigger": params_list[0],
            "answer_txt": params_list[1],
            "strict": strict_data,
            "set_chance": set_chance,
            "set_global": set_global,
        }

    def add_to_db(self):
        msg_text = str(self.obj.text)
        if compare_add_text(msg_text):
            try:
                dict_of_parameters = self._params_list_to_dict(msg_text[9:].split("|"))
            except ValueError:
                return "Неверно задан формат добавления"
            # result = ResultOfTrigger.objects.create(type_media=1, result_of_trigger=list_of_parameters[1])
            find_trigger = Trigger.get_or_none(Trigger.trigger_text == dict_of_parameters["trigger"])
            if not find_trigger:
                find_trigger = Trigger.create(trigger_text=dict_of_parameters["trigger"],
                                              trigger_chance=dict_of_parameters["set_chance"],
                                              trigger_type=dict_of_parameters["strict"],
                                              conference_id=dict_of_parameters["set_global"])

            answer = Answer.create(answer_text=dict_of_parameters["answer_txt"])
            TriggerAnswer.create(trigger_link=find_trigger.trigger_id, answer_link=answer.answer_id)
            return f"Условие {dict_of_parameters['trigger']} успешно добавлено!"
        elif compare_add_media(self.obj.text):
            pass
        else:
            return "Неверно задан формат добавления"

