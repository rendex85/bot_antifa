from random import *

from Databases.Models import *
from TextAnswer import *


class WorkWithText:
    def __init__(self, peer_id, from_id, message, vk):
        self.peer_id = peer_id
        self.vk = vk
        self.message = message
        self.from_id=from_id
        self.text = TextAnswer(self.peer_id, self.vk)

    def answer(self):
        answer = []
        answcount = 0
        txt = TextAnsw
        query = txt.select(TextAnsw.answer_id, Trigger.trigger_text, Answer.answer_text).join(Trigger).switch(
            TextAnsw).join(Answer)
        answers = query.dicts().execute()
        for row in answers:
            if self.message.lower().find(row['trigger_text'].lower()) != -1 and self.message.lower().find("!убрать") == -1:
                answcount += 1
                answer.append(row['answer_text'])
        if answcount > 0:
            self.text.sendmsg(random.choice(answer))

    def addToBase(self):
        if (self.message.lower().find("!добавить") != -1 and (self.from_id == 232282950 or self.from_id == 204181697)):
            trigger_txt = self.message[self.message.find("!добавить") + len("!добавить") + 1:self.message.find("|")]
            print(trigger_txt)
            newTrigger = Trigger(trigger_text=trigger_txt)
            newTrigger.save()
            triggerId = newTrigger.trigger_id
            answer_txt = self.message[self.message.find("|") + 1:]
            print(answer_txt)
            newAnswer = Answer(answer_text=answer_txt)
            newAnswer.save()
            answerId = newAnswer.answer_id
            TextAnsw.insert(trigger_link=triggerId, answer_link=answerId).execute()
            self.text.sendmsg("Новое условие успешно добавлено")
    def removeFromBase(self):
        if (self.message.lower().find("!убрать") != -1 and (self.peer_id == 232282950 or self.peer_id == 204181697)):
            delete_txt = self.message[self.message.find("!убрать") + len("!убрать") + 1:]
            trigger=Trigger.get(Trigger.trigger_text==delete_txt)
            triggerName=trigger.trigger_text
            trigger.delete_instance()
            self.text.sendmsg("Условие '"+triggerName+"' успешно убрано")






