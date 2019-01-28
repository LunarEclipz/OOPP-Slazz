import shelve

class Travel:
    def __init__(self):
        self.start = ''
        self.destination = ''
        self.fare = ''

def create_travel(username, travel):

    db = shelve.open('travel.db')
    userLog = username + 'travel'
    if username in db:
        temp = db[username]
        if travel in db[username]:
            verification = input('SIKE Y/N')
            if verification.lower() == 'y':
                for i in range(len(temp)):
                    if temp[i].title == travel.title:
                        temp.pop(i)
                        db[username] = temp
                    else:
                        continue
                temp.append(travel)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(travel)
                db[userLog] = temp2
            else:
                temp.append(travel)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(travel)
                db[userLog] = temp2
        else:
            temp.append(travel)
            db[username] = temp
            temp2 = db[userLog]
            temp2.append(travel)
            db[userLog] = temp2
    else:
        list1 = []
        list1.append(travel)
        db[username] = list1
        db[userLog] = list1
    db.close()
