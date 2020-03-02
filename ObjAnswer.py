from WorkWithUsers import *
from Upload import *

class PhotoAnswer():
    def __init__(self, peer_id, from_id, vk, vk_session):
        self.peer_id=peer_id
        self.from_id=from_id
        self.vk=vk
        self.vk_session=vk_session
        self.user=UserAnalyze(from_id,vk)
        self.load=PhotoUpload(vk_session)

    def chush(self):
        photo=self.user.getuser("photo_50")[0]["photo_50"]
        attach=self.load.loadImg(photo)
        self.sendmsg(self.vk,self.peer_id,"",attach)



    def sendmsg(self,vk,peer_id,msg, attach):
        vk.messages.send(peer_id=peer_id, random_id=0, message=msg, attachment=attach)