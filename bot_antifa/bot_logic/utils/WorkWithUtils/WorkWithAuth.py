from vk_api import vk_api
from vk_api.bot_longpoll import VkBotLongPoll

from bot_logic.consts import login_consts


class AuthTools():
    @staticmethod
    def authByUser():
        vk_session1 = vk_api.VkApi(str(login_consts.phone), str(login_consts.password))

        try:
            vk_session1.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
        return vk_session1.get_api()

    @staticmethod
    def authByGroup():
        vk_session = vk_api.VkApi(token=login_consts.token)
        longpoll = VkBotLongPoll(vk_session, login_consts.public)
        vk = vk_session.get_api()
        return vk, longpoll, vk_session
