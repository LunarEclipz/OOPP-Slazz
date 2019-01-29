
import shelve
from datetime import datetime

class Message:
    def __init__(self):
        self.sender = 'system'
        self.receiver = ''
        self.message = ''
        self.created = str(datetime.utcnow())
        self.id = self.created

    def get_id(self):
        return self.sender


messages = shelve.open('messages')


def send_message(receiver, message):
    m = Message()
    m.receiver = receiver
    m.message = message
    messages[m.id] = m

def get_message(receiver):
    l = []
    klist = list(messages.keys())
    for id in klist:
        message = messages[id]
        if message.receiver == receiver:
            l.append(message)
    return l

def send_transferred_message(receiver, amount):
    message = '     ' + str(amount) + ' has been transferred to your account    '
    send_message(receiver, message)

def send_spent_message(receiver, amount):
    spentMessage = 'You have spent      ' + str(amount) + ' from your account    '
    send_message(receiver, spentMessage)


