from flask import Flask, render_template, request
import Book
import Reminder
import BookDatabase
import shelve
import datetime

# replace all 'Bob's with username
app = Flask(__name__)


@app.route('/')
def libraryhome():
    return render_template("Library.html")


@app.route('/Reminders')
def reminders():
    books = Book
    reminder = Reminder.Reminder
    bdb = shelve.open('bookLoans.db')
    return render_template("Reminders.html", books=books, reminder=reminder, bdb=bdb)


@app.route('/Payment')
def payment():
    today = datetime.datetime.strptime(Book.today_date(), '%Y-%m-%d').date()
    bdb = shelve.open('bookLoans.db')
    return render_template("Payment.html", today=today, bdb=bdb)


@app.route('/RecommendedBooks')
def recBooks():
    bdb = shelve.open('bookLoans.db')
    book1Gen = ''
    rl = []
    if 'BobLOGBOOK' in bdb:
        book1Gen = bdb['BobLOGBOOK'][-1].genre
        for i in range(len(bdb['BobLOGBOOK'])-1, -1, -1):
            rl.append(bdb['BobLOGBOOK'][i].title)
    else:
        pass
    rdb = shelve.open('bookRecommendations')
    return render_template("RecommendedBooks.html", bdb=bdb, rdb=rdb, book1Gen=book1Gen, rl=rl)


@app.route('/BooksOnLoan')
def loaned():
    book = Book
    genres = ['Adventure', 'Art', 'Astrology', 'Autobiography', 'Biography', 'Biology', 'Chemistry',
              "Children's Literature", 'Comic Book', 'Coming-of-age', 'Cookbook', 'Crime', 'Diary', 'Drama',
              'Educational', 'Encyclopedia', 'Fairytale', 'Food', 'Geology', 'Guide', 'Health', 'History', 'Horror',
              'IT', 'Math', 'Memoir', 'Mystery', 'Non-Fiction', 'Paranormal', 'Physics', 'Physiology',
              'Poetry', 'Political Thriller', 'Prayer', 'Psychology', 'Religion', 'Review', 'Romance', 'Satire',
              'Sci-fi', 'Self Help', 'Suspense', 'Textbook', 'Thriller', 'Travel', 'Young Adult']
    db = BookDatabase
    bdb = shelve.open('bookLoans.db')
    return render_template('BorrowedBooks.html', book=book, bdb=bdb, genres=genres, db=db)


@app.route('/BookSubmitSuccess', methods=['POST', 'GET'])
def booksubmit():
    if request.method == 'POST':
        result = request.form
        bookname = result['bookTitle']
        genre = result['genre']
        loandate = result['loanDate']
        book = Book.Book()
        book.title = bookname
        book.genre = genre
        book.date_borrowed = loandate
        book.set_due_date(book.date_borrowed)
        db = BookDatabase
        db.storeBook('Bob', book)
        bdb = shelve.open('bookLoans.db')
        return render_template("BookSubmit.html", result=result, db=db, bdb=bdb)


@app.route('/ReminderSubmit', methods=['GET', 'POST'])
def reminderSubmit():
    if request.method == 'POST':
        result = request.form
        bookname = result['books']
        remindDate = result['RemindDate']
        db = BookDatabase
        remindDate2 = datetime.datetime.strptime(remindDate, '%Y-%m-%d').date()
        # replace all 'Bob's with username
        reminder = Reminder.Reminder('Bob', remindDate2)
        reminder.set_book('Bob', bookname)
        db.store_reminder('Bob', reminder, bookname)
        return render_template('ReminderSubmit.html', result=result, db=db)


@app.route('/RenewSubmit', methods=['GET', 'POST'])
def renewSubmit():
    if request.method == 'POST':
        result = request.form
        book = result['renewBooks']
        db = BookDatabase
        db.renewBook('Bob', book)
        bdb = shelve.open('bookLoans.db')
        return render_template('RenewSubmit.html', result=result, db=db, bdb=bdb)


@app.route('/ReturnSubmit', methods=['GET', 'POST'])
def returnSubmit():
    if request.method == 'POST':
        result = request.form
        book = result['returnBook']
        db = BookDatabase
        db.deleteBook('Bob', book)
        bdb = shelve.open('bookLoans.db')
        return render_template('ReturnSubmit.html', result=result, db=db, bdb=bdb)


if __name__ == '__main__':
    app.run(debug=True)
