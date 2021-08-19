import random

from bot_logic.Databases.Models import Trigger, Answer, TriggerAnswer
from bot_logic.WorkWith.WorkWithStatic.WorkWithUsers import MembersConf
from bot_logic.consts import const_array
from bot_logic.consts.login_consts import admin_id
from bot_logic.utils.RegexUtils import compare_add_text, compare_add_media


class GetText:
    def __init__(self, obj, vk):
        self.obj = obj
        self.vk = vk

    def answer_who(self):
        getmember = MembersConf(self.obj, self.vk)
        msg_text = self.obj.text
        while msg_text.find('&quot;') > 0:
            i = msg_text.find('&quot;')
            msg_text = msg_text[:i] + '"' + msg_text[i + len('&quot;'):]
        msg_text = msg_text[msg_text.lower().find('!кто') + 4:]
        full_msg = random.choice(const_array.answ) + ' ' + getmember.getonemember()['full_name'] + msg_text
        return full_msg

    def answer_inf(self):
        full_msg = random.choice(const_array.answ) + self.obj.text[self.obj.text.lower().find(
            '!инфа') + 5:] + " с вероятностью " + str(random.randint(0, 100)) + "%"
        return full_msg

