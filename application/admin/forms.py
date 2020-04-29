from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class addMatchForm(FlaskForm): 
	team1Name = SelectField('Team1 Name', choices=[], validators=[DataRequired()], coerce=int)

	team2Name = SelectField('Team2 Name', choices=[], validators=[DataRequired()], coerce=int)

	field = SelectField('Field', choices=[], validators=[DataRequired()], coerce=int)

	date = StringField('Date', render_kw={"placeholder": "yyyy-mm-dd"},validators=[
																		DataRequired(),
																		Length(min=10, max=10)])
	time = StringField('Time', render_kw={"placeholder": "hh:mm"},validators=[
																	DataRequired(),
																	Length(min=5, max=5)])
	submit = SubmitField('Submit')

class addGoalsForm(FlaskForm):
	matchID = SelectField('Match ID', choices=[], validators=[DataRequired()], coerce=int)

	team1Goals = StringField('Team1 Goals',validators=[
											DataRequired(),
											Length(min=1, max=2)])
	team2Goals = StringField('Team2 Goals',validators=[
											DataRequired(),
											Length(min=1, max=2)])
	submit = SubmitField('Submit')

class assignCardForm(FlaskForm):
	matchID = SelectField('Match ID', choices=[], validators=[DataRequired()], coerce=int)

	kfupmID = SelectField('Player', choices=[], validators=[DataRequired()], coerce=int)

	time = StringField('Time', render_kw={"placeholder": "hh:mm"}, validators=[
																	DataRequired(),
																	Length(min=5, max=5)])
	submit = SubmitField('Submit')

class changeFieldForm(FlaskForm):
	matchID = SelectField('Match ID', choices=[], validators=[DataRequired()], coerce=int)

	fieldID = SelectField('Field ID', choices=[], validators=[DataRequired()], coerce=int)

	submit = SubmitField('Submit')
