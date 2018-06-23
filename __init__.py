from mycroft import MycroftSkill, intent_file_handler


class RecieveKnock(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.handle_who=False

    @intent_file_handler('knock.recieve.intent')
    def handle_knock_recieve(self, message):
        response =self.get_response('who is there')
        response += " who?"
        response =self.get_response(response)
        self.speak_dialog("very_funny")
        time.sleep(12)
        
    def stop(self):
        pass

def create_skill():
    return RecieveKnock()

