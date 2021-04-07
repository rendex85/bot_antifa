import threading

from vk_api.bot_longpoll import VkBotEventType

from EventHandler.registrator import list_of_triggers
from WorkWith.WorkWithAuth import AuthTools


def initiate_trigger(trigger, vk, obj):
    trigger(vk, obj)


def main():
    vk, longpoll = AuthTools.authByGroup()
    for event in longpoll.listen():
        threads = []
        if event.type == VkBotEventType.MESSAGE_NEW:
            for el in list_of_triggers:
                new_thread = threading.Thread(target=initiate_trigger, args=(el, vk, event.obj))
                threads.append(new_thread)
                new_thread.start()


if __name__ == '__main__':
    main()
