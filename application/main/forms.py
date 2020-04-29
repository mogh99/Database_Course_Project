from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class loginForm(FlaskForm):
	username = StringField("Username", render_kw={"placeholder": "username"},validators=[
																		DataRequired(),
																		Length(min=5, max=15)])

	password = PasswordField("Password", render_kw={"placeholder": "password"},validators=[
																		DataRequired(),
																		Length(min=5, max=15)])

class playersForm(FlaskForm): 
	match = SelectField("Match", choices=[], validators=[DataRequired()], coerce=int)

	team = SelectField("Team", choices=[], validators=[DataRequired()], coerce=int)

	submit = SubmitField("Submit")

class refereeForm(FlaskForm):
	referee = SelectField("Referee", choices=[], validators=[DataRequired()], coerce=int)

	submit = SubmitField("Submit")
