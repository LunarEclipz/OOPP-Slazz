import shelve

def add_info(username, log):

    db = shelve.open('log.db')
    userLog = username + 'log'
    if username in db:
        temp = db[username]
        if log in db[username]:
            verification = input('Would you like to replace this log? Y/N')
            if verification.lower() == 'y':
                for i in range(len(temp)):
                    if temp[i].title == log.title:
                        temp.pop(i)
                        db[username] = temp
                    else:
                        continue
                temp.append(log)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(log)
                db[userLog] = temp2
            else:
                temp.append(log)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(log)
                db[userLog] = temp2
        else:
            temp.append(log)
            db[username] = temp
            temp2 = db[userLog]
            temp2.append(log)
            db[userLog] = temp2
    else:
        list1 = []
        list1.append(log)
        db[username] = list1
        db[userLog] = list1
    db.close()

def delete_info(username, log):

    db = shelve.open('log.db')


