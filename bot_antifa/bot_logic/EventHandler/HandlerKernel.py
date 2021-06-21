import random
from typing import List

from bot_logic.WorkWith.MainWorkWith import CompareWorkWithAll
from bot_logic.utils.DataClassUtils import Message


class BaseHandler:
    trigger_in: List[str] = []
    trigger_strict: List[str] = []
    trigger_not_strict: List[str] = []
    trigger_not_in: List[str] = []
    random_right: int = 0
    separate_random_triggers: bool = False  # бля че это)))

    def __init__(self, vk, obj):
        self.vk = vk
        self.obj = obj
        self.message_data = Message()
        self.working_methods = CompareWorkWithAll(self.obj, self.vk)
        self.initiator()

    def initiator(self):
        for el in self.trigger_not_in:
            if self.obj.text.lower().find(el) != -1:
                return True
        for el in self.trigger_not_strict:
            if self.obj.text.lower() == el:
                return True

        if self.random_right > 0:
            if random.randint(0, self.random_right) == 0:
                if self.separate_random_triggers:
                    self.preHandler()
                    self.post()
                return True
        if not (self.trigger_in or self.trigger_strict):
            self.preHandler()
            self.post()
            return True

        for el in self.trigger_in:
            if self.obj.text.lower().find(el) != -1:
                self.preHandler()
                self.post()
                return True
        for el in self.trigger_strict:
            if self.obj.text.lower() == el:
                self.preHandler()
                self.post()
                return True

    def preHandler(self):
        """
        Функция для кастомных условий
        """
        pass

    def post(self):
        self.vk.messages.send(peer_id=self.obj.peer_id, random_id=0, message=self.message_data.message,
                              attachment=self.message_data.attachment, reply_to=self.message_data.reply,
                              forward_messages=self.message_data.forward_mes, forward=self.message_data.forward,
                              sticker_id=self.message_data.sticker, keyboard=self.message_data.keyboard,
                              dont_parse_links=self.message_data.dont_parse_links,
                              disable_mentions=self.message_data.disable_mentions)
