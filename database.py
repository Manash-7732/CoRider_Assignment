
from flask_pymongo import PyMongo
from pymongo import errors
from flask import current_app

mongo = PyMongo();

def init_db(app):
    mongo.init_app(app);
    try:
        mongo.cx.server_info()
        print("Connected to MongoDB Database");
    except errors.ConnectionFailure as error:
        print("Not connected to the Mongo DB", error);
