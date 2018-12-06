from flask import Flask, render_template
from Library import Book, Due_date, Reminder

app = Flask(__name__)


@app.route('/')
def libraryhome():
    return render_template("Library.html")


@app.route('/Reminders.html')
def reminders():
    bk = ['Hell', 'Meow']
    books = Book.Book
    reminder = Reminder.Reminder
    return render_template("Reminders.html", books=books, reminder=reminder, bk=bk)


@app.route('/Payment.html')
def payment():
    duedate = Due_date.due_date
    return render_template("Payment.html", duedate=duedate)


@app.route('/RecommendedBooks.html')
def recBooks():
    return render_template("RecommendedBooks.html")


if __name__ == '__main__':
    app.run()
