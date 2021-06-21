import inspect
import json
import threading

import requests
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from Databases.TextAnswersQuery import *
from EventHandler.Triggers import WhoHandler
from WorkWith.WorkWithAuth import AuthTools
from WorkWith.WorkWithPictures import *
from consts.const_txt import *

session = requests.Session()

vk_session = vk_api.VkApi(token=login_consts.token)
longpoll = VkBotLongPoll(vk_session, login_consts.public)
vk = vk_session.get_api()


def main():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            peer = event.obj.peer_id
            from_id = event.obj.from_id
            txt_find=1499
            #txt_find = WorkWithText(peer, from_id, event.obj.text, vk)
            picture = GetPicture(peer, from_id, vk_session, vk)
            if (event.obj.text.lower().find('mama'))!=-1:
                who=WhoHandler(vk, event.obj)



if __name__ == '__main__':
    main()
