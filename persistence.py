import shelve


class feedbackUser:
    def __init__(self):
        self.id = ''
        self.email = ''
        self.message = ''


feedback = shelve.open('feedback')


def create_contactUs(contactUs, id, email, message):
    feedback[contactUs.id] = contactUs
    feedback[contactUs.email] = contactUs
    feedback[contactUs.message] = contactUs

