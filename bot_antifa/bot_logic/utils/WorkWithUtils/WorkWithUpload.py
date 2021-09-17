import requests
from vk_api import VkUpload


class PhotoUpload:
    @staticmethod
    def load_img(vk_session, image):
        session = requests.Session()
        upload = VkUpload(vk_session)
        image = session.get(image, stream=True)
        photo = upload.photo_messages(photos=image.raw)[0]
        return 'photo{}_{}'.format(photo['owner_id'], photo['id'])
