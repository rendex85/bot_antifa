import io

import requests
from vk_api import VkUpload, VkApi


class PhotoUpload:
    """
    Класс для работы с загрузкой фотографий
    """

    @staticmethod
    def load_img(vk_session: VkApi, image_url: str) -> str:
        """
        Загрузка картинок в вк по URL

        :param vk_session: сессия вк за паблик
        :param image_url: ссылка на картинку, которю надо загрузить
        :return: vk photo id with prefix
        """
        session = requests.Session()
        upload = VkUpload(vk_session)
        image = session.get(image_url, stream=True)
        photo = upload.photo_messages(photos=image.raw)[0]
        return 'photo{}_{}'.format(photo['owner_id'], photo['id'])

    @staticmethod
    def load_img_from_local_data(vk_session: VkApi, image:io.BytesIO) -> str:
        """
        Загружает фотографию в вк с машины/оперативной памяти

        :param vk_session:
        :param image:
        :return:vk photo id with prefix
        """
        upload = VkUpload(vk_session)
        photo = upload.photo_messages(photos=image)[0]
        return 'photo{}_{}'.format(photo['owner_id'], photo['id'])
