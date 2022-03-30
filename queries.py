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

def query_db(query, args=(), one=False, select=True):
    '''fetch data from the database'''
    cur = get_db().execute(query, args)
    if select:
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv
    else:
        cur.close()
        return
       
# make, get, update and delete user

def make_user(name, password, sex, kg, cm, age, activity):
    '''Create user in the database'''
    reg_date = # TODO date function
    password = # TODO hash
    target = 500 # change later?
    query = '''INSERT INTO users 
(name, password, reg_date, sex, kg, cm, age, activity, target)
values (?,?,?,?,?,?,?,?,?)'''
    query_db(query, (name, password, reg_date, sex, kg, cm, age, activity, target),
             False, False)

def get_user():
    pass

def update_user():
    pass

def delete_user():
    pass

# update weight

# log calories
