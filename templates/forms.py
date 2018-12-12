from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class SurveyForm(FlaskForm):
    f_budget = FloatField('F&B Budget :', validators=[DataRequired(), NumberRange(min=0, max=1000)])
    l_budget = FloatField('Leisure Budget :', validators=[DataRequired(), NumberRange(min=0, max=1000)])
    e_budget = FloatField('Essential Budget :', validators=[DataRequired(), NumberRange(min=0, max=1000)])
    o_budget = FloatField('Others Budget :', validators=[DataRequired(), NumberRange(min=0, max=1000)])
    submit = SubmitField('Confirm')
