from bot_logic.WorkWith.WorkWithPictures import GetPicture
from bot_logic.WorkWith.WorkWithText import GetText


class CompareWorkWithAll(GetPicture, GetText):
    def __init__(self, obj, vk):
        super().__init__(obj, vk)