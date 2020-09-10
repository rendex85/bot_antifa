class WallWorker():
    def __init__(self, peer_id, msg, vk):
        self.vk=vk
        self.peer_id=peer_id
        self.msg=msg
        self.public=""
        strtssyl = self.msg.find("vk.com/")
        if strtssyl != -1:
            endssyl=self.msg[strtssyl+len("vk.com/"):].find(' ')
            if endssyl ==-1:
                self.public=self.msg[strtssyl+len("vk.com/"):]
            else:
                self.public = self.msg[strtssyl + len("vk.com/"): endssyl]
        clown=vk.groups.getById(group_id=self.public, fields='counters')