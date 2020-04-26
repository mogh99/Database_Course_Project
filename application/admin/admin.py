from flask import Blueprint, render_template
from application.admin.forms import addMatchForm, addGoalsForm, assignCardForm, changeFieldForm 
from application.models import *

adminApp = Blueprint('adminApp', __name__)

report1 = [
            {"teamName": "team1",
            "goalsScored":5,
            "goalsReceived": 10,
            "points": 3,
            "rank": 10}
            ,
            {"teamName": "team2",
            "goalsScored": 10,
            "goalsReceived": 10,
            "points": 10,
            "rank": 1}
          ]

report2 = [
            {"playerName": "mohammed",
            "teamName":"team1",
            "type":"student"}
          ]

report3 = [
            {"playerName": "mohammed",
            "teamName":"team1",
            "type":"student",
            "goalsScored": 10,
            "goalsReceived": 10,
            "points": 10,
            "rank": 1}
          ]

@adminApp.route("/admin")
def admin():
    # initiate all the needed froms
    matchForm = addMatchForm()
    matchForm.team1Name.choices = [(instance.teamID, instance.name) for instance in db.session().query(Team).all()]
    matchForm.team2Name.choices = matchForm.team1Name.choices
    matchForm.field.choices = [(instance.fieldID, instance.name) for instance in db.session().query(Field).all()]

    goalsForm = addGoalsForm()
    goalsForm.matchID.choices = [(instance.matchID, f"Match{instance.matchID}") for instance in db.session().query(Match).all()]

    cardForm  = assignCardForm()
    matchQuery = f"SELECT matchID FROM Match WHERE matchID IN (SELECT matchID FROM matchActor)"
    cardForm.matchID.choices = [(instance.matchID, f"Match{instance.matchID}") for instance in db.engine.execute(matchQuery)]
    cardForm.kfupmID.choices = [(instance.kfupmID, f"{instance.kfupmID}, Match:{instance.matchID}") for instance in db.session().query(matchActor).all()]

    fieldForm = changeFieldForm()
    fieldForm.matchID.choices = [(instance.matchID, f"Match{instance.matchID}") for instance in db.session().query(Match).all()]
    fieldForm.fieldID.choices = [(instance.fieldID, instance.name) for instance in db.session().query(Field).all()]

    
    #render the admin page with all the forms, and reports
    return render_template("forms.html", title="admin", 
                            reports=[report1, report2, report3], 
                            forms=[matchForm, goalsForm, cardForm, fieldForm])