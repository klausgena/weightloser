# queries.py assures the interaction with the database

# initialise and manage the database connection
# (https://flask.palletsprojects.com/en/2.0.x/patterns/sqlite3/)

import sqlite3
from flask import g

DATABASE = 'db/weightloser.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
        
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Query functions for get, update, delete, make

def query_db(query, args=(), one=False):
    "fetch data from the database"
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
       
# make, get, update and delete user

def make_user():
    pass

def get_user():
    pass

def update_user():
    pass

def delete_user():
    pass

# update weight

# log calories
