from bot_antifa.bot_logic.Databases.Models import UserStuff, Permission
from bot_antifa.bot_logic.consts.login_consts import admin_id
from bot_antifa.bot_logic.utils.WorkWithUtils.WorkWithUsers import MembersConf


class PermissionChecker:
    def __init__(self, obj, vk):
        self.obj = obj
        self.vk = vk

    def is_user_admin_in_conference(self) -> bool:
        admin_list = MembersConf(self.obj, self.vk).get_admin_list()
        if self.obj.from_id in admin_list:
            return True
        else:
            return False

    def is_user_admin(self) -> bool:
        if int(self.obj.from_id) == int(admin_id) or \
                UserStuff.filter(user_vk_id=int(self.obj.from_id)).execute():
            return True
        else:
            return False

    def is_user_banned(self) -> bool:
        if Permission.filter(user_vk_id=self.obj.from_id, conference_id=None,
                             command_name=None).execute() and not self.is_user_admin():
            return True
        elif Permission.filter(user_vk_id=self.obj.from_id, conference_id=self.obj.peer_id,
                               command_name=None).execute() and not (
                self.is_user_admin_in_conference() or self.is_user_admin()):
            return True
        else:
            return False

    def is_command_banned(self, command) -> bool:
        for el in Permission.filter(user_vk_id=None, conference_id=self.obj.peer_id,
                                    command_name=command).execute():
            print(el)
        if Permission.filter(user_vk_id=None, conference_id=None,
                             command_name=command).execute() and not self.is_user_admin():
            return True
        elif Permission.filter(user_vk_id=None, conference_id=self.obj.peer_id,
                               command_name=command).execute() and not (
                self.is_user_admin_in_conference() or self.is_user_admin()):
            return True
        elif Permission.filter(user_vk_id=self.obj.from_id, conference_id=self.obj.peer_id,
                               command_name=command).execute() and not (
                self.is_user_admin_in_conference() or self.is_user_admin()):
            return True
        else:
            return False
