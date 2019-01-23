from flask import *
from forms import SurveyForm, transfer_form, topup_form, LoginForm, RegisterForm
import data
import activity
from user import *
import Book, Due_date, Reminder
from functools import wraps
import activities


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config.from_mapping(
    SECRET_KEY='dev'
)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/loggedin')
def loggedin():
    return render_template('loggedin.html')


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
            session['username'] = user.username

            flash('You are now logged in','success')
            return render_template('loggedin.html')

        flash(error)
    return render_template('login.html', form=login_form)


#Register
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = form.id.data
        password = form.password.data
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            create_user(username, password)
            flash('You are now registered and can log in', 'success')
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html', form=form)


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


@app.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/pay')
def pay():
    return render_template("pay.html", title="Pay")

# Transfer Tab


@app.route('/transfer')
def transfer():
    form1 = transfer_form()
    form2 = topup_form()
    return render_template("transfer.html", title="Transfer", form1=form1, form2=form2)


@app.route('/transactions')
def transactions():
    return render_template("transactions.html", title="Transactios")


@app.route('/add')
def add():
    return render_template("add.html", title="Add")


@app.route('/Finance')
def Financehome():
    return render_template("Finance.html", title='Finance')


@app.route('/Survey', methods=['GET', 'POST'])
def Survey():
    form = SurveyForm()
    if form.validate_on_submit():
        flash(f'F&B: {form.f_budget.data}\n Essential: {form.e_budget.data}\n Leisure: {form.l_budget.data}\n Others: {form.o_budget.data} Submitted!', 'success')
        s = shelve.open('test_shelf.db')
        s['Budget'] = {'Food and Beverage': form.f_budget.data, 'Essentials': form.e_budget.data, 'Leisure': form.l_budget.data, 'Others': form.o_budget.data}
        s.close()
        return redirect(url_for('Advisor'))
    else:
        s = shelve.open('test_shelf.db')
        s['Budget'] = {'Food and Beverage': '', 'Essentials': '', 'Leisure': '', 'Others': ''}
        s.close()
    return render_template("Survey.html", title='Survey', form=form)


@app.route('/Savings')
def Savings():
    saved_data = data.get_save()
    return render_template("Savings.html", title='Savings', saved_data=saved_data)


@app.route('/Spending')
def Spending():
    spending_data = data.get_spend()
    return render_template("Spending.html", title='Spending', spending_data=spending_data)


@app.route('/Advisor')
def Advisor():
    f_a = data.f_a
    l_a = data.l_a
    e_a = data.e_a
    o_a = data.o_a
    food_budget = data.food_budget
    essen_budget = data.essen_budget
    others_budget = data.others_budget
    leisure_budget = data.leisure_budget
    spending_data = data.spending_data
    saved_total = data.saved_total
    return render_template("Advisor.html", title='Advisor', spending_data=spending_data, food_budget=food_budget,
                           f_a=f_a, l_a=l_a, e_a=e_a, o_a=o_a, saved_total=saved_total, essen_budget=essen_budget,
                           others_budget=others_budget, leisure_budget=leisure_budget)


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
        db.add_activity('Bob', a)
        bdb = shelve.open('activity.db')
        return render_template("Activity.html", result=result, db=db, bdb=bdb)


@app.route('/ReturnSubmit', methods=['GET', 'POST'])
def returnSubmit():
    if request.method == 'POST':
        result = request.form
        a = result['returnName']
        db = activity
        db.remove_activity('Bob', a)
        bdb = shelve.open('activity.db')
        return render_template('ReturnSubmit.html', result=result, db=db, bdb=bdb)


@app.route('/library')
def libraryhome():
    return render_template("Library.html")


@app.route('/Reminders')
def reminders():
    bk = ['Dante', 'Locker B']
    books = Book.Book
    reminder = Reminder.Reminder
    return render_template("Reminders.html", books=books, reminder=reminder, bk=bk)


@app.route('/Payment')
def payment():
    return render_template("Payment.html")


@app.route('/RecommendedBooks')
def recBooks():
    return render_template("RecommendedBooks.html")


@app.route('/BooksOnLoan')
def loaned():
    book = Book
    duedate = Due_date
    return render_template('BorrowedBooks.html', book=book, duedate=duedate)


if __name__ == '__main__':
    app.run()
