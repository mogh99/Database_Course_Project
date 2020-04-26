from application import db


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
	db.Column("time", db.String(20), nullable=False))

class Match(db.Model):
	matchID = db.Column(db.Integer, primary_key=True, nullable=False)
	team1ID = db.Column(db.Integer, db.ForeignKey("team.teamID"), nullable=False)
	team2ID = db.Column(db.Integer, db.ForeignKey("team.teamID"), nullable=False)
	fieldID = db.Column(db.Integer, db.ForeignKey("field.fieldID"), nullable=False)
	date = db.Column(db.String(20), nullable=False)
	time = db.Column(db.String(20), nullable=False)
	team1Goals = db.Column(db.Integer, nullable=False, default=0)
	team2Goals = db.Column(db.Integer, nullable=False, default=0)
	comments = db.Column(db.String(100), nullable=True)

	team1Relation = db.relationship("Team", foreign_keys=[team1ID], backref=db.backref("team1Relation", lazy=True))
	team2Relation = db.relationship("Team", foreign_keys=[team2ID], backref=db.backref("team2Relation", lazy=True))

	fieldRelation = db.relationship("Field", foreign_keys=[fieldID], backref=db.backref("fieldRelation", lazy=True))

	def __repr__(self):
		return (f"Match('{self.matchID}','{self.team1ID}','{self.team2ID}','{self.fieldID}','{self.date}','{self.time}','{self.team1Goals}','{self.team2Goals}','{self.comments}')")
		

class Team(db.Model):
	teamID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	
	def __repr__(self):
		return (f"Team('{self.teamID}','{self.name}')")

class Actor(db.Model):
	kfupmID = db.Column(db.Integer, primary_key=True, nullable=False)
	firstName = db.Column(db.String(20), nullable=False)
	lastName = db.Column(db.String(20), nullable=False)
	departmentID = db.Column(db.Integer, db.ForeignKey("department.departmentID"), nullable=False)
	typeID = db.Column(db.Integer, db.ForeignKey("type.typeID"), nullable=False)

	

	def __repr__(self):
		return (f"Actor('{self.kfupmID}','{self.firstName}','{self.lastName}','{self.departmentID}','{self.typeID}')")


class Category(db.Model):
	categoryID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(100), nullable=True)
	
	def __repr__(self):
		return (f"Category('{self.categoryID}','{self.name}','{self.description}')")

class Type(db.Model):
	typeID = db.Column(db.Integer, primary_key=True, nullable=False)
	categoryID = db.Column(db.Integer, db.ForeignKey('category.categoryID'), nullable=False)
	name = db.Column(db.String(20), nullable=False)
	description = db.Column(db.String(100), nullable=True)
	
	categoryRelation = db.relationship("Category", foreign_keys=[categoryID], backref=db.backref("categoryRelation", lazy=True))

	def __repr__(self):
		return (f"Type('{self.typeID}','{self.categoryID}','{self.name}','{self.description}')")

class Field(db.Model):
	fieldID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(100), nullable=True)
	
	def __repr__(self):
		return (f"Field('{self.fieldID}','{self.name}','{self.description}')")

class Department(db.Model):
	departmentID = db.Column(db.Integer, primary_key=True, nullable=False)
	code = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	
	def __repr__(self):
		return (f"Department('{self.departmentID}','{self.code}','{self.name}')")

 