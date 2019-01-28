from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, StringField, PasswordField, Form
from wtforms.validators import DataRequired, NumberRange, Length, EqualTo
from wtforms import validators


class SurveyForm(FlaskForm):
    f_budget = FloatField('F&B Budget :', validators=[DataRequired(), NumberRange(min=0, max=400)])
    l_budget = FloatField('Leisure Budget :', validators=[DataRequired(), NumberRange(min=0, max=400)])
    e_budget = FloatField('Essential Budget :', validators=[DataRequired(), NumberRange(min=0, max=400)])
    o_budget = FloatField('Others Budget :', validators=[DataRequired(), NumberRange(min=0, max=400)])
    submit = SubmitField('Confirm')


class transfer_form(FlaskForm):
    payee = StringField("Payee:", validators=[DataRequired()])
    amount = StringField("Enter Amount:", validators=[DataRequired(), Length(min=1, max=6)])
    submit = SubmitField("Confirm")

class topup_form(FlaskForm):
    topup = StringField("Bank Account:", validators=[DataRequired(), Length(max=20)])
    amount = StringField("Enter Amount:", validators=[DataRequired(), Length(min=1, max=6)])
    pin = StringField("Bank Account Pin:", validators=[DataRequired(), Length(max=10)])
    confirm_pin = StringField("Confirm Bank Account Pin:", validators=[DataRequired(), EqualTo("pin ")])
    submit = SubmitField("Confirm")



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
