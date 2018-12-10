from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, IntegerField, validators, PasswordField
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

#Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'OOPPproj'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#init MYSQL
mysql = MySQL(app)


#index
@app.route('/')
def index():
    return render_template('home.html')

#Register Form Class
class RegisterForm(Form):
    fullname = StringField('Full Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    nric = StringField('NRIC', [validators.Length(min=9, max=9)])
    ezlinkNo = IntegerField('Ezlink Card No.', [validators.Length(min=16, max=16)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

#User Register
@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        fullname = form.fullname.data
        username = form.username.data
        email = form.email.data
        nric = form.nric.data
        ezlinkNo = form.ezlinkNo.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #Create cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO user(fullname, username, email, nric, ezlinkNo, password) VALUE(%s, %s, %s, %s, %s, %s)", (fullname, username, email, nric, ezlinkNo, password))

        #Commit to DB
        mysql.connection.commit()

        #Close connection
        cur.close()

        flash('You are now registered and can now log in', 'success')

        return redirect(url_for('index'))
    return render_template('register.html', form=form)


#User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        #Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        #Create cursor
        cur = mysql.connection.cursor()

        #Get user by username
        result = cur.execute("SELECT * FROM user WHERE username = %s", [username])

        if result > 0:
            #Get stored hash
            data = cur.fetchone()
            password = data['password']

            #Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                #Passed
                session["logged_in"] = True
                session["username"] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error)
            #Close connection
            cur.close()

        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template(login.html)

#Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unaurthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


#Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


#Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.secret_key='secret123'
    app.run()

