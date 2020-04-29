from application import db		

class Team(object):
	def __init__(self, teamID, goalsScored, goalsRecivied):
		self.teamID = teamID
		self.goalsScored = goalsScored
		self.goalsRecivied = goalsRecivied
		self.rank = 1


def teamsInformation():
	teamsQuery = f"SELECT teamID FROM team;"
	teamsIDs = db.engine.execute(teamsQuery)

	teams = [Team(teamID=team.teamID, goalsScored=0, goalsRecivied=0) for team in teamsIDs]
	
	matchQuery = f"SELECT * FROM match;"
	matchsData = db.engine.execute(matchQuery)

	matchs = [{"team1ID":match.team1ID, "team2ID":match.team2ID, "team1Goals":match.team1Goals, "team2Goals":match.team2Goals} for match in matchsData]

	for match in matchs:
		for team in teams:
			if team.teamID == match["team1ID"]:
				team.goalsScored = match["team1Goals"] + team.goalsScored
				team.goalsRecivied = match["team2Goals"] + team.goalsRecivied
			elif team.teamID == match["team2ID"]:
				team.goalsScored = match["team2Goals"] + team.goalsScored
				team.goalsRecivied = match["team1Goals"] + team.goalsRecivied

	teamRank(teams)

	data = [{"TeamID":team.teamID, "Goals Scored":team.goalsScored, "Goals Recivied":team.goalsRecivied, "Points":team.goalsScored*2, "Rank":team.rank} for team in teams]

	return data


def teamRank(teams):

	for team1 in teams:
		for team2 in teams:
			if team1.goalsScored < team2.goalsScored:
				team1.rank = team1.rank + 1


'''
	playerInformation() and matchInformation()
	populate the reports in the main, and admin page
'''

def playerInformation():
	'''
		this method will return the information of the players
		who scored more than two goals.
	'''
	query = f'''SELECT A.kfupmID, A.firstName, A.lastName, D.name, T.name 
				FROM actor A 
				NATURAL JOIN department D 
				JOIN type T ON T.typeID=A.typeID 
				WHERE kfupmID IN(
					SELECT kfupmID 
					FROM event 
					GROUP BY kfupmID 
					HAVING COUNT(typeID) >= 2 AND typeID = 15);
			'''
	result = db.engine.execute(query)
	return [{"playerID":instance.kfupmID, "First Name":instance.firstName, "Last Name":instance.lastName, "Department":instance[3], "type":instance[4]} for instance in result]


def matchInformation():
	'''
		this method will return the informatino of all the match
	'''
	query = f'''SELECT M.matchID, F.name, T1.name, T2.name, M.date, M.time, M.team1Goals, M.team2Goals 
				FROM match M 
				JOIN team T1 ON T1.teamID=M.team1ID 
				JOIN team T2 ON T2.teamID=M.team2ID 
				JOIN field F ON F.fieldID=M.fieldID;
			'''
	result = db.engine.execute(query)
	return [{"Match":f"Match{instance[0]}", 
			"Field":instance[1], 
			"Team1 Name":instance[2], 
			"Team2 Name":instance[3], 
			"Date":instance[4], 
			"Time":instance[5], 
			"Team1 Goals":instance[6], 
			"Team2 Goals":instance[7]} for instance in result]