from flask import Blueprint, render_template
from application.admin.forms import addMatchForm, addGoalsForm, assignCardForm, changeFieldForm 
from application.models import *
from application.main.forms import playersForm, refereeForm
from application.main.utils import playerInformation, matchInformation, teamInformation

adminApp = Blueprint('adminApp', __name__)

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

    #static reports
    playerInformationReport = playerInformation()
    matchInformationReport = matchInformation()
    teamInformatinoReport = teamInformation()

    #dynamic reports
    teamPlayers = playersForm()
    teamPlayers.match.choices = [(instance.matchID, f"Match{instance.matchID}") for instance in db.session().query(Match).all()]
    query = f"SELECT teamID FROM team;"
    teamPlayers.team.choices = [(instance.teamID, f"Team{instance.teamID}") for instance in db.engine.execute(query)]
    referees = refereeForm()
    query = f'''SELECT DISTINCT A.kfupmID, A.firstName, A.lastName 
                FROM matchActor M 
                JOIN actor A ON A.kfupmID=M.kfupmID 
                WHERE M.typeID=11 
                OR 
                M.typeID=12;'''
    referees.referee.choices = [(instance.kfupmID, f"{instance.firstName} {instance.lastName}") for instance in db.engine.execute(query)]

    #render the admin page with all the forms, and reports
    return render_template("forms.html", title="admin", 
                            staticReports=[ playerInformationReport, matchInformationReport],
                            dynamicReports=[teamPlayers, referees], 
                            forms=[matchForm, goalsForm, cardForm, fieldForm])