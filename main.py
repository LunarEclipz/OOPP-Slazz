from flask import *
from forms import *
import data
import activity
from user import *
import Book
from functools import wraps
import activities
from message import *
from persistence import *
import datetime
import Reminder
import BookDatabase
import payment_data
import update_log
import traveldata

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config.from_mapping(
    SECRET_KEY='dev'
)


@app.route('/')
def home():
    return render_template('home.html')


#User Login
@app.route('/login',  methods=('GET', 'POST'))
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST':
        user = get_user(login_form.id.data, login_form.password.data)
        if user is None:
            error = 'Incorrect username and/or password'
        else:
            session['logged_in'] = True
            session['username'] = user.id

            flash('You are now logged in','success')
            return redirect(url_for('profile'))

        flash(error)
    return render_template('login.html', form=login_form)


#Register Account
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        id = form.id.data
        email = form.email.data
        password = form.password.data
        create_user(id, email, password)
        flash('You are now registered and can log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


#Check if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


#Logout
@app.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for('login'))


#user settings part(Lousia's Part)
@app.route("/profile")
def profile():
    name = session['username']
    user = retrieve_user(name)
    return render_template('profile.html', user = user)


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['fullname']
        nric = request.form['nric']
        email = request.form['email']
        password = request.form['newpass']
        user = User()
        user.id = username
        user.name = name
        user.nric = nric
        user.email = email
        user.password = password
        # store user object in persistence
        update_user(user)
        return render_template('success.html')


@app.route('/balance')
def balance():
    return render_template('balance.html')


@app.route('/message', methods=['GET'])
def message():
    name = session['username']
    messages = get_message(name)
    return render_template('message.html', messages = messages)


@app.route('/contactUs', methods=["GET", "POST"])
def contactUs():
    if request.method == 'POST':
        id = request.form.get('id')
        email = request.form.get('email')
        message = request.form.get('message')

        contactUs = feedbackUser()
        contactUs.id = id
        contactUs.email = email
        contactUs.message = message

        create_contactUs(contactUs, id, email, message)
        return render_template('contactUs.html')
    else:
        return render_template('contactUs.html')


@app.route('/testmessage', methods=["GET", "POST"])
def test_message():
    send_transferred_message('louisa', 500)
    send_transferred_message('louisa', 100)
    return 'created test messages to louisa'

# Main Pay Tab
@app.route('/paymain')
def paymain():
    return render_template('pay_main.html', title='Pay Main')


# Pay Tab
@app.route('/pay')
def pay():
    db = payment_data
    bdb = shelve.open('log.db')
    return render_template('pay.html', title='Pay', db=db, bdb=bdb)


# Top-up Tab
@app.route('/topup')
def topup():
    db = payment_data
    bdb = shelve.open('log.db')
    return render_template("top_up.html", title="Top-Up", db=db, bdb=bdb)


# Transaction Tab
@app.route('/transaction', methods=['POST', 'GET'])
def transactions():
    db = payment_data
    bdb = shelve.open('log.db')
    try:
        if request.method == 'POST':
            result = request.form
            amount = result['amount']
            try:
                name = result['name']
                p = update_log.Update(name, amount)
                p.amount = amount
                p.name = name
                p.color = "red"
                send_spent_message(session['username'], p.amount)
            except:
                p = update_log.topup(amount)
                p.amount = amount
                p.color = "green"
                p.name = p.get_name()
                send_transferred_message(session['username'], p.amount)
            db = payment_data
            db.add_info('Bob', p)
            bdb = shelve.open('log.db')
            return render_template("transactions.html", title="Transactions", result=result, db=db, bdb=bdb)
    except:
        db = payment_data
        bdb = shelve.open('log.db')
    return render_template("transactions.html", title="Transactions", db=db, bdb=bdb)


@app.route('/Finance')
def Financehome():
    return render_template("Finance_final.html", title='Finance')


@app.route('/Survey', methods=['GET', 'POST'])
def Survey():
    form = SurveyForm()
    return render_template("Survey.html", title='Survey', form=form)


@app.route('/Savings')
def Savings():
    db = data
    bdb = shelve.open('budget.db')
    return render_template("Savings.html", title='Savings',db=db, bdb=bdb)


@app.route('/Spending')
def Spending():
    db = data
    bdb = shelve.open('budget.db')
    return render_template("Spending.html", title='Spending',db=db, bdb=bdb)


@app.route('/Advisor', methods=['POST', 'GET'])
def Advisor():
    db = data
    bdb = shelve.open('budget.db')
    db.clear_budgets(session['username'])
    if request.method == 'POST':
        result = request.form
        food_b = result['food_b']
        essen_b = result['essen_b']
        leisure_b = result['leisure_b']
        others_b = result['others_b']
        a = data.self_Settings()
        a.food_b = food_b
        a.leisure_b = leisure_b
        a.others_b = others_b
        a.essen_b = essen_b
        db = data
        db.update_budget(session['username'], a)
        bdb = shelve.open('budget.db')
        f_a = db.get_advise(a.food_b, a.food_e)
        l_a = db.get_advise(a.leisure_b, a.leisure_e)
        e_a = db.get_advise(a.essen_b, a.essen_e)
        o_a = db.get_advise(a.others_b, a.others_e)
        db.clear_budgets(session['username'])
        a = data.self_Settings()
        a.food_b = food_b
        a.leisure_b = leisure_b
        a.others_b = others_b
        a.essen_b = essen_b
        colorvise = db.get_colorvise('', f_a, '', e_a, '', o_a, '', l_a)
        a.f_color = colorvise[0]
        a.f_advise = colorvise[1]
        a.e_color = colorvise[2]
        a.e_advise = colorvise[3]
        a.o_color = colorvise[4]
        a.o_advise = colorvise[5]
        a.l_color = colorvise[6]
        a.l_advise = colorvise[7]
        db.update_budget(session['username'], a)
        bdb = shelve.open('budget.db')
        saved_total = a.total - a.food_e - a.others_e - a.essen_e - a.leisure_e
        return render_template("Advisor.html", title='Advisor', result=result, db=db, bdb=bdb, saved_total=saved_total)
    else:
        a = data.Default()
        db = data
        db.update_budget(session['username'], a)
        bdb = shelve.open('budget.db')
        f_a = db.get_advise(a.food_b, a.food_e)
        l_a = db.get_advise(a.leisure_b, a.leisure_e)
        e_a = db.get_advise(a.essen_b, a.essen_e)
        o_a = db.get_advise(a.others_b, a.others_e)
        db.clear_budgets(session['username'])
        colorvise = db.get_colorvise('', f_a, '', e_a, '', o_a, '', l_a)
        a = data.Default()
        a.f_color = colorvise[0]
        a.f_advise = colorvise[1]
        a.e_color = colorvise[2]
        a.e_advise = colorvise[3]
        a.o_color = colorvise[4]
        a.o_advise = colorvise[5]
        a.l_color = colorvise[6]
        a.l_advise = colorvise[7]
        db.update_budget(session['username'], a)
        bdb = shelve.open('budget.db')
        saved_total = a.total - a.food_e - a.others_e - a.essen_e - a.leisure_e
        return render_template("Advisor.html", title='Advisor', db=db, bdb=bdb, saved_total=saved_total)


@app.route('/Activity')
def Activity():
    db = activity
    bdb = shelve.open('activity.db')
    return render_template("activitysubmit.html", title='Activity', db=db, bdb=bdb)


@app.route('/activitySubmit', methods=['POST', 'GET'])
def activitySubmit():
    if request.method == 'POST':
        result = request.form
        activity_name = result['activityName']
        image = result['image']
        hours = result['hours']
        pricing = result['pricing']
        a = activities.Activity()
        a.image = image
        a.name = activity_name
        a.hours = hours
        a.pricing = pricing
        db = activity
        db.add_activity(session['username'], a)
        bdb = shelve.open('activity.db')
        return render_template("Activity.html", result=result, db=db, bdb=bdb)


@app.route('/rSubmit', methods=['GET', 'POST'])
def rSubmit():
    if request.method == 'POST':
        result = request.form
        a = result['returnName']
        db = activity
        db.remove_activity(session['username'], a)
        bdb = shelve.open('activity.db')
        return render_template('rSubmit.html', result=result, db=db, bdb=bdb)



@app.route('/Library')
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
    log = str(session['username']) + 'LOGBOOK'
    return render_template('BorrowedBooks.html', book=book, bdb=bdb, genres=genres, db=db, log=log)


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
        db.storeBook(session['username'], book)
        bdb = shelve.open('bookLoans.db')
        log = str(session['username']) + 'LOGBOOK'
        return render_template("BookSubmit.html", result=result, db=db, bdb=bdb, log=log)


@app.route('/ReminderSubmit', methods=['GET', 'POST'])
def reminderSubmit():
    if request.method == 'POST':
        result = request.form
        bookname = result['books']
        remindDate = result['RemindDate']
        db = BookDatabase
        remindDate2 = datetime.datetime.strptime(remindDate, '%Y-%m-%d').date()
        # replace all session['username']s with username
        reminder = Reminder.Reminder(session['username'], remindDate2)
        reminder.set_book(session['username'], bookname)
        db.store_reminder(session['username'], reminder, bookname)
        return render_template('ReminderSubmit.html', result=result, db=db)


@app.route('/RenewSubmit', methods=['GET', 'POST'])
def renewSubmit():
    if request.method == 'POST':
        result = request.form
        book = result['renewBooks']
        db = BookDatabase
        db.renewBook(session['username'], book)
        bdb = shelve.open('bookLoans.db')
        return render_template('RenewSubmit.html', result=result, db=db, bdb=bdb)


@app.route('/ReturnSubmit', methods=['GET', 'POST'])
def returnSubmit():
    if request.method == 'POST':
        result = request.form
        book = result['returnBook']
        db = BookDatabase
        db.deleteBook(session['username'], book)
        bdb = shelve.open('bookLoans.db')
        return render_template('ReturnSubmit.html', result=result, db=db, bdb=bdb)

@app.route('/transportmain')
def transportmain():
    return render_template('transport_main.html')

@app.route('/transport')
def transport():
    return render_template('transport.html')


@app.route('/directions')
def directions():
    return render_template('directions.html')


@app.route('/amenities', methods=('GET', 'POST'))
def route():
    return render_template('amenities.html')


@app.route('/travels')
def travels():
    db = shelve.open('travel')
    bdb = shelve.open('travel.db')
    return render_template('travels.html', db=db, bdb=bdb)


@app.route('/add_travel', methods=('GET', 'POST'))
def add_travel():
    form = TravelForm(request.form)
    if request.method == 'POST' and form.validate():
        start = form.start.data
        destination = form.destination.data
        fare = form.fare.data
        date = form.date.data
        a = traveldata.Travel()
        a.destination = destination
        a.start = start
        a.fare = fare
        a.date = date
        db = traveldata
        db.create_travel('Bob', a)
        flash('Your travel has been added', 'success')
        return redirect(url_for('travels'))
    bdb = shelve.open('travel.db')
    return render_template('add_travel.html', form=form, bdb=bdb)


if __name__ == '__main__':
    app.run()
