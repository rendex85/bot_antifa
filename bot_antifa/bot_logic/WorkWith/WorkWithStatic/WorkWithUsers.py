import random


class MembersConf():
    def __init__(self, obj, vk):
        self.vk = vk
        self.obj=obj
        self.peer_id = obj.peer_id
        self.list_of_members = list()
        self.admin_list = list()
        self.memb_dict = dict(self.vk.messages.getConversationMembers(peer_id=self.peer_id))
        for i in self.memb_dict['profiles']:
            self.list_of_members.append(
                {'full_name': (i['first_name'] + ' ' + i['last_name']), 'id': i['id'], 'photo_miniature': i['photo_50'],
                 'type': 'profile'})
        for i in self.memb_dict['groups']:
            self.list_of_members.append(
                {'full_name': i['name'], 'id': i['id'], 'photo_miniature': i['photo_50'], 'type': 'group',
                 'admin': 'false'})
        for i in self.memb_dict['items']:
            if ('is_admin' in i) and (i['is_admin'] == True):
                self.admin_list.append({'id': i['member_id']})

    def getonemember(self):
        return (random.choice(self.list_of_members))


class UserAnalyze:
    @staticmethod
    def getuser(vk, from_id, params):
        return vk.users.get(user_ids=from_id, fields=params)