import random

from consts import const_array
from utils.WorkWithUtils.WorkWithAuth import AuthTools
from utils.WorkWithUtils.WorkWithUpload import PhotoUpload
from utils.WorkWithUtils.WorkWithUsers import UserAnalyze
from .MainWorkWith import BaseWorkWith


class GetPicture(BaseWorkWith):
    def pic(self):
        return self.get_img('-84187544', 'wall', 'photo-84187544')

    def gat(self):
        choose_alb = random.choice(const_array.gatari_alb_lsit)
        return self.get_img('-7776162', choose_alb, 'photo-7776162')

    def chush(self):
        photo = UserAnalyze.getuser(self.vk, self.obj.from_id, "photo_50")[0]["photo_50"]
        attach = PhotoUpload.load_img(AuthTools.authByGroup()[2], photo)
        print(attach)
        return attach

    def cat(self):
        attach = PhotoUpload.load_img(AuthTools.authByGroup()[2], "https://thiscatdoesnotexist.com/")
        return attach

    def casper_cat(self):
        casper_attach = self.get_img_from_private_album("299186552", "276063968", "photo299186552", 1)
        return casper_attach

    def vasily_cat(self):
        vasily_attach = self.get_img_from_private_album("299186552", "280961377", "photo299186552", 1)
        return vasily_attach

    def gar(self):
        random_num = random.choice([0, 1])
        choose_alb = random.choice(const_array.photo_garik_list[random_num])
        photo_url = self.get_img(const_array.account_garik_list[random_num], choose_alb,
                                 'photo' + const_array.account_garik_list[random_num], 1)
        attach = PhotoUpload.load_img(AuthTools.authByGroup()[2], photo_url)
        return attach

    def get_img_from_private_album(self, owner, album, photo_obj_start, type_photo):
        photo_url = self.get_img(owner=owner, album=album, photo_obj_start=photo_obj_start, type=type_photo)
        attach = PhotoUpload.load_img(AuthTools.authByGroup()[2], photo_url)
        return attach

    """
    ты ушел брат ты ушел так рано
    
    def catWithAnek(self):
        attach = self.load.loadImg("https://thiscatdoesnotexist.com/")
        wallWork = WallWorker(public=92876084)
        text = ""
        try:
            text = wallWork.getRandomPublicPost()["text"]
        except KeyError:
            text = ""
        self.post(attach,text)
        """

    def get_img(self, owner, album, photo_obj_start, type=0):
        vk1 = AuthTools.authByUser()
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
