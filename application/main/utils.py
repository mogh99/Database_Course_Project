from application import db


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