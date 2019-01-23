class Finance:
    __budget = ''
    __expenditure = ''

    def __init__(self, expenditure, budget):
        self.__budget = budget
        self.__expenditure = expenditure

    def get_budget(self):
        return self.__budget

    def set_budget(self, budget):
        self.__budget = budget

    def get_expenditure(self):
        return self.__expenditure

    def set_expenditure(self, expenditure):
        self.__expenditure = expenditure


class Food(Finance):
    def __init__(self, expenditure, budget=0.2, name='Food'):
        super().__init__(expenditure, budget)
        self.__name = name

    def get_name(self):
        return self.__name


class Leisure(Finance):
    def __init__(self, expenditure, budget=0.4, name='Leisure'):
        super().__init__(expenditure, budget)
        self.__name = name

    def get_name(self):
        return self.__name


class Essentials(Finance):
    def __init__(self, expenditure, budget=0.3, name='Essentials'):
        super().__init__(expenditure, budget)
        self.__name = name

    def get_name(self):
        return self.__name


class Others(Finance):
    def __init__(self, expenditure, budget=0.1, name='Others'):
        super().__init__(expenditure, budget)
        self.__name = name

    def get_name(self):
        return self.__name


