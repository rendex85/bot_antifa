"""
Возможно, этот код омерзителен, но я лучше не придумал
"""


class BaseWorkWith:
    """
    Базовый класс для функциональной части бота
    """
    def __init__(self, obj, vk):
        self.vk = vk
        self.obj = obj


from .WorkWithDB import DataBaseTrigger, PermissionsWorker
from .WorkWithPictures import GetPicture
from .WorkWithText import GetText


class CompareWorkWithAll(GetPicture, GetText, DataBaseTrigger):
    """
    Объединяем весь функционал бота для доступа через единый интерфейс
    """
    def __init__(self, obj, vk):
        super().__init__(obj, vk)
