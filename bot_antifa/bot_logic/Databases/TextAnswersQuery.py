from random import *

from bot_antifa.Databases.Models import *
from bot_antifa.WorkWith.WorkWithText import *


class WorkWithText:
    def __init__(self, peer_id, from_id, message, vk):
        self.peer_id = peer_id
        self.vk = vk
        self.message = message
        self.from_id = from_id
        self.text = TextAnswer(self.peer_id, self.vk)

    def answer(self):
        answer = []
        answcount = 0
        txt = TriggerAnsw
        query = txt.select(TriggerAnsw.trig_answ_id, Trigger.trigger_text, Answer.answer_text).join(Trigger).switch(
            TriggerAnsw).join(Answer)
        answers = query.dicts().execute()
        for row in answers:
            if self.message.lower().find(row['trigger_text'].lower()) != -1 and self.message.lower().find(
                    "!убрать") == -1:
                answcount += 1
                answer.append(row['answer_text'])
        if answcount > 0:
            self.text.sendmsg(random.choice(answer))

    def addToBase(self):
            trigger_txt = self.message[self.message.find("!добавить") + len("!добавить") + 1:self.message.find("|")]
            checkTrigger = Trigger.get_or_none(Trigger.trigger_text == trigger_txt)
            if checkTrigger == None:
                newTrigger = Trigger(trigger_text=trigger_txt)
                newTrigger.save()
                triggerId = newTrigger.trigger_id
            else:
                triggerId = checkTrigger.trigger_id
            answer_txt = self.message[self.message.find("|") + 1:]
            newAnswer = Answer(answer_text=answer_txt)
            newAnswer.save()
            answerId = newAnswer.answer_id
            TriggerAnsw.insert(trigger_link=triggerId, answer_link=answerId).execute()
            self.text.sendmsg("Условие успешно добавлено")

    def removeFromBase(self):

            delete_txt = self.message[self.message.find("!убрать") + len("!убрать") + 1:]
            query = TriggerAnsw.select(TriggerAnsw.trig_answ_id, Answer.answer_id).join(Trigger).switch(
                TriggerAnsw).join(Answer).where(Trigger.trigger_text == delete_txt)
            answ = query.dicts().execute()
            for row in answ:
                Answer.delete().where(Answer.answer_id == int(row['answer_id'])).execute()
            trigger = Trigger.get(Trigger.trigger_text == delete_txt)
            triggerName = trigger.trigger_text
            trigger.delete_instance()
            self.text.sendmsg("Условие '" + triggerName + "' успешно убрано")
