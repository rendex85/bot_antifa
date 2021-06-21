import random

from antifa_main.models import Trigger, ResultOfTrigger
from bot_logic.WorkWith.WorkWithStatic.WorkWithUsers import MembersConf
from bot_logic.consts import const_array
from bot_logic.utils.RegexUtils import compare_add_text, compare_add_media


class GetText():
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

    def add_to_db(self):
        msg_text = str(self.obj.text)
        if compare_add_text(msg_text):
            list_of_parameters = msg_text[9:].split("|")
            result = ResultOfTrigger.objects.create(type_media=1, result_of_trigger=list_of_parameters[1])
            try:
                strict_data = bool(list_of_parameters[2])
            except IndexError:
                strict_data = False
            try:
                trigger = Trigger.objects.get(name=list_of_parameters[0])
            except Trigger.DoesNotExist:
                trigger = Trigger.objects.create(name=list_of_parameters[0], strict=strict_data)
            trigger.result.add(result)
            trigger.save()
            return f"Условие {list_of_parameters[0]} успешно добавлено!"
        elif compare_add_media(self.obj.text):
            pass
        else:
            return "Условие неверное"
