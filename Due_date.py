
import datetime as dt

date_borrowed = dt.datetime.now().strftime("%Y-%m-%d")
date_borrowed2 = dt.datetime.strptime(date_borrowed, "%Y-%m-%d")


class due_date:

    def __init__(self):
        self.__date_borrowed = date_borrowed2
        self.__dueDate = 0
        self.set_due_date()

    def get_due_date(self):
        return self.__dueDate

    def set_due_date(self, borrowdate):
        self.__dueDate = borrowdate + dt.timedelta(days=14)
        return self.__dueDate

    def __str__(self):
        s = "due date is {}".format(self.get_due_date())
        return s


