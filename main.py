import requests
from vk_api import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from MembersConf import *
import login_consts
from TextAnswer import  *

from GetPicture import *

session = requests.Session()

vk_session = vk_api.VkApi(token=login_consts.token)
longpoll = VkBotLongPoll(vk_session,login_consts.public )
vk = vk_session.get_api()
upload = VkUpload(vk_session)



for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        peer=event.obj.peer_id
        answer_send=TextAnswer(peer, vk)
        picture = GetPicture(peer,vk)
        if (event.obj.text == '!пик' or event.obj.text == '!пикча'):
            picture.pic()
        if (event.obj.text == '!гат' or event.obj.text == '!гатари'):
            picture.gat()
        if (event.obj.text.lower().find('!кто') != (-1)):
            answer_send.answerwho(event.obj.text)
        if (event.obj.text=="!мать"):
            vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="мать жива")
        if (event.obj.text == "*public178122731 top anime"):
            vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="завали сой гнилой еблет")