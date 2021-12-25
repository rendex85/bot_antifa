"""
Возможно, этот код омерзителен, но я лучше не придумал
"""


class BaseWorkWith:
    """
    Базовый класс для функциональной части бота
    """

    def __init__(self, obj, vk, dict_of_globals=None):
        self.obj = obj
        self.vk = vk
        self.dict_of_globals = dict_of_globals


from .WorkWithDB import DataBaseTrigger, PermissionsWorker
from .WorkWithPictures import GetPicture
from .WorkWithText import GetText


class CompareWorkWithAll(GetPicture, GetText, DataBaseTrigger, PermissionsWorker):
    """
    Объединяем весь функционал бота для доступа через единый интерфейс
    """

    def __init__(self, obj, vk, dict_of_globals):
        super().__init__(obj, vk, dict_of_globals)
