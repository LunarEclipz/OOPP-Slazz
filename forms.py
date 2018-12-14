from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo

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

