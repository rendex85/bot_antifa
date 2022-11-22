import json
import random

from EventHandler.HandlerKernel import BaseHandler
from WorkWith.WorkWithDB import DataBaseTrigger
from consts import const_array, const_txt


class WhoHandler(BaseHandler):
    trigger_in = ["!кто", "!rnj"]

    def preHandler(self):
        self.message_data.message = self.working_methods.answer_who()


class InfHandler(BaseHandler):
    trigger_in = ["!инфа", ]

    def preHandler(self):
        self.message_data.message = self.working_methods.answer_inf()


class AddHandler(BaseHandler):
    do_threading = True
    trigger_in = ["!добавить", ]

    def preHandler(self):
        self.message_data.message = self.working_methods.add_to_db()


class RemoveHandler(BaseHandler):
    do_threading = True
    trigger_in = ["!убрать", ]

    def preHandler(self):
        self.message_data.message = self.working_methods.remove_from_db()


class TriggerHandler(BaseHandler):
    do_threading = True
    trigger_in = [""]

    # Если честно - говнокод
    def preHandler(self):
        trigger_id, chance, command = self.working_methods.get_trigger()
        if trigger_id and random.randint(0, chance) == 0:
            self.command = command
            return_dict = DataBaseTrigger.get_answer_from_db(trigger_id)
            self.message_data.message = return_dict["text"]
            self.message_data.attachment = return_dict["picture"]
        else:
            self.do_post = False


class TriggersList(BaseHandler):
    do_threading = True
    trigger_in = ["!триггеры", ]

    def preHandler(self):
        try:
            self.message_data.message = self.working_methods.get_list_of_triggers()
        except KeyError:
            self.do_post = False


class PicHandler(BaseHandler):
    trigger_in = ["!пик", "!пикча", "!gbr", "!gbrxf", ]

    def preHandler(self):
        try:
            self.message_data.attachment = self.working_methods.pic()
        except KeyError or ValueError or IndexError:
            self.do_post = False


class GatHandler(BaseHandler):
    trigger_in = ["!гат", "!гатари", ]

    def preHandler(self):
        self.message_data.attachment = self.working_methods.gat()


class ChushHandler(BaseHandler):
    do_threading = True
    trigger_strict = ["чуш", ]
    random_right = 200
    separate_random_triggers = True

    def preHandler(self):
        self.message_data.attachment = self.working_methods.chush()


class CatHandler(BaseHandler):
    do_threading = True
    trigger_strict = ["!кот", "!rjn"]

    def preHandler(self):
        self.message_data.attachment = self.working_methods.cat()


class GarikHandler(BaseHandler):
    do_threading = True
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




class SaberHandler(BaseHandler):
    trigger_in = ["сейб", "сэйб", "сэиб"]

    def preHandler(self):
        self.message_data.message = const_txt.saiba


class WhatHandler(BaseHandler):
    trigger_strict = ["чо", "че", "чё"]

    def preHandler(self):
        self.message_data.sticker = 3380


class CatAHandler(BaseHandler):
    trigger_strict = ["a", "а"]
    random_right = 2

    def preHandler(self):
        self.message_data.attachment = 'photo-147805525_456240041'


class CerfAHandler(BaseHandler):
    trigger_strict = ["сука", "cerf", "мкеп"]
    random_right = 5

    def preHandler(self):
        self.message_data.attachment = const_array.cerf_list


class BanHandler(BaseHandler):
    do_threading = True
    trigger_in = ["!бан"]
    trigger_not_in = ["!разбан"]

    def preHandler(self):
        self.message_data.message = self.working_methods.ban()


class UnbanBanHandler(BaseHandler):
    do_threading = True
    trigger_in = ["!разбан"]

    def preHandler(self):
        self.message_data.message = self.working_methods.unban()


class CasperCat(BaseHandler):
    # TODO: Сделать кэш
    do_threading = True
    trigger_strict = ["!каспер", "!кот каспер", "!каспир", "!кот_каспер"]

    def preHandler(self):
        self.message_data.attachment = self.working_methods.casper_cat()


class ReportSmth(BaseHandler):
    do_threading = True
    trigger_in = ["!репорт"]

    def preHandler(self):
        self.message_data.forward = json.dumps({
            "peer_id": self.obj.peer_id,
            "conversation_message_ids": self.obj.conversation_message_id
        })
        self.obj.peer_id = 204181697


class VasilyCat(BaseHandler):
    do_threading = True
    trigger_strict = ["!марсик", "!муся", "!мурсик", "!кот василия", "!коты василия"]

    def preHandler(self):
        self.message_data.attachment = self.working_methods.vasily_cat()


class test_cache(BaseHandler):
    do_threading = True
    trigger_strict = ["!cac"]

    def preHandler(self):
        self.message_data.attachment = self.working_methods.cash_checker()
