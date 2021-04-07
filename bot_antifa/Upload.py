import requests
from vk_api import VkUpload



class PhotoUpload:
    def __init__(self, vk_session):
        self.session = requests.Session()
        self.upload = VkUpload(vk_session)
    def loadImg (self, image):
        image = self.session.get(image, stream=True)
        photo = self.upload.photo_messages(photos=image.raw)[0]
        return 'photo{}_{}'.format(photo['owner_id'], photo['id'])