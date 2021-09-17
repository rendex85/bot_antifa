class BaseWorkWith:
    def __init__(self, obj, vk):
        self.vk = vk
        self.obj = obj


from bot_logic.WorkWith.WorkWithDB import DataBaseTrigger, PermissionsWorker
from bot_logic.WorkWith.WorkWithPictures import GetPicture
from bot_logic.WorkWith.WorkWithText import GetText


class CompareWorkWithAll(GetPicture, GetText, DataBaseTrigger, PermissionsWorker):
    def __init__(self, obj, vk):
        super().__init__(obj, vk)
