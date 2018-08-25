#!flask/bin/python
import os, datetime, time, requests
from flask import Flask, jsonify, abort, make_response, request, render_template
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object('config')
app.config['ASK_VERIFY_REQUESTS'] = False
app.secret_key = 'super secret key'
db = SQLAlchemy(app)
admin = Admin(app, url="/admin")
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    done = db.Column(db.Boolean, unique=False)
    
    def __repr__(self):
        return "<Tasks({})>".format(self.title)
        
class Tasks_day(db.Model):
    __tablename__ = 'tasks_day'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200))
    hours = db.Column(db.Integer)
    # done = db.Column(db.Boolean, unique=False)
    
    # def __repr__(self):
    #     return "<Tasks({})>".format(self.title)

class Private(db.Model):
    __tablename__ = 'private'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fullAddressEn = db.Column(db.String(200))
    latitude = db.Column(db.String(200))
    longitude = db.Column(db.String(200))


admin.add_view(ModelView(Tasks, db.session))
admin.add_view(ModelView(Tasks_day, db.session))
admin.add_view(ModelView(Private, db.session))

from views import *


if __name__ == '__main__':
    manager.run()