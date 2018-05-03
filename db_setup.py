# db_setup.py 

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///pubhub.db", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
					 autoflush=False,
					 bind=engine))

def init_db():
    import models
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
	Base.query = db_session.query_property()
 
