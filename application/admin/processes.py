'''
	-This file process all the froms responses
	for the admin, and the guest users.
	
	-The methods name is consist of the forms methods names
	plus the work Process.
	example: addMatchForm + Process = addMathcFormProcess 
'''
from flask import Blueprint, jsonify, url_for
from application.admin.forms import addMatchForm, addGoalsForm, assignCardForm, changeFieldForm
from application import db
from application.models import *

processesApp = Blueprint('processesApp', __name__)

@processesApp.route("/addMatchFormProcess", methods=["POST"])
def addMatchFormProcess():
	form = addMatchForm()
	form.team1Name.choices = [(instance.teamID, instance.name) for instance in db.session().query(Team).all()]
	form.team2Name.choices = form.team1Name.choices
	form.field.choices = [(instance.fieldID, instance.name) for instance in db.session().query(Field).all()]

	#if order_type.submit.data and order_type.validate_on_submit():
	if form.validate_on_submit():
		#Insert The data and return the success message
		if form.team1Name.data != form.team2Name.data:
			#Insert the data to the database
			newMatch = Match(team1ID=form.team1Name.data, team2ID=form.team2Name.data, fieldID=form.field.data, date=form.date.data, time=form.time.data)
			db.session.add(newMatch)
			db.session.commit()
			return jsonify(success="The data have been inserted")
		else:
			return jsonify(error={"team1Name": ["Team1 Name Equals Team2 Name"]})
	#send an error message that include all the possible errors
	return jsonify(error=form.errors)

@processesApp.route("/addGoalsFormProcess", methods=["POST"])
def addGoalsFormProcess():
	form = addGoalsForm()
	form.matchID.choices = [(instance.matchID, f"Match{instance.matchID}") for instance in db.session().query(Match).all()]

	if form.validate_on_submit():
		#insert the data to the database
		updateMatch = db.session().query(Match).get(form.matchID.data)
		updateMatch.team1Goals = form.team1Goals.data
		updateMatch.team2Goals = form.team2Goals.data
		db.session().commit()
		return jsonify(success="The data have been inserted")
	#send an error message that include all the possible errors
	return jsonify(error=form.errors)

@processesApp.route("/assignCardFormProcess", methods=["POST"])
def assignCardFormProcess():
	form = assignCardForm()
	form.matchID.choices = [(instance.matchID, f"Match{instance.matchID}") for instance in db.session().query(matchActor).all()]
	form.kfupmID.choices = [(instance.kfupmID, f"{instance.kfupmID}, Match:{instance.matchID}") for instance in db.session().query(matchActor).all()]
    
	if form.validate_on_submit():
		#insert the data to the database
		newEvent = event()
		return jsonify(success="The data have been inserted")
	#send an error message that include all the possible errors
	return jsonify(error=form.errors)

@processesApp.route("/changeFieldFormProcess", methods=["POST"])
def changeFieldFormProcess():
	form = changeFieldForm()
	form.matchID.choices = [(instance.matchID, f"Match{instance.matchID}") for instance in db.session().query(Match).all()]
	form.fieldID.choices = [(instance.fieldID, instance.name) for instance in db.session().query(Field).all()]

	if form.validate_on_submit():
		#insert the data to the database
		updateMatch = db.session().query(Match).get(form.matchID.data)
		updateMatch.fieldID = form.fieldID.data
		db.session().commit()
		return jsonify(success="The data have been inserted")
	#send an error message that include all the possible errors
	return jsonify(error=form.errors)


