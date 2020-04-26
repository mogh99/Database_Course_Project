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

	def __repr__(self):
		pass
		

class Team(db.Model):
	teamID = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(20), unique=True, nullable=False)
	match = db.relationship("Match", backref="match", lazy=True)
	
	def __repr__(self):
		pass

class Actor(db.Model):
	kfupmID = db.Column(db.Integer, primary_key=True, nullable=False)
	firstName = db.Column(db.String(20), nullable=False)
	lastName = db.Column(db.String(20), nullable=False)
	departmentID = db.Column(db.Integer, db.ForeignKey("department.departmentID"), nullable=False)
	
	#typeID is many-to-one relation not one-to-many relation
	typeID = db.Column(db.Integer, db.ForeignKey("type.typeID"), nullable=False)
	type_ = db.relationship('Type', backref='type_', lazy=True)

	#contact = db.relationship('Contact', backref="contact", lazy=True)

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

# class ContactType(db.Model):
# 	contypeID = db.Column(db.Integer, primary_key=True, nullable=False)
# 	name = db.Column(db.String(20), unique=True, nullable=False)
# 	description = db.Column(db.String(100), nullable=False)
# 	contact = db.relationship('Contact', backref='contact', lazy=True)

# 	def __repr__(self):
# 		pass

# class Contact(db.Model):
# 	contactID = db.Column(db.Integer, primary_key=True)
# 	#kfupmID = db.Column(db.Integer, db.ForeignKey("actor.kfupmID"), nullable=False)
# 	contypeID = db.Column(db.Integer, db.ForeignKey("contacttype.contypeID"), nullable=False)
# 	value = db.Column(db.String(20), nullable=False)

# 	def __repr__(self):
# 		pass


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