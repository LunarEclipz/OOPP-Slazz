import shelve


def add_activity(username, activity):

    db = shelve.open('activity.db')
    userLog = username + 'activity'
    if username in db:
        temp = db[username]
        if activity in db[username]:
            verification = input('Would you like to replace this activity? Y/N')
            if verification.lower() == 'y':
                for i in range(len(temp)):
                    if temp[i].title == activity.title:
                        temp.pop(i)
                        db[username] = temp
                    else:
                        continue
                temp.append(activity)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(activity)
                db[userLog] = temp2
            else:
                temp.append(activity)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(activity)
                db[userLog] = temp2
        else:
            temp.append(activity)
            db[username] = temp
            temp2 = db[userLog]
            temp2.append(activity)
            db[userLog] = temp2
    else:
        list1 = []
        list1.append(activity)
        db[username] = list1
        db[userLog] = list1
    db.close()


def remove_activity(username, activity_name):
    db = shelve.open('activity.db', writeback=True)
    loopcount = 0
    try:
        temp = db[username]
        for i in temp:
            if i.name == activity_name:
                temp.pop(loopcount)
                db[username] = temp
            else:
                loopcount += 1
                pass
    except KeyError:
        print('There is no user named', username, '.')
    else:
        print(activity_name, ' has been removed.')
    db.close()


