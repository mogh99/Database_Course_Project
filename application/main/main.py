from flask import Flask, render_template, jsonify, Blueprint, redirect, url_for
from application.main.utils import playerInformation, matchInformation
from application.main.forms import playersForm, refereeForm
from application import db
from application.models import Match


mainApp = Blueprint('mainApp', __name__)


report1 = [
            {"playerName": "mohammed",
            "teamName":"team1",
            "type":"student"}
          ]

'''
    The main method is responsible for rendering the main page 
    with all the needed data.
'''
@mainApp.route("/")
@mainApp.route("/home")
def main():
    #static reports
    playerInformationReport = playerInformation()
    matchInformationReport = matchInformation()

    #dynamic reports
    teamPlayers = playersForm()
    teamPlayers.match.choices = [(instance.matchID, f"Match{instance.matchID}") for instance in db.session().query(Match).all()]
    query = f"SELECT M.matchID, T.teamID FROM match M NATURAL JOIN team T;"
    teamPlayers.team.choices = [(instance.teamID, f"Team{instance.teamID}, Match{instance.matchID}") for instance in db.engine.execute(query)]
    referees = refereeForm()
    query = f'''SELECT DISTINCT A.kfupmID, A.firstName, A.lastName 
                FROM matchActor M 
                JOIN actor A ON A.kfupmID=M.kfupmID 
                WHERE M.typeID=11 
                OR 
                M.typeID=12;'''
    referees.referee.choices = [(instance.kfupmID, f"{instance.firstName} {instance.lastName}") for instance in db.engine.execute(query)]
     
    # render the main page with all the reports
    return render_template("reports.html", title="home", 
                            staticReports=[report1, playerInformationReport, matchInformationReport],
                            dynamicReports=[teamPlayers, referees])