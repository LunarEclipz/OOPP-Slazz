import datetime as dt

now = dt.datetime.now()


class Book:

    renewCount = 0

    def __init__(self, title, genre, synopsis):
        self.title = title
        self.synopsis = synopsis
        self.genre = genre
        self.date_borrowed = 0
        self.set_date_borrowed()

    def get_title(self):
        return self.title

    def get_genre(self):
        return self.genre

    def get_synopsis(self):
        return self.synopsis

    def get_date_borrowed(self):
        return self.date_borrowed

    def set_title(self, title):
        self.title = title

    def set_genre(self, genre):
        self.genre = genre

    def set_synopsis(self, synopsis):
        self.synopsis = synopsis

    def set_date_borrowed(self):
        self.date_borrowed = now.strftime("%Y-%m-%d")

    def book_renewal(self):
        self.date_borrowed = now.strftime("%Y-%m-%d")

    def __str__(self):
        s = "title is {}\n genre is {}\n date is {}".format(self.get_title(), self.get_genre(), self.get_date_borrowed())
        return s


def today_date():
    return now.strftime("%Y-%m-%d")


