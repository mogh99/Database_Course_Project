from application import db


class Match(db.Model):
	matchID = db.Column(db.Integer, primary_key=True, nullable=False)
	team1ID = db.Column(db.Integer, db.ForeignKey("team.teamID"), nullable=False)
	team2ID = db.Column(db.Integer, db.ForeignKey("team.teamID"), nullable=False)
	fieldID = db.Column(db.Integer, db.ForeignKey("field.fieldID"), nullable=False)
	date = db.Column(db.Date, nullable=False)
	time = db.Column(db.DateTime, nullable=False)
	team1Goals = db.Column(db.Integer, nullable=False, default=0)
	team2Goals = db.Column(db.Integer, nullable=False, default=0)
	comments = db.Column(db.String(100), nullable=True)

	team1Relation = db.relationship("Team", foreign_keys=[team1ID])
	team2Relation = db.relationship("Team", foreign_keys=[team2ID])

	def __repr__(self):
		return (f'''Match('{self.matchID}','{self.team1ID}','{self.team2ID}','{self.fieldID}','{self.date}','{self.time}','{self.team1Goals}','{self.team2Goals}','{self.comments}')''')
		

class Team(db.Model):
	teamID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	
	def __repr__(self):
		pass

class Actor(db.Model):
	kfupmID = db.Column(db.Integer, primary_key=True, nullable=False)
	firstName = db.Column(db.String(20), nullable=False)
	lastName = db.Column(db.String(20), nullable=False)
	departmentID = db.Column(db.Integer, db.ForeignKey("department.departmentID"), nullable=False)
	
	typeID = db.Column(db.Integer, db.ForeignKey("type.typeID"), nullable=False)
	typeRelation = db.relationship('Type', foreign_keys=[typeID])

	def __repr__(self):
		pass


class Category(db.Model):
	categoryID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(100), nullable=True)
	type_ = db.relationship('Type', backref='type_', lazy=True)

	def __repr__(self):
		pass

class Type(db.Model):
	typeID = db.Column(db.Integer, primary_key=True, nullable=False)
	categoryID = db.Column(db.Integer, db.ForeignKey('category.categoryID'), nullable=False)
	name = db.Column(db.String(20), nullable=False)
	description = db.Column(db.String(100), nullable=True)
	

	def __repr__(self):
		pass

class Field(db.Model):
	fieldID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(100), nullable=True)
	match = db.relationship('Match', backref='match', lazy=True)

	def __repr__(self):
		pass

class Department(db.Model):
	departmentID = db.Column(db.Integer, primary_key=True, nullable=False)
	code = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	actor = db.relationship('Actor', backref='actor', lazy=True)

	def __repr__(self):
		pass

#Many-To-Many Relations
tournamentActor = db.Table("torActor",
	db.Column("kfupmID", db.Integer, db.ForeignKey("actor.kfupmID"), nullable=False),
	db.Column("teamID", db.Integer, db.ForeignKey("team.teamID"), nullable=False),
	db.Column("typeID", db.Integer, db.ForeignKey("type.typeID"), nullable=False))

matchActor = db.Table("matchActor",
	db.Column("matchID", db.Integer, db.ForeignKey("match.matchID"), nullable=False),
	db.Column("kfupmID", db.Integer, db.ForeignKey("actor.kfupmID"), nullable=False),
	db.Column("typeID", db.Integer, db.ForeignKey("type.typeID"), nullable=False))

event = db.Table("event",
	db.Column("matchID", db.Integer, db.ForeignKey("match.matchID"), nullable=False),
	db.Column("kfupmID", db.Integer, db.ForeignKey("actor.kfupmID"), nullable=False),
	db.Column("typeID", db.Integer, db.ForeignKey("type.typeID"), nullable=False),
	db.Column("time", db.DateTime(), nullable=False)) 