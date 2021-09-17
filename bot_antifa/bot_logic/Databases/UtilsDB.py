from peewee import PostgresqlDatabase

from bot_antifa.bot_logic.Databases.Models import BaseModel
from bot_antifa.bot_logic.consts.login_consts import db_host, db_port, db_password, db_user


class ConnectDB:
    @staticmethod
    def get_connection():
        return PostgresqlDatabase('bot_db', user=db_user, password=db_password,
                                  host=db_host, port=int(db_port))

    @staticmethod
    def create_tables(connection):
        connection.create_tables(BaseModel.__subclasses__())
