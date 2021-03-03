import random

import vk_api

from Upload import PhotoUpload
from WorkWith.WorkWithAuth import AuthTools
from WorkWith.WorkWithPublic import WallWorker
from WorkWith.WorkWithUsers import UserAnalyze
from consts import const_array, login_consts


class GetPicture:

    def __init__(self, peer_id, from_id, vk_session, vk):
        self.peer_id = peer_id
        self.vk = vk
        self.user = UserAnalyze(from_id, vk)
        self.load = PhotoUpload(vk_session)

    def pic(self):
        return self.getImg('-84187544', 'wall', 'photo-84187544')

    def gar(self):
        randomnum = random.choice([0, 1])
        choosen_alb = random.choice(const_array.photo_garik_list[randomnum])
        photo_url = self.getImg(const_array.account_garik_list[randomnum], choosen_alb,
                                'photo' + const_array.account_garik_list[randomnum], 1)
        attach = self.load.loadImg(photo_url)
        return attach

    def gat(self):
        choosen_alb = random.choice(const_array.gatari_alb_lsit)
        return self.getImg('-7776162', choosen_alb, 'photo-7776162')

    def chush(self):
        photo = self.user.getuser("photo_50")[0]["photo_50"]
        attach = self.load.loadImg(photo)
        return attach

    def cat(self):
        attach = self.load.loadImg("https://thiscatdoesnotexist.com/")
        return attach

    def catWithAnek(self):
        attach = self.load.loadImg("https://thiscatdoesnotexist.com/")
        wallWork = WallWorker(public=92876084)
        text = ""
        try:
            text = wallWork.getRandomPublicPost()["text"]
        except KeyError:
            text = ""
        return attach, text

    def getImg(self, owner, album, photo_obj_start, type=0):
        vk1, longpoll = AuthTools().authByUser()

        url_pic = ""
        pic_lenght = (dict(vk1.photos.get(owner_id=owner, album_id=album, offset=1, count='1', photo_sizes=0)))[
            'count']
        dict_of_img = dict(
            vk1.photos.get(owner_id=owner, album_id=album, offset=random.randint(0, pic_lenght - 1),
                           count='1'))
        if type == 0:
            url_pic = (photo_obj_start + '_' + str(dict_of_img['items'][0]['id']))
        elif type == 1:
            url_pic = dict_of_img['items'][0]['sizes'][-1]['url']
        return url_pic
