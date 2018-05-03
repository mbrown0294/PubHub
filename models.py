# models.py

from app import db

association = db.Table("association",
	db.Column("author_id", db.Integer, db.ForeignKey("authors.id")),
	db.Column("work_id", db.Integer, db.ForeignKey("works.id"), primary_key=True)
)

class Author(db.Model):
	__tablename__ = "authors"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	def __repr__(self):
		return self.name


class Work(db.Model):
	__tablename__ = "works"

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String)
	department = db.Column(db.String)
	date = db.Column(db.String)
	authors = db.relationship(
		"Author", 
		secondary=association, 
		lazy='subquery',
		backref=db.backref(
			"works", lazy=True)
	)

	def __str__(self, id, title, date):
		self.id = id
		self.title = title
		self.date = date

	def __repr__(self):
		return self.title
