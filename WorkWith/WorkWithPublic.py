import random
from random import choice

from WorkWith.WorkWithAuth import AuthTools


class WallWorker:
    def __init__(self, peer_id="", msg="", vk="", public=""):
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
            postDict = self.user_vk.wall.get(owner_id="-" + str(self.public), offset=random.randint(0,countofposts-101), count=100)
            anek_choice = choice(list(postDict["items"]))
            while anek_choice["text"] == "":
                anek_choice = choice(list(postDict["items"]))
            return anek_choice
