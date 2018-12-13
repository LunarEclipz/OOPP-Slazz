from flask import *
from user import *
from forms import *
from functools import wraps

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
        error = None
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

if __name__ == '__main__':
    app.run(debug=True)
