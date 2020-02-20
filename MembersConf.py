class MembersConf():
    memb_dict = dict()
    list_of_members=list()
    admin_list=list()

    def __init__(self, vk, peer_id):
        self.memb_dict = dict(vk.messages.getConversationMembers(peer_id=str(peer_id)))

        for i in self.memb_dict['profiles']:
            self.list_of_members.append(
                {'full_name': (i['first_name'] + ' ' + i['last_name']), 'id': i['id'], 'photo_miniature': i['photo_50'],
                 'type': 'profile'})
        for i in self.memb_dict['groups']:
            self.list_of_members.append(
                {'full_name': i['name'], 'id': i['id'], 'photo_miniature': i['photo_50'], 'type': 'group',
                 'admin': 'false'})

    def getonemember(self):
        listofmembers = list()


        return (listofmembers)
