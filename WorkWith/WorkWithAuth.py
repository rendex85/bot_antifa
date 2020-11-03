from vk_api import vk_api

from consts import login_consts


class AuthTools():
    @staticmethod
    def authByUser():
        vk_session1 = vk_api.VkApi(login_consts.phone, login_consts.password)
        try:
            vk_session1.auth(token_only=True)
        except vk_api.AuthError as error_msg:
            print(error_msg)
        return vk_session1.get_api()