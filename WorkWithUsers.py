import random


class MembersConf():

    def __init__(self, peer_id, vk):
        self.vk=vk
        self.peer_id=peer_id
    def getMembers(self):
        list_of_members = list()
        admin_list = list()
        memb_dict = dict(self.vk.messages.getConversationMembers(peer_id=self.peer_id))
        for i in memb_dict['profiles']:
            list_of_members.append(
                {'full_name': (i['first_name'] + ' ' + i['last_name']), 'id': i['id'], 'photo_miniature': i['photo_50'],
                 'type': 'profile'})
        for i in memb_dict['groups']:
            list_of_members.append(
                {'full_name': i['name'], 'id': i['id'], 'photo_miniature': i['photo_50'], 'type': 'group',
                 'admin': 'false'})
        for i in memb_dict['items']:
            if ('is_admin' in i) and (i['is_admin'] == True):
                admin_list.append({'id': i['member_id']})
        return list_of_members
    def getonemember(self):
        return (random.choice(self.getMembers()))


class UserAnalyze():
    def __init__ (self, from_id, vk):
        self.vk=vk
        self.from_id=from_id

    def getuser(self,params):
        return (self.vk.users.get(user_ids=self.from_id, fields=params))


