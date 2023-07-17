from flask import Flask
from pymongo import MongoClient
from os import environ

app = Flask(__name__)

if app.config['TESTING']:
    client = MongoClient('mongodb://localhost:27017/test_deadlinebase')
else:
    client = MongoClient(environ.get("MONGO_URL"))

db = client.db_projects
