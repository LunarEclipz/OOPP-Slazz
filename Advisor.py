class Finance:
    __budget = ''
    __expenditure = ''

    def __init__(self, budget, expenditure):
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


class Departments(Finance):
    __individual_savings = ''
    __name = ''

    def __init__(self, name, budget, expenditure, indi):
        Finance.__init__(self, budget, expenditure)
        self.__name = name
        self.__individual_savings = indi

    def get_indi(self):
        return self.__individual_savings
    
    def set_indi(self, indi):
        self.__individual_savings = indi

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


class User(Finance):
    __total_savings = ''

    def __init__(self, budget, expenditure, total):
        Finance.__init__(self, budget, expenditure)
        self.__total = total

    def get_total(self):
        return self.__total

    def set_total(self, total):
        self.__total = total
