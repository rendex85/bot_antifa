import threading

from vk_api.bot_longpoll import VkBotEventType

from Databases.UtilsDB import ConnectDB
from EventHandler.HandlerKernel import BaseHandler
from utils.WorkWithUtils.WorkWithAuth import AuthTools


class MainLoop:
    TURN_ON = True
    DICT_OF_GLOBAL_VARIABLES = \
        {
            "chess_objects_list": []
        }

    def initiate_trigger(self, trigger, vk, obj, global_list):
        trigger(vk, obj, global_list)

    def run(self):
        vk, longpoll, vk_session = AuthTools.authByGroup()
        database = ConnectDB.get_connection()
        ConnectDB.create_tables(database)
        database.close()
        for event in longpoll.listen():
            threads = []
            if event.type == VkBotEventType.MESSAGE_NEW and self.TURN_ON:
                for el in BaseHandler.__subclasses__():
                    new_thread = threading.Thread(target=self.initiate_trigger,
                                                  args=(el, vk, event.obj, self.DICT_OF_GLOBAL_VARIABLES))
                    threads.append(new_thread)
                    new_thread.start()
                    # new_thread.join()


if __name__ == '__main__':
    while True:
        try:
            main_loop = MainLoop()
            main_loop.run()
        except Exception as e:
            print(e)
