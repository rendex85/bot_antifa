import random

import vk_api

from Upload import PhotoUpload
from WorkWith.WorkWithUsers import UserAnalyze
from consts import const_array, login_consts


class GetPicture:

    def __init__(self, peer_id, from_id, vk_session, vk):
        self.peer_id = peer_id
        self.vk = vk
        self.vk_session1 = vk_api.VkApi(login_consts.phone, login_consts.password)
        self.user = UserAnalyze(from_id, vk)
        self.load = PhotoUpload(vk_session)

    def post(self, url_pic):
        self.vk.messages.send(peer_id=self.peer_id, random_id=0, attachment=url_pic)

    def pic(self):
        self.post(self.get_img('-84187544', 'wall', 'photo-84187544'))

    def gar(self):
        randomnum = random.choice([0, 1])
        choosen_alb = random.choice(const_array.photo_garik_list[randomnum])
        photo_url=self.get_img(const_array.account_garik_list[randomnum], choosen_alb, 'photo' + const_array.account_garik_list[randomnum], 1)
        attach = self.load.loadImg(photo_url)
        self.post(attach)


    def gat(self):
        choosen_alb = random.choice(const_array.gatari_alb_lsit)
        self.post(self.get_img('-7776162', choosen_alb, 'photo-7776162'))

    def chush(self):
        photo = self.user.getuser("photo_50")[0]["photo_50"]
        attach = self.load.loadImg(photo)
        self.post(attach)

    def get_img(self, owner, album, photo_obj_start, type=0):
        vk1=self.auth()
        url_pic=""
        pic_lenght = (dict(vk1.photos.get(owner_id=owner, album_id=album, offset=1, count='1', photo_sizes=0)))[
            'count']
        dict_of_img = dict(
            vk1.photos.get(owner_id=owner, album_id=album, offset=random.randint(0, pic_lenght - 1),
                           count='1'))
        if type==0:
            url_pic = (photo_obj_start + '_' + str(dict_of_img['items'][0]['id']))
        elif type==1:
            url_pic=dict_of_img['items'][0]['sizes'][-1]['url']
        return url_pic

    def auth(self):
        try:
            self.vk_session1.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
        vk1 = self.vk_session1.get_api()
        return vk1