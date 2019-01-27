from flask import *
from user import *
from forms import *
from functools import wraps
from traveldata import *


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

#Login
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
            return render_template('loggedin.html')

        flash(error, 'danger')
    return render_template('login.html', form=login_form)
#/Login

#Register
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
#/Register

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
#/Check

#Logout
@app.route('/logout', methods=('GET', 'POST'))
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/loggedin')
def loggedin():
    return render_template('loggedin.html')

#Transport
@app.route('/transport')
def transport():
    return render_template('transport.html')

@app.route('/directions')
def directions():
    return render_template('directions.html')

@app.route('/routes', methods=('GET', 'POST'))
def route():
    return render_template('routes.html')

@app.route('/travels')
def travels():
    return render_template('travels.html')

@app.route('/add_travel', methods=('GET', 'POST'))
def add_travel():
    form = TravelForm(request.form)
    if request.method == 'POST' and form.validate():
        start = form.start.data
        destination = form.destination.data
        fare = form.fare.data
        create_travel(start, destination, fare)
        flash('Your travel has been added', 'success')
        return redirect(url_for('travels'))
    return render_template('add_travel.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
