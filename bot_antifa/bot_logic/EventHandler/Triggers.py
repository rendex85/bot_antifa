import random

from bot_logic.EventHandler.HandlerKernel import BaseHandler
from bot_logic.consts import const_array, const_txt


class WhoHandler(BaseHandler):
    trigger_in = ["!кто", ]

    def preHandler(self):
        self.message_data.message = self.working_methods.answer_who()


class InfHandler(BaseHandler):
    trigger_in = ["!инфа", ]

    def preHandler(self):
        self.message_data.message = self.working_methods.answer_inf()


class AddHandler(BaseHandler):
    trigger_in = ["!добавить", ]

    def preHandler(self):
        self.message_data.message = self.working_methods.add_to_db()


class PicHandler(BaseHandler):
    trigger_strict = ["!пик", "!пикча", "!gbr", "!gbrxf", ]

    def preHandler(self):
        self.message_data.attachment = self.working_methods.pic()


class ChushHandler(BaseHandler):
    trigger_strict = ["чуш", ]
    random_right = 200
    separate_random_triggers = True

    def preHandler(self):
        self.message_data.attachment = self.working_methods.chush()


class CatHandler(BaseHandler):
    trigger_strict = ["!кот", "!rjn"]

    def preHandler(self):
        self.message_data.attachment = self.working_methods.cat()


class GarikHandler(BaseHandler):
    trigger_strict = ["!непик", ]

    def preHandler(self):
        self.message_data.attachment = self.working_methods.gar()


class NaziHandler(BaseHandler):
    trigger_in = ["гитлер", "нациз", 'нацис', 'гитлир']
    random_right = 2

    def preHandler(self):
        self.message_data.attachment = random.choice(const_array.naz_list)


class GachaHandler(BaseHandler):
    trigger_in = ["гача", "фго", ]
    random_right = 2

    def preHandler(self):
        self.message_data.attachment = random.choice(const_array.gacha_list)


class FashiHandler(BaseHandler):
    trigger_in = ["фаши", ]
    trigger_not_in = ["мы против фашизма", ]

    def preHandler(self):
        self.message_data.message = const_txt.fascist


class SaberHandler(BaseHandler):
    trigger_in = ["сейб", "сэйб", "сэиб"]

    def preHandler(self):
        self.message_data.message = const_txt.saiba


class WhatHandler(BaseHandler):
    trigger_strict = ["чо", "че", "чё "]

    def preHandler(self):
        self.message_data.sticker = 3380


class CatAHandler(BaseHandler):
    trigger_strict = ["a", "а"]
    random_right = 2

    def preHandler(self):
        self.message_data.attachment = 'photo-147805525_456240041'


class CerfAHandler(BaseHandler):
    trigger_strict = ["сука", "cerf"]
    random_right = 10

    def preHandler(self):
        self.message_data.attachment = const_array.cerf_list
