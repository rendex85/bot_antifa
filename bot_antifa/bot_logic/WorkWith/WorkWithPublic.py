import random
from random import choice

from bot_antifa.bot_logic.WorkWith.MainWorkWith import BaseWorkWith
from bot_antifa.bot_logic.utils.WorkWithUtils.WorkWithAuth import AuthTools


class WallWorker(BaseWorkWith):
    def __init__(self, obj, peer_id="", msg="", vk="", public=""):
        super().__init__(obj, vk)
        self.vk = vk
        self.peer_id = peer_id
        self.msg = msg
        self.user_vk = AuthTools.authByUser()
        if public == "":
            self.public = ""
            strtssyl = self.msg.find("vk.com/")
            if strtssyl != -1:
                endssyl = self.msg[strtssyl + len("vk.com/"):].find(' ')
                if endssyl == -1:
                    self.public = self.msg[strtssyl + len("vk.com/"):]
                else:
                    self.public = self.msg[strtssyl + len("vk.com/"): endssyl]
            clown = vk.groups.getById(group_id=self.public, fields='counters')
        else:
            self.public = public

    def getRandomPublicPost(self):
        countofposts = self.user_vk.wall.get(owner_id="-" + str(self.public))["count"]
        # если я еще чтото буду длеать с волл гетом надо не заьыть про этот иф и ограничение на 100 постов
        if countofposts > 200:
            post_dict = self.user_vk.wall.get(owner_id="-" + str(self.public), offset=random.randint(0,countofposts-101), count=100)
            anek_choice = choice(list(post_dict["items"]))
            while anek_choice["text"] == "":
                anek_choice = choice(list(post_dict["items"]))
            return anek_choice
