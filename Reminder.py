class Reminder:

    reminders = []

    def __init__(self, date, notification, email):
        self.__date = date
        self.__notification = notification
        self.__email = email

    def get_date(self):
        return self.__date

    def get_notification(self):
        return self.__notification

    def get_email(self):
        return self.__email

    def set_date(self, date):
        self.__date = date

    def set_notification(self, notification):
        self.__notification = notification

    def set_email(self, email):
        self.__email = email
