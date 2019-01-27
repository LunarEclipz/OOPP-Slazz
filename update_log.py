class Update():
    def __init__(self, amount, name):
        self.__name = name
        self.__amount = amount

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

class topup(Update):

    def __init__(self, amount, name='Bob', mode='topup'):
        super().__init__(amount, name)
        self.__mode = mode

class payee(Update):

    def __init__(self, amount, name, mode='payee'):
        super().__init__(amount, name)
        self.__mode = mode

p = topup(7)
print(p.get_name())
