from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, Form, PasswordField
from wtforms import validators, ValidationError
import datetime

class LoginForm(Form):
    id = StringField('Username', [validators.DataRequired('Please enter your name.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    submit = SubmitField('Login')

class RegisterForm(Form):
    id = StringField('Username', [validators.DataRequired('Please enter your name.')])
    email = StringField('Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired('Please enter your password.'),
    ])
    confirm = PasswordField('Confirm Password', [
        validators.EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')

# class TrainRoute(Form):
#     comingfrom = StringField('From: ', [validators.DataRequired('Please enter an MRT Station')])
#     goingto = StringField('To: ', [validators.DataRequired('Please enter an MRT Station.')])
#     submit = SubmitField('Calculate Route')

class TravelForm(Form):
    start = StringField('Starting Point')
    destination = StringField('Destination')
    fare = StringField('Fare')
    date_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    submit = SubmitField('Register')
