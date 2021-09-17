


class BaseWorkWith:
    def __init__(self, obj, vk):
        self.vk = vk
        self.obj = obj


from .WorkWithDB import DataBaseTrigger, PermissionsWorker
from .WorkWithPictures import GetPicture
from .WorkWithText import GetText


class CompareWorkWithAll(GetPicture, GetText, DataBaseTrigger, PermissionsWorker):
    def __init__(self, obj, vk):
        super().__init__(obj, vk)
