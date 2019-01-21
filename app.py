from flask import Flask, render_template, request
import Book
import Reminder
import BookDatabase
import shelve
import datetime

app = Flask(__name__)


@app.route('/')
def libraryhome():
    return render_template("Library.html")


@app.route('/Reminders')
def reminders():
    bk = ['Dante', 'Locker B']
    books = Book.Book
    reminder = Reminder.Reminder
    bdb = shelve.open('bookLoans.db')
    return render_template("Reminders.html", books=books, reminder=reminder, bk=bk, bdb=bdb)


@app.route('/Payment')
def payment():
    return render_template("Payment.html")


@app.route('/RecommendedBooks')
def recBooks():
    return render_template("RecommendedBooks.html")


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
    return render_template('BorrowedBooks.html', book=book, genres=genres, db=db)


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


@app.route('/ReminderSubmit')
def reminderSubmit():
    result = request.form
    book = result['books']
    remindDate = result['RemindDate']
    db = BookDatabase
    remindDate2 = datetime.datetime.strftime(remindDate, '%Y-%m-%d')
    reminder = Reminder.Reminder('Bob', remindDate2)
    reminder.set_book('Bob', book)

    return render_template('ReminderSubmit.html', db=db)


if __name__ == '__main__':
    app.run(debug=True)
