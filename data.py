import shelve


def update_budget(username, budget):

    db = shelve.open('budget.db')
    userLog = username + 'budget'
    if username in db:
        temp = db[username]
        if budget in db[username]:
            verification = input('Would you like to replace this activity? Y/N')
            if verification.lower() == 'y':
                for i in range(len(temp)):
                    if temp[i].title == budget.title:
                        temp.pop(i)
                        db[username] = temp
                    else:
                        continue
                temp.append(budget)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(budget)
                db[userLog] = temp2
            else:
                temp.append(budget)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(budget)
                db[userLog] = temp2
        else:
            temp.append(budget)
            db[username] = temp
            temp2 = db[userLog]
            temp2.append(budget)
            db[userLog] = temp2
    else:
        list1 = []
        list1.append(budget)
        db[username] = list1
        db[userLog] = list1
    db.close()


def clear_budgets(username):
    db = shelve.open('budget.db')
    del db[username]
    db.close()


class Budget:

    def __init__(self, food_b, leisure_b, essen_b, others_b, food_e, leisure_e, essen_e, others_e, total):
        self.food_b = food_b
        self.leisure_b = leisure_b
        self.essen_b = essen_b
        self.others_b = others_b
        self.food_e = food_e
        self.leisure_e = leisure_e
        self.essen_e = essen_e
        self.others_e = others_e
        self.total = total

    def get_foodb(self):
        return self.food_b

    def get_foode(self):
        return self.food_e

    def get_leisureb(self):
        return self.leisure_b

    def get_leisuree(self):
        return self.leisure_e

    def get_othersb(self):
        return self.food_b

    def get_otherse(self):
        return self.others_e

    def get_essenb(self):
        return self.essen_b

    def get_essene(self):
        return self.essen_e

    def get_total(self):
        return self.total


class Default(Budget):

    def __init__(self, food_b=0.2, leisure_b=0.4, essen_b=0.3, others_b=0.1, food_e=50, leisure_e=30, essen_e=25, \
                 others_e=10, total=400, type='Default', Oct='30', Nov='20', Dec='10', Jan='285', f_color='', f_advise=''\
                 , e_color='', e_advise='', l_color='', l_advise='', o_color='', o_advise=''):
        super().__init__(food_b, leisure_b, essen_b, others_b, food_e, leisure_e, essen_e, others_e, total)
        self.type = type
        self.Oct = Oct
        self.Nov = Nov
        self.Dec = Dec
        self.Jan = Jan
        self.f_color = f_color
        self.f_advise = f_advise
        self.l_color = l_color
        self.l_advise = l_advise
        self.o_color = o_color
        self.o_advise = o_advise
        self.e_color = e_color
        self.e_advise = e_advise



    def get_type(self):
        return self.type


class self_Settings(Budget):

    def __init__(self, food_b='', leisure_b='', essen_b='', others_b='', food_e=50, leisure_e=30, essen_e=25,\
                 others_e=10, total=400, type='Self Settings', Oct='30', Nov='20', Dec='10', Jan='285',\
                 f_color='', f_advise='', e_color='', e_advise='', l_color='', l_advise='', o_color='', o_advise=''):
        super().__init__(food_b, leisure_b, essen_b, others_b, food_e, leisure_e, essen_e, others_e, total)
        self.type = type
        self.Oct = Oct
        self.Nov = Nov
        self.Dec = Dec
        self.Jan = Jan
        self.f_color = f_color
        self.f_advise = f_advise
        self.l_color = l_color
        self.l_advise = l_advise
        self.o_color = o_color
        self.o_advise = o_advise
        self.e_color = e_color
        self.e_advise = e_advise

    def get_type(self):
        return self.type


def get_advise(budget, expenditure):
    budget = float(budget)
    expenditure = float(expenditure)
    if 0 <= budget and budget < 1:
        account = 400
        amount = budget*account
        value = amount - expenditure
    else:
        value = budget - expenditure
    return value


def get_colorvise(f_c, f_a, e_c, e_a, o_c, o_a, l_c, l_a):
    if f_a < 0:
        f_c = 'red'
        f_a = 'You lost $' + str(f_a) + ' for food and beverages. Save More!'
    else:
        f_c = 'green'
        f_a = 'You gained $' + str(f_a) + ' for food and beverages. You Saved Well!'
    if e_a < 0:
        e_c = 'red'
        e_a = 'You lost $' + str(e_a) + ' for essentials. Save More!'
    else:
        e_c = 'green'
        e_a = 'You gained $' + str(e_a) + ' for essentials. You Saved Well!'
    if o_a < 0:
        o_c = 'red'
        o_a = 'You lost $' + str(o_a) + ' for others. Save More!'
    else:
        o_c = 'green'
        o_a = 'You gained $' + str(o_a) + ' for others. You Saved Well!'
    if l_a < 0:
        l_c = 'red'
        l_a = 'You lost $' + str(l_a) + ' for leisure. Save More!'
    else:
        l_c = 'green'
        l_a = 'You gained $' + str(l_a) + ' for leisure. You Saved Well!'
    return f_c, f_a, e_c, e_a, o_c, o_a, l_c, l_a


# def update_Savings(username, Savings):
#     db = shelve.open('budget.db')
#     userLog = username + 'Savings'
#     if username in db:
#         temp = db[username]
#         if Savings in db[username]:
#             verification = input('Would you like to replace this activity? Y/N')
#             if verification.lower() == 'y':
#                 for i in range(len(temp)):
#                     if temp[i].title == Savings.title:
#                         temp.pop(i)
#                         db[username] = temp
#                     else:
#                         continue
#                 temp.append(Savings)
#                 db[username] = temp
#                 temp2 = db[userLog]
#                 temp2.append(Savings)
#                 db[userLog] = temp2
#             else:
#                 temp.append(Savings)
#                 db[username] = temp
#                 temp2 = db[userLog]
#                 temp2.append(Savings)
#                 db[userLog] = temp2
#         else:
#             temp.append(Savings)
#             db[username] = temp
#             temp2 = db[userLog]
#             temp2.append(Savings)
#             db[userLog] = temp2
#     else:
#         list1 = []
#         list1.append(Savings)
#         db[username] = list1
#         db[userLog] = list1
#     db.close()
#
#
# class Months:
#     def __init__(self, name, amount, anno):
#         self.amount = name
#         self.anno = anno
#         self.name = amount
#
#     def get_name(self):
#         return self.name
#
#     def get_amount(self):
#         return self.amount
#
#     def get_anno(self):
#         return self.anno
#
#
# class Oct(Months):
#     def __init__(self, amount=30, anno='Oct', name='October'):
#         super().__init__(amount, anno, name)
#
#
# class Nov(Months):
#     def __init__(self, amount=10, anno='Nov', name='November'):
#         super().__init__(amount, anno, name)
#
#
# class Dec(Months):
#     def __init__(self, amount=20, anno='Dec', name='December'):
#         super().__init__(amount, anno, name)
#
#
# class Jan(Months):
#     def __init__(self, amount=50, anno='Jan', name='January'):
#         super().__init__(amount, anno, name)
#
#
# o = Oct()
# n = Nov()
# d = Dec()
# j = Jan()
#
# update_Savings('Bob', o)
