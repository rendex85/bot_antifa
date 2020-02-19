import random

import vk_api
import  const_array
import  login_consts

class GetPicture:
    login, password = login_consts.phone, login_consts.password
    vk_session1 = vk_api.VkApi(login, password)

    def post(self, obj, vk, url_pic):
        vk.messages.send(peer_id=obj, random_id=0, attachment=url_pic)

    def pic(self, obj, vk):
        try:
            self.vk_session1.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
        vk1 = self.vk_session1.get_api()
        pic_lenght = (dict(vk1.photos.get(owner_id='-84187544', album_id='wall', offset=1, count='1', photo_sizes=0)))[
            'count']
        dcit_of_img = dict(
            vk1.photos.get(owner_id='-84187544', album_id='wall', offset=random.randint(0, pic_lenght - 1),
                           count='1'))
        url_pic = ('photo-84187544' + '_' + str(dcit_of_img['items'][0]['id']))
        self.post(obj, vk, url_pic)

    def gat(self, obj, vk):
        try:
            self.vk_session1.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
        vk1 = self.vk_session1.get_api()
        choosen_alb=random.choice(const_array.gatari_alb_lsit)
        pic_lenght = (dict(vk1.photos.get(owner_id='-7776162', album_id=choosen_alb, offset=1, count='1', photo_sizes=0)))[
            'count']

