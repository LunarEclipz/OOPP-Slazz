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


def save_budget(form):
    s = shelve.open('test_shelf.db')
    try:
        s['Budget'] = {'Food and Beverage': form.f_budget.data, 'Essentials': form.e_budget.data, 'Leisure': form.l_budget.data, 'Others': form.o_budget.data}
    finally:
        s.close()

