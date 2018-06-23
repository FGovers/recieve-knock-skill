from mycroft import MycroftSkill, intent_file_handler


class RecieveKnock(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('knock.recieve.intent')
    def handle_knock_recieve(self, message):
        self.speak_dialog('knock.recieve')
        
    @intent_file_handler('knock.who.intent').require('name')
    def handle_who(self,message):
        utterance=message.data.get('utterance')
        utterance += " who?"
        self.speak(utterance)


def create_skill():
    return RecieveKnock()

