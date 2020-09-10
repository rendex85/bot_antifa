import threading

import requests
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from Databases.TextAnswersQuery import *
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
            txt_find = WorkWithText(peer, from_id, event.obj.text, vk)
            if (event.obj.text == '!ладдер') or (event.obj.text == '!лад'):
                lader = open(str(event.obj.peer_id) + '_lader' + '.txt', encoding="utf8")
                strlader = lader.read()
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message=strlader)
                lader.close()
            if (event.obj.text == '!пик' or event.obj.text == '!пикча'):
                picture = GetPicture(peer, from_id,vk_session, vk)
                picture.pic()
            if (event.obj.text == '!гат' or event.obj.text == '!гатари'):
                picture = GetPicture(peer, from_id,vk_session, vk)
                picture.gat()
            if (event.obj.text.lower().find('!кто') != (-1)):
                answer_txt = TextAnswer(peer, vk)
                answer_txt.answerwho(event.obj.text)
            if (event.obj.text == "чуш"):
                answer_photo = GetPicture(peer, from_id, vk_session, vk)
                answer_photo.chush()
            if event.obj.text.lower().find('!инфа') != (-1):
                strt = event.obj.text
                randosha = str(random.randint(1, 100))
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0,
                                 message=(random.choice(const_array.answ) + strt[(strt).lower().find(
                                     '!инфа') + 5:] + " с вероятностью " + randosha + "%"))

            if (event.obj.text.lower().find('гитлер') != (-1)) or (event.obj.text.lower().find('нациз') != (-1)) or (
                    event.obj.text.lower().find('нацис') != (-1)) or (event.obj.text.lower().find('гитлир') != (-1)):
                if random.randint(1, 3) == 3:
                    vk.messages.send(peer_id=event.obj.peer_id, random_id=0,
                                     attachment=random.choice(const_array.naz_list))
            if (event.obj.text.lower().find('гача') != (-1)) or (event.obj.text.lower().find('фго') != (-1)):
                if random.randint(1, 3) == 3:
                    vk.messages.send(peer_id=event.obj.peer_id, random_id=0,
                                     attachment=random.choice(const_array.gacha_list))
            if random.randint(1, 200) == 100:
                answer_photo = GetPicture(peer, from_id, vk_session, vk)
                answer_photo.chush()
            if random.randint(1, 1000) == 228:
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, attachment='doc204181697_493314661')
            if (event.obj.text.lower().find('сука') != (-1)) or (event.obj.text.lower().find('cerf') != (-1)):
                if random.randint(1, 10) == 3:
                    vk.messages.send(peer_id=event.obj.peer_id, random_id=0,
                                     attachment=random.choice(const_array.cerf_list))
            if (event.obj.text.lower().find('аборт') != (-1)) or (event.obj.text.lower().find('пример') != (-1)) or (
                    event.obj.text.lower().find('критерий') != (-1)):
                if random.randint(1, 5) == 3:
                    vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message=abort)
            if event.obj.text.find('😊') != (-1):
                if random.randint(1, 2) == 2:
                    vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message='&#128522;')
            if event.obj.text.lower().find('артур') != -1 or event.obj.text.lower().find(
                    'сеиб') != -1 or event.obj.text.lower().find('сейб') != -1 or event.obj.text.lower().find(
                'сэйб') != -1 or event.obj.text.lower().find('сэиб') != -1:
                if random.randint(1, 3) == 1:
                    vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message=saiba)
            if event.obj.text.lower() == 'че' or event.obj.text.lower() == 'чо' or event.obj.text.lower() == 'чё':
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, attachment='photo-89104511_456239018')
            if event.obj.text.lower() == 'а':
                if random.randint(1, 3) == 3:
                    vk.messages.send(peer_id=event.obj.peer_id, random_id=0, attachment='photo-147805525_456240041')
            if event.obj.text.lower().find('фаши') != (-1):
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message=(fascist))
            if event.obj.text == '14':
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="88")
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="МЫ НЕ ОДОБРЯЕМ")
            if (event.obj.text == "[club178122731|*public178122731] top anime"):
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="завали свой гнилой еблет")
            if (event.obj.text.lower().find('я ') == 0) or (
                    (len(event.obj.text) == 1) and event.obj.text.lower()[0] == 'я'):
                if random.randint(1, 15) == 1:
                    vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message='ты-то')

            if (event.obj.text.lower().find("!добавить") != -1 and (
                    from_id == 232282950 or from_id == 204181697 or from_id == 576191490)):
                add = threading.Thread(target=txt_find.addToBase)
                add.start()
                add.join()
            if (event.obj.text.lower().find("!убрать") != -1 and (
                    from_id == 232282950 or from_id == 204181697)):
                rem = threading.Thread(target=txt_find.removeFromBase)
                rem.start()
                rem.join()
            answ = threading.Thread(target=txt_find.answer)
            answ.start()
            answ.join()


if __name__ == '__main__':
    d = 0
    while d == 0:
        try:
            main()
        except:
            d = 0
