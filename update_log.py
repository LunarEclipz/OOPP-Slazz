class Update():
    def __init__(self, amount, name):
        self.__name = name
        self.__amount = amount

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

class topup(Update):

    def __init__(self, amount, name='Bob', mode='topup', color='green'):
        super().__init__(amount, name)
        self.__mode = mode
        self.color = color

class payee(Update):

    def __init__(self, amount, name, mode='payee', color='red'):
        super().__init__(amount, name)
        self.__mode = mode
        self.color = color

p = topup(7)
print(p.get_name())
