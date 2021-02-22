import random
from typing import List

from utils.DataClassUtils import Message


class BaseHandler:
    trigger_in: List[str] = []
    trigger_strict: List[str] = []
    random_right: int = 0

    def __init__(self, vk, obj):
        self.vk = vk
        self.obj = obj
        self.message_data = Message()
        self.initiator()

    def initiator(self):
        if self.random_right > 0:
            if random.randint(0, self.random_right) == 0:
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
            if self.obj.text.lower == el:
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
