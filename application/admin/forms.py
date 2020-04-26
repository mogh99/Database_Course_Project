from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from application.models import *

class addMatchForm(FlaskForm):
	team1Name = StringField('Team1 Name',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	team2Name = StringField('Team2 Name',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	field = StringField('Field',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	date = StringField('Date',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	time = StringField('Time',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	submit = SubmitField('Submit')

class addGoalsForm(FlaskForm):
	matchID = StringField('Match ID',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	team1Goals = StringField('Team1 Goals',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	team2Goals = StringField('Team2 Goals',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	submit = SubmitField('Submit')

class assignCardForm(FlaskForm):
	matchID = StringField('Match ID',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	KFUPMID = StringField('Player ID',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	Time = StringField('Time',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	submit = SubmitField('Submit')

class changeFieldForm(FlaskForm):
	matchID = StringField('Match ID',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	FieldID = StringField('Field ID',validators=[
											DataRequired(),
											Length(min=2, max=20)])
	submit = SubmitField('Submit')
