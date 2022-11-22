from vk_api import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.vk_api import VkApiMethod, VkApi

from consts import login_consts


class AuthTools:
    """
    Все крутые штуки с авторизацией в вк происходят здесь
    """

    @staticmethod
    def authByUser() -> VkApiMethod:
        """
        Функция логирования за пользователя.
        Логин и пароль указывается в login_const
        :return: vk user session object
        """
        print(login_consts.phone, login_consts.password)
        vk_session1 = vk_api.VkApi(str(login_consts.phone), str(login_consts.password))
        try:
            vk_session1.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
        return vk_session1.get_api()

    @staticmethod
    def authByGroup() -> (VkApiMethod, VkBotLongPoll, VkApi):
        """
        Функция логирования за группу.
        Токен и id паблика храниться в login_const
        :return: vk obj, longpoll obj, vk group session obj
        """
        vk_session = vk_api.VkApi(token=login_consts.token)
        longpoll = VkBotLongPoll(vk_session, login_consts.public)
        vk = vk_session.get_api()
        return vk, longpoll, vk_session
