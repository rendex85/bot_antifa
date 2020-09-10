import login_consts
import vk_api

class PublicWork():
    login, password = login_consts.phone, login_consts.password
    vk_session1 = vk_api.VkApi(login, password)
    def __init__(self, peer_id, message, vk):
        self.vk=vk
        self.peer_id=peer_id
        self.message=message
        self.pubname=""
        startssyl = message.find("vk.com/")
        if startssyl != -1:
            startssyl += len("vk.com/")
            enssyl = message[startssyl:]
            endssyl = enssyl.find(' ')
            if endssyl == - 1:
                self.pubname = message[startssyl:]
            else:
                self.pubname = enssyl[:endssyl]
