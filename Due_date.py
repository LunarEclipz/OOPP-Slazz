
import datetime as dt


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


