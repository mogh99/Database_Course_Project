from flask import Blueprint, jsonify, url_for
from application.main.forms import playersForm, refereeForm
from application import db
from application.models import *

processesMainApp = Blueprint('processesMainApp', __name__)


@processesMainApp.route("/playersFormProcess", methods=["POST"])
def playersFormProcess():
	form = playersForm()
	form.match.choices = [(instance.matchID, f"Match{instance.matchID}") for instance in db.session().query(Match).all()]
	query = f"SELECT M.matchID, T.teamID FROM match M NATURAL JOIN team T;"
	form.team.choices = [(instance.teamID, f"Team{instance.teamID}, Match{instance.matchID}") for instance in db.engine.execute(query)]
	#if order_type.submit.data and order_type.validate_on_submit():
	if form.validate_on_submit():
		#Insert The data and return the success message
		#Insert the data to the database
		playerQuery = f'''SELECT T.kfupmID, A.firstName, A.lastName, D.name, Y.name  
						FROM torActor T 
						JOIN matchActor M ON M.kfupmID=T.kfupmID 
						JOIN actor A ON A.kfupmID=T.kfupmID 
						JOIN department D ON A.departmentID=D.departmentID 
						JOIN type Y ON Y.typeID=A.typeID 
						WHERE T.teamID={form.team.data} AND M.matchID={form.match.data};'''
		result = db.engine.execute(playerQuery)
		data = [{"kfupmID":instance[0], "FirstName":instance[1], "SecondName":instance[2], "Department":instance[3], "Type":instance[4]} for instance in result]
		return jsonify(report=data)
	#send an error message that include all the possible errors
	return jsonify(error=form.errors)

@processesMainApp.route("/refereeFormProcess", methods=["POST"])
def refereeFormProcess():
	form = refereeForm()
	query = f'''SELECT DISTINCT A.kfupmID, A.firstName, A.lastName 
				FROM matchActor M 
				JOIN actor A ON A.kfupmID=M.kfupmID 
				WHERE M.typeID=11 
				OR 
				M.typeID=12;'''
	form.referee.choices = [(instance.kfupmID, f"{instance.firstName} {instance.lastName}") for instance in db.engine.execute(query)]
	
	#if order_type.submit.data and order_type.validate_on_submit():
	if form.validate_on_submit():
		#Insert The data and return the success message
		#Insert the data to the database
		refereeQuery = f'''SELECT M.matchID, F.name, T1.name, T2.name, M.date, M.time, M.team1Goals, M.team2Goals 
				FROM match M 
				JOIN team T1 ON T1.teamID=M.team1ID 
				JOIN team T2 ON T2.teamID=M.team2ID 
				JOIN field F ON F.fieldID=M.fieldID
				WHERE matchID IN (
					SELECT matchID 
					FROM matchActor 
					WHERE kfupmID = {form.referee.data}
				);
			'''
		result = db.engine.execute(refereeQuery)
		data = [{"Match":f"Match{instance[0]}", 
			"Field":instance[1], 
			"Team1 Name":instance[2], 
			"Team2 Name":instance[3], 
			"Date":instance[4], 
			"Time":instance[5], 
			"Team1 Goals":instance[6], 
			"Team2 Goals":instance[7]} for instance in result]

		return jsonify(report=data)
	#send an error message that include all the possible errors
	return jsonify(error=form.errors)

