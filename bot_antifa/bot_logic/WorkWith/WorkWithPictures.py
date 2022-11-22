import inspect

import random
import threading
import time

from consts import const_array
from utils.WorkWithUtils.WorkWithAuth import AuthTools
from utils.WorkWithUtils.WorkWithUpload import PhotoUpload
from utils.WorkWithUtils.WorkWithUsers import UserAnalyze
from utils.cache_utils import cache_finder_photo, cache_append
from .MainWorkWith import BaseWorkWith


class GetPicture(BaseWorkWith):
    def pic(self) -> str:
        """
        Для команды !пик
        :return: vk photo id with prefix
        """
        split_data_message = self.obj.text.split(" ")
        if split_data_message[0] in ["!пик", "!пикча", "!gbr", "!gbrxf", ]:
            if len(split_data_message) == 1:
                return self.get_img('-84187544', 'wall', )
            elif (int(split_data_message[1]) in range(1, 11)) and len(split_data_message) == 2:
                return self.get_img('-84187544', 'wall', count_of_pics=int(split_data_message[1]))
        else:
            raise KeyError

    def gat(self) -> str:
        """
        для команды !гат
        :return:  vk photo id with prefix
        """
        choose_alb = random.choice(const_array.gatari_alb_lsit)
        return self.get_img(owner='-7776162', album=choose_alb)

    def chush(self) -> str:
        """
        для ChushHandler
        :return: vk photo id with prefix
        """
        photo = UserAnalyze.getuser(self.vk, self.obj.from_id, "photo_50")[0]["photo_50"]
        attach = PhotoUpload.load_img(AuthTools.authByGroup()[2], photo)
        return attach

    def cat(self) -> str:
        """
        команда !кот
        :return: vk photo id with prefix
        """
        attach = PhotoUpload.load_img(AuthTools.authByGroup()[2], "https://thiscatdoesnotexist.com/")
        return attach

    def casper_cat(self) -> str:
        """
        команда !каспер
        :return: vk photo id with prefix
        """
        casper_attach = self.get_img(owner="299186552", album="276063968", get_from="user",
                                     caller_name=inspect.currentframe().f_code.co_name)
        return casper_attach

    def vasily_cat(self) -> str:
        """
        коты василия шуйского
        :return: vk photo id with prefix
        """
        vasily_attach = self.get_img(owner="299186552", album="280961377", get_from="user",
                                     caller_name=inspect.currentframe().f_code.co_name)
        return vasily_attach

    def cash_checker(self) -> str:
        """
        коты василия шуйского
        :return: vk photo id with prefix
        """
        vasily_attach = self.get_img(owner="204181697", album="274033486", get_from="user",
                                     caller_name=inspect.currentframe().f_code.co_name)
        return vasily_attach

    def gar(self) -> str:
        """
        Что-то из альбомов гарика, работает через раз  и я не собираюсь это чинить.
        :return: vk photo id with prefix
        """
        random_num = random.choice([0, 1])
        choose_alb = random.choice(const_array.photo_garik_list[random_num])
        photo_url = self.get_img(owner=const_array.account_garik_list[random_num], album=choose_alb, get_from="user")
        return photo_url

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

    def get_img(self, owner: str, album: str, get_from: str = "public", count_of_pics: int = 1,
                pic_length_delta: int = 1, caller_name=None) -> str:
        """
        Основная функция, отвественная за достование картинок откуда либо
        :param caller_name: Имя функции, вызвавшей get_img. Нужно для кэширования
        :param owner: сурс страницы/паблика откуда берутся картинки
        :param album: альбом картинок
        :param get_from: явное указание откуда мы берем картинки (public, user)
        :param count_of_pics:  Какое количество картинок хотелось бы в ответе (работает пока только для пабликов)
        :param pic_length_delta: для того чтобы не словить IndexError
        :return: vk photo id with prefix
        """
        vk1 = AuthTools.authByUser()
        pic_string = ""
        # получаем количество картинок в альбоме
        pic_length = (dict(vk1.photos.get(owner_id=owner, album_id=album, offset=1, count='1', photo_sizes=0)))[
            'count']
        # выбираем, сколько картинок доставать из вк
        if count_of_pics == 1:
            count_of_pics_in_dict = 1
        else:
            count_of_pics_in_dict = 1000 if pic_length > 1000 else pic_length
        # получаем словарик с нужным количеством картинок со случайным смещением по альбому
        dict_of_img = dict(
            vk1.photos.get(owner_id=owner, album_id=album, offset=random.randint(0, pic_length - pic_length_delta),
                           count=str(count_of_pics_in_dict)))
        # в зависимости от выбранного типа достаем пикчуру
        if get_from == "public":
            for _ in range(0, count_of_pics):
                pic_object = random.choice(dict_of_img['items'])
                pic_string += f"photo{owner}_" + str(pic_object["id"]) + ","
            return pic_string

        elif get_from == "user":
            url_pic = dict_of_img['items'][0]['sizes'][-1]['url']
            # Если мы передаем информацию для кеширования
            if caller_name:
                pic_string = cache_finder_photo(cache_dict=self.dict_of_globals, url=url_pic, type_name=caller_name)
                if not pic_string:
                    pic_string = PhotoUpload.load_img(AuthTools.authByGroup()[2], url_pic)
                    cache_append(cache_dict=self.dict_of_globals, url=url_pic, type_name=caller_name, value=pic_string)
            else:
                pic_string = PhotoUpload.load_img(AuthTools.authByGroup()[2], url_pic)
        return pic_string
