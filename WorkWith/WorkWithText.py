from consts import const_array
from WorkWith.WorkWithUsers import *


class TextAnswer():
    def __init__(self, peer_id, vk):
        self.vk=vk
        self.peer_id=peer_id

    def answerwho(self, msg_text):
        self.getmember = MembersConf(self.peer_id, self.vk)
        while msg_text.find('&quot;') > 0:
            i = msg_text.find('&quot;')
            msg_text = msg_text[:i] + '"' + msg_text[i + len('&quot;'):]
        msg_text = msg_text[(msg_text).lower().find('!кто') + 4:]
        full_msg = random.choice(const_array.answ) + ' ' + self.getmember.getonemember()['full_name'] + msg_text
        self.sendmsg(full_msg)

    def sendmsg(self, msg):
        self.vk.messages.send(peer_id=self.peer_id, random_id=0, message=msg)
