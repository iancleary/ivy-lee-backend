import datetime

from sqlalchemy import create_engine
from sqlalchemy import insert, select, update
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import Session

# Pick one feature that will be useful for users
# and then go about implementing it in the simplest way possible

# name, release_date, watched

# CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS projects (
#     name TEXT,
#     release_timestamp REAL,
#     watched INTEGER
# );"""

# INSERT_MOVIES = "INSERT INTO projects (name, release_timestamp, watched) VALUES (?, ?, 0);" # good practice to include columns, leave empty does all
# SELECT_ALL_MOVIES = "SELECT * FROM projects;"
# SELECT_UPCOMING_MOVIES = "SELECT * FROM projects WHERE release_timestamp > ?;" # number of seconds since 1st of January 1970 right now
# SELECT_WATCHED_MOVIES = "SELECT * FROM projects WHERE watched = 1;"
# SET_MOVIE_WATCHED = "UPDATE projects SET watched = 1 WHERE name = ?;"



# connection = sqlite3.connect("/data/data.db")
# need 4 slashes (https://docs.sqlalchemy.org/en/13/core/engines.html#sqlite)
engine = create_engine('sqlite:////data/data.db', echo=True, future=True)
Session = sessionmaker(engine)
import models

def create_tables():    
    print(engine)
    models.Base.metadata.create_all(engine)

def add_project(name:str):
    with Session.begin() as session:
        project = models.Project(name=name)
        session.add_all([project])

def get_projects(active:bool=True):

    
    session = Session()
    if active == True:
        column = getattr(models.Project, "active")
        stmt = select(models.Project).where(column == 1)
    else:
        stmt = select(models.Project)
    return session.scalars(stmt)


def activate_project(id:int):
    with engine.connect() as conn:
        stmt = update(models.Project).where(models.Project.c.id == id).values(active = 1)
        conn.execute(stmt)

