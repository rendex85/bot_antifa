import threading

from vk_api.bot_longpoll import VkBotEventType

from Databases.UtilsDB import ConnectDB
from EventHandler.HandlerKernel import BaseHandler
from utils.WorkWithUtils.WorkWithAuth import AuthTools


class MainLoop:
    """
    Не должно было быть классом, так сложились обстоятельства.
    Это входная точка в бота.
    """

    # Словарь с объектами для оперативной памяти бота
    DICT_OF_GLOBAL_VARIABLES = \
        {
            "chess_objects_list": []
        }

    def initiate_trigger(self, trigger, vk, obj, global_list):
        """
        Инициализация отдельного класа тригерра из списка по ссылке
        """
        trigger(vk, obj, global_list)

    def run(self):
        """
        Главная функция-обработчик бота
        """
        # Авторизируемся в вк
        vk, longpoll, vk_session = AuthTools.authByGroup()

        # Получаем коннект к базе данных и создаем таблицы
        database = ConnectDB.get_connection()
        ConnectDB.create_tables(database)
        database.close()
        threads = []
        # Слушаем лонгпулл
        for event in longpoll.listen():

            if event.type == VkBotEventType.MESSAGE_NEW:
                """
                Проходимся по всем наследникам бейсхенделра и получаем ссылки на все классы-наследники
                Все классы триггеров хранятся в пакете EventHandler
                """
                for trigger_class in BaseHandler.__subclasses__():
                    # Новый тред для отедльного класса
                    new_thread = threading.Thread(target=self.initiate_trigger,
                                                  args=(
                                                      trigger_class, vk, event.obj, self.DICT_OF_GLOBAL_VARIABLES))
                    threads.append(new_thread)
                    new_thread.start()
            if len(threads) > 2000:
                [thread.join() for thread in threads]
                threads = []


# TODO: Сделай уже нормальное логирование, дэбил
if __name__ == '__main__':
    while True:
        try:
            main_loop = MainLoop()
            main_loop.run()
        except Exception as e:
            print(e)
