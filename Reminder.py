class Reminder:

    reminders = []

    def __init__(self, date, notification, email):
        self.date = date
        self.notification = notification
        self.email = email

    def get_date(self):
        return self.date

    def get_notification(self):
        return self.notification

    def get_email(self):
        return self.email

    def set_date(self, date):
        self.date = date

    def set_notification(self, notification):
        self.notification = notification

    def set_email(self, email):
        self.email = email
