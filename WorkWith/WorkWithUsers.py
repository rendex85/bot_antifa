import random


class MembersConf():
    def __init__(self, peer_id, vk):
        self.vk = vk
        self.peer_id = peer_id
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
        print(self.list_of_members)
        return (random.choice(self.list_of_members))


class UserAnalyze():
    def __init__(self, from_id, vk):
        self.vk = vk
        self.from_id = from_id

    def getuser(self, params):
        return (self.vk.users.get(user_ids=self.from_id, fields=params))