import shelve


s = shelve.open('test_shelf.db')
try:
    activity = s['Activity']
    save = s['Save']
    spend = s['Spend']
    budget = s['Budget']
    account = s['Account']
finally:
    s.close()


def get_account():
    return account


def get_save():
    return save


def get_spend():
    return spend


def get_activity():
    return activity


def get_budget():
    return budget


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


def get_advise(budget, expenditure):
    if 0 <= budget and budget < 1:
        account = get_account()['Total_Monthly_Allowance']
        amount = budget*account
        value = amount - expenditure
    else:
        value = budget - expenditure
    return value


spending_data = get_spend()
budget_data = get_budget()
account_data = get_account()


def create_food():
    if budget_data['Food and Beverage'] is '':
        food = Food(account_data['Spent_on_Food_and_Beverage'])
    else:
        food = Food(account_data['Spent_on_Food_and_Beverage'], budget_data['Food and Beverage'])
    return food


def create_leisure():
    if budget_data['Food and Beverage'] is '':
        leisure = Leisure(account_data['Spent_on_Leisure'])
    else:
        leisure = Leisure(account_data['Spent_on_Leisure'], budget_data['Leisure'])
    return leisure


def create_essen():
    if budget_data['Food and Beverage'] is '':
        essentials = Essentials(account_data['Spent_on_Essentials'])
    else:
        essentials = Essentials(account_data['Spent_on_Essentials'], budget_data['Essentials'])
    return essentials


def create_others():
    if budget_data['Food and Beverage'] is '':
        others = Others(account_data['Spent_on_Others'])
    else:
        others = Others(account_data['Spent_on_Others'], budget_data['Others'])
    return others


saved_total = account_data['Total_Monthly_Allowance'] - account_data['Spent_on_Food_and_Beverage']\
                  - account_data['Spent_on_Leisure'] - account_data['Spent_on_Essentials'] - account_data['Spent_on_Others']
f_a = get_advise(create_food().get_budget(), create_food().get_expenditure())
l_a = get_advise(create_leisure().get_budget(), create_leisure().get_expenditure())
e_a = get_advise(create_essen().get_budget(), create_essen().get_expenditure())
o_a = get_advise(create_others().get_budget(), create_others().get_expenditure())

food_budget = create_food().get_budget()
essen_budget = create_essen().get_budget()
leisure_budget = create_leisure().get_budget()
others_budget = create_others().get_budget()
