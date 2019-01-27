import shelve
from datetime import datetime
from threading import Timer


x = datetime.today()
y = x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t = y-x

secs = delta_t.seconds+1


# adds a certain amount of money to fine database once per day depending on how many books are overdue
# Type 'username' in fine_add parameters
def fine_add():
    print("hello world")
    todayDate = datetime.now().strftime("%Y-%m-%d")
    bdb = shelve.open('bookLoans.db')
    fdb = shelve.open('bookFines', writeback=True)
    # replace 'Bob's with username
    for i in bdb['Bob']:
        if i.due_date == todayDate:
            if 'Bob' in fdb:
                fdb['Bob'] += 0.2
            else:
                fdb['Bob'] = 0.2
        else:
            pass


t = Timer(secs, fine_add)
t.start()
