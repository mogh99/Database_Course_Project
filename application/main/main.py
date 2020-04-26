from flask import Flask, render_template, jsonify, Blueprint, redirect, url_for


mainApp = Blueprint('mainApp', __name__)

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

'''
    The main method is responsible for rendering the main page 
    with all the needed data.
'''
@mainApp.route("/")
@mainApp.route("/home")
def main():
    # render the main page with all the reports
    return render_template("reports.html", title="home", reports=[report1, report2, report3])



