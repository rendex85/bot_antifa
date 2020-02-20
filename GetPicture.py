import random

import vk_api
import  const_array
import  login_consts

class GetPicture:
    login, password = login_consts.phone, login_consts.password
    vk_session1 = vk_api.VkApi(login, password)

    def __init__(self, peer_id, vk):
        self.peer_id=peer_id
        self.vk=vk

    def post(self, url_pic):
        self.vk.messages.send(peer_id=self.peer_id, random_id=0, attachment=url_pic)

    def pic(self):
        self.post(self.get_img('-84187544','wall','photo-84187544'))

    def gat(self):
        choosen_alb=random.choice(const_array.gatari_alb_lsit)
        self.post(self.get_img('-7776162',choosen_alb,'photo-7776162'))


    def get_img(self,owner,album,photo_obj_start):
        try:
            self.vk_session1.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
        vk1 = self.vk_session1.get_api()

        pic_lenght = (dict(vk1.photos.get(owner_id=owner, album_id=album, offset=1, count='1', photo_sizes=0)))[
            'count']
        dict_of_img = dict(
            vk1.photos.get(owner_id=owner, album_id=album, offset=random.randint(0, pic_lenght - 1),
                           count='1'))
        url_pic = (photo_obj_start + '_' + str(dict_of_img['items'][0]['id']))
        return  url_pic


