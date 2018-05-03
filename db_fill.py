# db_fill.py

import csv
import pandas as pd
import sqlite3
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db_creator import Work, Author
from time import time

if __name__ == '__main__':
	t = time()
	print("Time start: {}".format(str(t)))
	
	engine = create_engine('sqlite:///pubhub.db', echo=True)
	Session = sessionmaker(bind=engine)
	session = Session()

	Base = declarative_base()

	db = sqlite3.connect('pubhub.db')
	c = db.cursor()	
	file_name = "endnote.txt"
	delim="\t"

	with open (file_name, 'r') as infile, db:
		content = pd.read_csv(infile, delimiter=delim, header=None)
		for ind, row in content.iterrows():
			authors = row[0].split("//")
			date = row[1]
			title = row[2]
			publisher = row[3]
			# department = row[9]
			w = Work(title="{}".format(title), date="{}".format(date), authors=authors)
			a = Author(name="{}".format(author))
			session.add(w)
			session.add(a)
		session.commit()	

