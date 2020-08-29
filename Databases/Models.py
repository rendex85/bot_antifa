from peewee import *
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Bot.db")
conn = SqliteDatabase(db_path,  pragmas={'foreign_keys': 1})


class BaseModel(Model):
    conn.connect()
    class Meta:
        database = conn

class Answer(BaseModel):
    answer_id = AutoField(column_name='answer_id')
    answer_text = TextField(column_name='answer_text')

    class Meta:
        database = conn
        table_name = 'Answer'


class Trigger(BaseModel):
    trigger_id = AutoField(column_name='trigger_id')
    trigger_text = TextField(column_name='trigger_text')

    class Meta:
        database = conn
        table_name = 'Trigger'


class TriggerAnsw(BaseModel):
    trig_answ_id = AutoField(column_name='trig_answ_id')
    trigger_link= ForeignKeyField(Trigger, column_name='trigger_link', on_delete='CASCADE')
    answer_link = ForeignKeyField(Answer, column_name='answer_link', on_delete='CASCADE')

    class Meta:
        database = conn
        table_name = 'TriggerAnsw'
