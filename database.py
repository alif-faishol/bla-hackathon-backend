import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

if os.path.exists('database.sqlite3'):
    os.remove('database.sqlite3')

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))

Base = declarative_base()
Base.metadata.bind = engine
