import requests
from vk_api import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from MembersConf import *
import login_consts

from GetPicture import *

session = requests.Session()

vk_session = vk_api.VkApi(token=login_consts.token)
longpoll = VkBotLongPoll(vk_session,login_consts.public )
vk = vk_session.get_api()
upload = VkUpload(vk_session)

picture = GetPicture()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if (event.obj.text == '!пик' or event.obj.text == '!пикча'):
            picture.pic(event.obj.peer_id, vk)
        if (event.obj.text == '!гат' or event.obj.text == '!гатари'):
            picture.gat(event.obj.peer_id, vk)

        if (event.obj.text=="!мать"):
            vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="мать жива")
            print(MembersConf(vk,event.obj.peer_id).getonemember())
