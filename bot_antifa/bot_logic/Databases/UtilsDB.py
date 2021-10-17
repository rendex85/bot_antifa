from peewee import PostgresqlDatabase

from consts import login_consts
from .Models import BaseModel


class ConnectDB:
    """
    Класс для мэнэджмента основного БД-объкта
    """

    @staticmethod
    def get_connection():
        """
        Получаем объект базы данных бота
        Пользователь, хост и пароль от ДБ хранятся в файле login_consts
        :return:  peewee db obj
        """
        return PostgresqlDatabase('bot_db', user=login_consts.db_user, password=login_consts.db_password,
                                  host=login_consts.db_host, port=int(login_consts.db_port))

    @staticmethod
    def create_tables(connection):
        """
        Создаем таблицы, описанные в Databases/Models.py
        :param connection:  peewee db obj

        """
        connection.create_tables(BaseModel.__subclasses__())
