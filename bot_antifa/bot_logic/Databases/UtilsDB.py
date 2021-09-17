from peewee import PostgresqlDatabase

from .Models import BaseModel
from consts.login_consts import db_host, db_port, db_password, db_user


class ConnectDB:
    @staticmethod
    def get_connection():
        return PostgresqlDatabase('bot_db', user=db_user, password=db_password,
                                  host=db_host, port=int(db_port))

    @staticmethod
    def create_tables(connection):
        connection.create_tables(BaseModel.__subclasses__())
