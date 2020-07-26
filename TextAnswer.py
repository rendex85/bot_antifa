import const_array
from WorkWithUsers import *


class TextAnswer(MembersConf):
    def answerwho(self, msg_text):
        while msg_text.find('&quot;') > 0:
            i = msg_text.find('&quot;')
            msg_text = msg_text[:i] + '"' + msg_text[i + len('&quot;'):]
        msg_text = msg_text[(msg_text).lower().find('!кто') + 4:]
        full_msg = random.choice(const_array.answ) + ' ' + self.getonemember()['full_name'] + ' ' + msg_text
        self.sendmsg(full_msg)

    def sendmsg(self, msg):
        self.vk.messages.send(peer_id=self.peer_id, random_id=0, message=msg)
