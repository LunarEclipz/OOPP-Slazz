from flask import Flask, render_template, url_for, flash, redirect
from forms import SurveyForm, transfer_form, topup_form
import data
import Book, Due_date, Reminder

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


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
        data.save_budget(form)
        return redirect(url_for('Advisor'))

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
    spending_data = data.get_spend()
    budget_data = data.get_budget()
    account_data = data.get_account()
    f_b = budget_data['Food and Beverage'] - account_data['Spent_on_Food_and_Beverage']
    l_a = budget_data['Leisure'] - account_data['Spent_on_Leisure']
    e_a = budget_data['Essentials'] - account_data['Spent_on_Essentials']
    o_a = budget_data['Others'] - account_data['Spent_on_Others']
    saved_total = account_data['Total_Monthly_Allowance'] - account_data['Spent_on_Food_and_Beverage']\
                  - account_data['Spent_on_Leisure'] - account_data['Spent_on_Essentials'] - account_data['Spent_on_Others']
    return render_template("Advisor.html", title='Advisor', spending_data=spending_data, budget_data=budget_data,
                           f_b=f_b, l_a=l_a, e_a=e_a, o_a=o_a, saved_total=saved_total)


@app.route('/Activity')
def Activity():
    activities = data.get_activity()

    return render_template("Activity.html", title='Activity', activities=activities)


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
