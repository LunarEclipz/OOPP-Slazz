from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class SurveyForm(FlaskForm):
    f_budget = FloatField('F&B Budget :', validators=[DataRequired(), NumberRange(min=0, max=400)])
    l_budget = FloatField('Leisure Budget :', validators=[DataRequired(), NumberRange(min=0, max=400)])
    e_budget = FloatField('Essential Budget :', validators=[DataRequired(), NumberRange(min=0, max=400)])
    o_budget = FloatField('Others Budget :', validators=[DataRequired(), NumberRange(min=0, max=400)])
    submit = SubmitField('Confirm')
