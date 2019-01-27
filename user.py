import shelve

class User:
    def __init__(self):
        self.id = ''
        self.email = ''
        self.password = ''

users = shelve.open('user')

def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]

def get_users():
    user_list = []
    klist = list(users.keys())
    for key in klist:
        user_list.append(users[key])
    return user_list


def init_users():
    clear_user()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i))

def get_user(id, password):
    if id in users:
        user = users[id]
        if  user.password == password:
            return user
    return None

def create_user(id, email, password):
    u = User()
    u.id = id
    u.email = email
    u.password = password
    users[id] = u







