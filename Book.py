import datetime as dt

now = dt.datetime.now()


class Book:

    renewCount = 0

    def __init__(self, title, genre, synopsis):
        self.__title = title
        self.__synopsis = synopsis
        self.__genre = genre
        self.__date_borrowed = 0
        self.set_date_borrowed()

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_synopsis(self):
        return self.__synopsis

    def get_date_borrowed(self):
        return self.__date_borrowed

    def set_title(self, title):
        self.__title = title

    def set_genre(self, genre):
        self.__genre = genre

    def set_synopsis(self, synopsis):
        self.__synopsis = synopsis

    def set_date_borrowed(self):
        self.__date_borrowed = now.strftime("%Y-%m-%d")

    def book_renewal(self):
        self.__date_borrowed = now.strftime("%Y-%m-%d")

    def __str__(self):
        s = "title is {}\n genre is {}\n date is {}".format(self.get_title(), self.get_genre(), self.get_date_borrowed())
        return s


