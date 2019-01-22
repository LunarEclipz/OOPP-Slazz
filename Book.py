import datetime as dt

now = dt.datetime.now()


class Book:

    renewCount = 0

    def __init__(self):
        self.title = ''
        self.synopsis = ''
        self.genre = ''
        self.date_borrowed = 0
        self.due_date = 0
        self.reminder = 0

    def get_title(self):
        return self.title

    def get_genre(self):
        return self.genre

    def get_synopsis(self):
        return self.synopsis

    def get_date_borrowed(self):
        return self.date_borrowed

    def get_due_date(self):
        return self.due_date

    def get_reminder(self):
        return self.reminder

    def set_title(self, title):
        self.title = title

    def set_genre(self, genre):
        self.genre = genre

    def set_synopsis(self, synopsis):
        self.synopsis = synopsis

    def set_date_borrowed(self, date_borrowed):
        self.date_borrowed = date_borrowed

    def set_due_date(self, date_borrowed):
        if isinstance(date_borrowed, str):
            datetime_object = dt.datetime.strptime(date_borrowed, '%Y-%m-%d').date()
            self.due_date = datetime_object + dt.timedelta(days=14)
        else:
            self.due_date = date_borrowed + dt.timedelta(days=14)

    def book_renewal(self):
        self.due_date += dt.timedelta(days=14)
        self.__class__.renewCount += 1

    def set_reminder(self, reminder):
        self.reminder = reminder

    def __str__(self):
        s = "title is {}\n genre is {}\n date is {}".format(self.get_title(), self.get_genre(), self.get_date_borrowed())
        return s


def today_date():
    return now.strftime("%Y-%m-%d")


class due_date:

    def __init__(self, date_borrowed):
        self.date_borrowed = date_borrowed
        self.dueDate = 0
        self.set_due_date(date_borrowed)

    def get_due_date(self):
        return self.dueDate

    def set_due_date(self, borrowdate):
        self.dueDate = borrowdate + dt.timedelta(days=14)
        return self.dueDate

    def __str__(self):
        s = "due date is {}".format(self.get_due_date())
        return s

