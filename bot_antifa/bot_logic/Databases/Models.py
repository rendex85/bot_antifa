from peewee import *

from ..consts.login_consts import db_host, db_port, db_password, db_user


class BaseModel(Model):
    class Meta:
        database = PostgresqlDatabase('bot_db', user=db_user, password=db_password,
                                      host=db_host, port=int(db_port))


# Блок !добавить
class Answer(BaseModel):
    answer_id = PrimaryKeyField()
    answer_text = TextField(null=True)
    answer_picture = TextField(null=True)
    answer_doc = TextField(null=True)
    answer_video = TextField(null=True)
    answer_music = TextField(null=True)


class Trigger(BaseModel):
    STATUS_CHOICES = (
        (0, 'strict'),
        (1, 'in'),)
    trigger_id = PrimaryKeyField()
    trigger_text = TextField()
    trigger_chance = IntegerField(null=True)
    trigger_type = IntegerField(choices=STATUS_CHOICES)
    conference_id = IntegerField(null=True)


class TriggerAnswer(BaseModel):
    trigger_answer_id = PrimaryKeyField()
    trigger_link = ForeignKeyField(Trigger, on_delete='CASCADE')
    answer_link = ForeignKeyField(Answer, on_delete='CASCADE')


# Блок пермишеннов
class Permission(BaseModel):
    STATUS_CHOICES = (
        (0, 'For other users/Admins'),
        (1, 'No one'),)
    user_id = PrimaryKeyField()
    user_vk_id = TextField(null=True)
    conference_id = IntegerField(null=True)
    command_name = TextField(null=True)
    permission_status = IntegerField(choices=STATUS_CHOICES, default=0)


class UserStuff(BaseModel):
    user_id = PrimaryKeyField()
    user_vk_id = IntegerField()
    crud_triggers = BooleanField(null=True)
    crud_bans = BooleanField(null=True)
