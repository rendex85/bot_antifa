import requests
from vk_api import *
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from WorkWithUsers import *
import login_consts
from TextAnswer import  *
from ObjAnswer import *

from GetPicture import *

session = requests.Session()

vk_session = vk_api.VkApi(token=login_consts.token)
longpoll = VkBotLongPoll(vk_session,login_consts.public )
vk = vk_session.get_api()



for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        peer=event.obj.peer_id
        from_id=event.obj.from_id
        answer_txt=TextAnswer(peer, vk)
        picture = GetPicture(peer,vk)
        answer_photo=PhotoAnswer(peer,from_id,vk,vk_session)
        user=UserAnalyze(from_id,vk)

        if (event.obj.text == '!пик' or event.obj.text == '!пикча'):
            picture.pic()
        if (event.obj.text == '!гат' or event.obj.text == '!гатари'):
            picture.gat()
        if (event.obj.text.lower().find('!кто') != (-1)):
            answer_txt.answerwho(event.obj.text)
        if (event.obj.text == "чуш"):
            answer_photo.chush()
        if random.randint(1, 200) == 100:
            answer_photo.chush()

        if (event.obj.text == "[club178122731|*public178122731] top anime"):
            vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="завали свой гнилой еблет")
        if (event.obj.text == "!мать"):
            vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="мать жива")
