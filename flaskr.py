#all imports 
from contextlib import closing
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
	abort, render_template, flash

#configuration
DATABASE = 'tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'devkey'
USERNAME = 'admin'
PASSWORD = 'default'

#create application
app = Flask(__name__)
app.config.from_object(__name__)

#Connect to database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

#initialize and create database
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

#assures that database is connected for each request
@app.before_request
def before_request():
	g.db = connect_db()

#closes database at end of request
@app.teardown_request
def teardown_request(exception):
	db = getattr(g, 'db', None)
	if db is not None:
		db.close()

if __name__ == '__main__':
	app.run()