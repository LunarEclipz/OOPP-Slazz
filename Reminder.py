import datetime as dt
import shelve
import Book


class Reminder(Book.Book):

    reminders = []
    bookcount = 0

    def __init__(self, username, date):
        super().__init__()
        self.username = username
        # need to use self.set_book to set self.bookname
        self.bookname = ''
        self.date = date
        self.notification = ''
        self.__email = ''

    def set_book(self, username, bookname):
        db = shelve.open('BookDatabase.db')
        if username in db.keys():
            for i in db[username]:
                if i.title == bookname:
                    self.bookname = bookname
                    self.__class__.bookcount += 1
                else:
                    continue
        else:
            return 'There is no user named', username
        db.close()

    def get_date(self):
        return self.date

    def get_notification(self):
        return self.notification

    def get_email(self):
        return self.__email

    def set_date(self, date):
        self.date = date

    def set_notification(self, notification):
        self.notification = notification

    def set_email(self, email):
        self.__email = email


def days_between(d1, d2):
    shelve.open('bookLoans.db')
    d1 = dt.datetime.strptime(d1, "%Y-%m-%d")
    d2 = dt.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
