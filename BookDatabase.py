import shelve


# username is the key for all book loans for that user
# parameter book is an instance of the Book class
def storeBook(username, book):

    db = shelve.open('bookLoans.db')
    userLog = username + 'LOGBOOK'
    if username in db:
        temp = db[username]
        if book in db[username]:
            verification = input('Would you like to replace the existing copy of this book? Y/N')
            if verification.lower() == 'y':
                for i in range(len(temp)):
                    if temp[i].title == book.title:
                        temp.pop(i)
                        db[username] = temp
                    else:
                        continue
                temp.append(book)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(book)
                db[userLog] = temp2
            else:
                temp.append(book)
                db[username] = temp
                temp2 = db[userLog]
                temp2.append(book)
                db[userLog] = temp2
        else:
            temp.append(book)
            db[username] = temp
            temp2 = db[userLog]
            temp2.append(book)
            db[userLog] = temp2
    else:
        list1 = []
        list1.append(book)
        db[username] = list1
        db[userLog] = list1
    db.close()


# gets a book instance value from a user key
def extractBook(username, bookname):
    db = shelve.open('bookLoans.db')
    for i in range(len(db[username])):
        if db[username][i].title == bookname:
            return db[username][i]
        else:
            pass
    db.close()


# deletes a user from the bookLoans database
def deleteUser(username):
    db = shelve.open('bookLoans.db')
    del db[username]
    db.close()


# deletes a book from a user key
def deleteBook(username, bookname):
    db = shelve.open('bookLoans.db', writeback=True)
    loopcount = 0
    try:
        temp = db[username]
        for i in temp:
            if i.title == bookname:
                temp.pop(loopcount)
                db[username] = temp
            else:
                loopcount += 1
                pass
    except KeyError:
        print('There is no user named', username, '.')
    else:
        print('There is no book named', bookname, '.')
    db.close()


def renewBook(username, bookname):
    db = shelve.open('bookLoans.db', writeback=True)
    for i in db[username]:
        if i.title == bookname:
            i.book_renewal()
        else:
            pass
    db.close()


# prints all book titles for a user
def showBookTitles(username):
    db = shelve.open('bookLoans.db')
    for i in range(len(db[username])):
            print(db[username][i].title, db[username][i].date_borrowed)
    db.close()


# reminder is an instance of the class Reminder
def store_reminder(username, reminder, bookname):
    db = shelve.open('bookLoans.db', writeback=True)
    for i in db[username]:
        if i.title == bookname:
            i.reminder = reminder
        else:
            pass
    db.close()

