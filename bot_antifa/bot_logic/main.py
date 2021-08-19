import threading

from vk_api.bot_longpoll import VkBotEventType

from bot_logic.Databases.UtilsDB import ConnectDB
from bot_logic.EventHandler.registrator import list_of_triggers
from bot_logic.WorkWith.WorkWithStatic.WorkWithAuth import AuthTools


class MainLoop:
    TURN_ON = True

    def initiate_trigger(self, trigger, vk, obj):
        trigger(vk, obj)

    def run(self):
        vk, longpoll, vk_session = AuthTools.authByGroup()
        database = ConnectDB.get_connection()
        ConnectDB.create_tables(database)
        database.close()
        for event in longpoll.listen():
            threads = []
            if event.type == VkBotEventType.MESSAGE_NEW and self.TURN_ON:
                for el in list_of_triggers:
                    new_thread = threading.Thread(target=self.initiate_trigger, args=(el, vk, event.obj))
                    threads.append(new_thread)
                    new_thread.start()
                    new_thread.join()


if __name__ == '__main__':
    main_loop = MainLoop()
    main_loop.run()
