#db_creator.py

import csv
import pandas as pd
import sqlite3

from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, create_engine, Date, Float, ForeignKey, Integer, String, Table, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
	
WorksxAuthors = Table(
	"works_x_authors",
	Base.metadata,
	Column("author", Integer, ForeignKey("authors.id")),
	Column("work", Integer, ForeignKey("works.id"))
)	
 
class Work(Base):
	__tablename__ = "works"
	__table_args__ = {"sqlite_autoincrement": True} 
	id = Column(Integer, primary_key=True, nullable=False)
	title = Column(String) # id:0
	department = Column(String)
	date = Column(String) # id:1
	authors = relationship(
		"Author",
		secondary=WorksxAuthors,
		back_populates="works"
	)
 
	def __str__(self):
		return "{}".format(self.title)
	
class Author(Base):
	__tablename__ = "authors"
	__table_args__ = {"sqlite_autoincrement": True}
 
	id = Column(Integer, primary_key=True, nullable=False) 
	name = Column("name", VARCHAR(100)) # id:0
	works = relationship(
		"Work",
		secondary=WorksxAuthors,
		back_populates="authors"
	)
	
	def __str__(self):
		return "{}".format(self.name)
 
if __name__ == "__main__":
	t = time()
	print("Start Time: {}".format(str(t)))

	engine = create_engine("sqlite:///pubhub.db", echo=True)
	Session = sessionmaker(bind=engine)
	session = Session()
	
	# start with a clean slate (delete all tables)
	conn = sqlite3.connect("pubhub.db")
	c = conn.cursor()
	c.execute("DROP TABLE IF EXISTS works")
	c.execute("DROP TABLE IF EXISTS authors")
	c.execute("DROP TABLE IF EXISTS works_x_authors")

	# dirty the slate again (create tables)
	Base.metadata.create_all(engine) 

	print("Time elapsed: {}s.".format(str(time() - t)))
