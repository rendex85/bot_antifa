from EventHandler.HandlerKernel import BaseHandler
from WorkWith.WorkWithText import TextAnswer


class WhoHandler(BaseHandler):
    trigger_in = ["!кто", ]

    def preHandler(self):
        self.message_data.message = TextAnswer(self.obj, self.vk).answer_who()
