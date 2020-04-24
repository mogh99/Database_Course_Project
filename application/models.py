from application import db


class Tournament(db.Model):
	tournamentID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	startDate = db.Column(db.Date, nullable=False)
	endDate = db.Column(db.Date, nullable=False)

	def __repr__(self):
		return (f'''Tournament(
			'{self.tournamentID}', 
			'{self.name}', 
			'{self.startDate}', 
			'{self.endDate}')''')

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

	def __repr__(self):
		pass
		

class Team(db.Model):
	teamID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	
	def __repr__(self):
		pass

class Actor(db.Model):
	kfupmID = db.Column(db.Integer, primary_key=True, nullable=False)
	firstName = db.Column(db.String(20), nullable=False)
	lastName = db.Column(db.String(20), nullable=False)
	goals = db.Column(db.Integer, nullable=False, default=0)
	departmentID = db.Column(db.Integer, db.ForeignKey("department.departmentID"), nullable=False)
	typeID = db.Column(db.Integer, db.ForeignKey("type.typeID"), nullable=False)

	def __repr__(self):
		pass


class Category(db.Model):
	categoryID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(100), nullable=True)

	def __repr__(self):
		pass

class Type(db.Model):
	typeID = db.Column(db.Integer, primary_key=True, nullable=False)
	categoryID = db.Column(db.Integer, db.ForeignKey('category.categoryID'), nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(100), nullable=True)

	def __repr__(self):
		pass

class Field(db.Model):
	fieldID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(100), nullable=True)

	def __repr__(self):
		pass

class Department(db.Model):
	departmentID = db.Column(db.Integer, primary_key=True, nullable=False)
	code = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)

	def __repr__(self):
		pass

class ConatactType(db.Model):
	contypeID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	description = db.Column(db.String(100), nullable=False)

	def __repr__(self):
		pass

class Contact(db.Model):
	kfupmID = db.Column(db.Integer, db.ForeignKey("actor.kfupmID"), nullable=False)
	contypeID = db.Column(db.Integer, db.ForeignKey("contaacttype.contypeID"), nullable=False)
	value = db.Column(db.String(20), nullable=False)
	def __repr__(self):
		pass


tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

#Many-To-Many Relations
# tournamentActor = db.Table('torActor',
# 	db.Column("tournamentID", db.Integer, db.ForeignKey("tournament.tournamentID")),
# 	db.Column("kfupmID", db.Integer, db.ForeignKey("actor.actorID")),
# 	db.Column("teamID", db.Integer, db.ForeignKey("team.teamID"))
# 	db.Column("typeID", db.Integer, db.ForeignKey("type.typeID")))

# matchActor = 

# event = 