from WorkWith.WorkWithUsers import *
from consts import const_array


class TextAnswer:
    def __init__(self, obj, vk):
        self.vk = vk
        self.obj = obj
        self.getmember = MembersConf(self.obj.peer_id, self.vk)

    def answer_who(self):
        msg_text = self.obj.text
        while msg_text.find('&quot;') > 0:
            i = msg_text.find('&quot;')
            msg_text = msg_text[:i] + '"' + msg_text[i + len('&quot;'):]
        msg_text = msg_text[msg_text.lower().find('!кто') + 4:]
        full_msg = random.choice(const_array.answ) + ' ' + self.getmember.getonemember()['full_name'] + msg_text
        return full_msg
