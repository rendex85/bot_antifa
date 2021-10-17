import random

from .MainWorkWith import BaseWorkWith
from consts import const_array
from utils.WorkWithUtils.WorkWithUsers import MembersConf


class GetText(BaseWorkWith):

    def answer_who(self) -> str:
        """
        Легендарная команда !кто, выбирает случайного человека из конференции и обзывает его частью текста после "!кто"
        :return: Возвращает текст сообщения с ответом на команду
        """
        getmember = MembersConf(self.obj, self.vk)
        msg_text = self.obj.text
        while msg_text.find('&quot;') > 0:
            i = msg_text.find('&quot;')
            msg_text = msg_text[:i] + '"' + msg_text[i + len('&quot;'):]
        msg_text = msg_text[msg_text.lower().find('!кто') + 4:]
        full_msg = random.choice(const_array.answ) + ' ' + getmember.getonemember()['full_name'] + msg_text
        return full_msg

    def answer_inf(self) -> str:
        """
        Команда !инфа, показывает вероятность события в сообщении после "!инфа"
        :return: Возвращает текс сообщения с ответом на команду
        """
        full_msg = random.choice(const_array.answ) + self.obj.text[self.obj.text.lower().find(
            '!инфа') + 5:] + " с вероятностью " + str(random.randint(0, 100)) + "%"
        return full_msg
