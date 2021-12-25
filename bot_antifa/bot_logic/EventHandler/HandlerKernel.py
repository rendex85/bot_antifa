import random
from abc import ABCMeta, abstractmethod
from typing import List

from Permissions import PermissionChecker
from WorkWith.MainWorkWith import CompareWorkWithAll, BaseWorkWith
from utils.DataClassUtils import Message


class BaseHandler(metaclass=ABCMeta):
    """
    Обработчик комманд для бота.
    Предназачен для наследования и реализации различного функционала для респоносов робота
    """
    do_threading = False  # пока ни за что не отвечает, когда-нибудь придумаю что с этим можно придумать

    trigger_in: List[str] = []  # Если есть вхождение строки из списка, запускает обработку команды
    trigger_strict: List[str] = []  # Если есть строка из списка соотвествует тексту, запускает обработку команды
    trigger_not_strict: List[str] = []  # Пропускает обработку если строка из списка соотвествует сообщению
    trigger_not_in: List[str] = []  # Пропускает обработку если есть вхождение строки из списка
    random_right: int = 0  # Задает значение, с каким шансом будет реагировать на сообщение (0 - 100%)
    separate_random_triggers: bool = False  # Нужно ли разделять срабатывание рандома и срабатывание на триггеры

    def __init__(self, vk, obj, dict_of_globals):
        self.vk = vk
        self.obj = obj
        self.message_data = Message()  # Все что можно передать в метод vk.messages.send()
        self.do_post: bool = True  # Если нужно пропустить вызов метода self.post
        self.command = None  # Стриггереная команда
        self.permissions = PermissionChecker(self.obj, self.vk)  # Права доступа
        self.dict_of_globals = dict_of_globals  # Оперативная память бота
        self.working_methods = CompareWorkWithAll(self.obj, self.vk,
                                                  self.dict_of_globals)  # Объединяем все классы из WorkWith
        self._initiator()  # Вызов функции првоерки условий

    def _initiate_post_message(self) -> None:
        self.preHandler()
        self.post()

    def _initiator(self) -> None:
        """
        Проверка возможности ответа на сообщение
        """

        # Если текст не соответсвует trigger_not, заканчиваем обработку
        for el in self.trigger_not_in:
            if self.obj.text.lower().find(el) != -1:
                return
        for el in self.trigger_not_strict:
            if self.obj.text.lower() == el:
                return

        # Если есть разделение рандома и триггеров
        if self.random_right > 0:
            if random.randint(0, self.random_right) == 0:
                if self.separate_random_triggers:
                    self._initiate_post_message()
            elif not self.separate_random_triggers:
                return

        # Проверяем наличие вхождения сообщения текста в триггер, запоминаем комманды
        for el in self.trigger_in:
            if self.obj.text.lower().find(el) != -1:
                self.command = el
                self._initiate_post_message()
                return
        for el in self.trigger_strict:
            if self.obj.text.lower() == el:
                self.command = el
                self._initiate_post_message()
                return

    @abstractmethod
    def preHandler(self) -> None:
        """
        Функция для генерации ответа бота
        """
        pass

    def post(self) -> None:
        """
        Отправка сообщения в диалог
        """
        if not (self.permissions.is_user_banned() or self.permissions.is_command_banned(self.command)) and self.do_post:
            self.vk.messages.send(peer_id=self.obj.peer_id, random_id=0, message=self.message_data.message,
                                  attachment=self.message_data.attachment, reply_to=self.message_data.reply,
                                  forward_messages=self.message_data.forward_mes, forward=self.message_data.forward,
                                  sticker_id=self.message_data.sticker, keyboard=self.message_data.keyboard,
                                  dont_parse_links=self.message_data.dont_parse_links,
                                  disable_mentions=self.message_data.disable_mentions)
