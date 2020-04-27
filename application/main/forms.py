from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from application.models import *


class playersForm(FlaskForm): 
	match = SelectField('Match', choices=[], validators=[DataRequired()], coerce=int)

	team = SelectField('Team', choices=[], validators=[DataRequired()], coerce=int)

	submit = SubmitField('Submit')

class refereeForm(FlaskForm):
	referee = SelectField('Referee', choices=[], validators=[DataRequired()], coerce=int)

	submit = SubmitField('Submit')
