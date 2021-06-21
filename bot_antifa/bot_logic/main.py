import threading

from vk_api.bot_longpoll import VkBotEventType

from bot_logic.EventHandler.registrator import list_of_triggers
from bot_logic.WorkWith.WorkWithStatic.WorkWithAuth import AuthTools


class MainLoop(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    TURN_ON = True

    def initiate_trigger(self, trigger, vk, obj):
        trigger(vk, obj)

    def run(self):
        vk, longpoll, vk_session = AuthTools.authByGroup()
        for event in longpoll.listen():
            threads = []
            if event.type == VkBotEventType.MESSAGE_NEW and self.TURN_ON:
                for el in list_of_triggers:
                    new_thread = threading.Thread(target=self.initiate_trigger, args=(el, vk, event.obj))
                    threads.append(new_thread)
                    new_thread.start()
                    new_thread.join()

main_loop = MainLoop()
main_loop.start()
