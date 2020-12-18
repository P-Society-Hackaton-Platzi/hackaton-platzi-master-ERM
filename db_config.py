""" Data base conection config """

from flask_pymongo import pymongo
import os


DB_USER= os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@psociety-db.kg94a.mongodb.net/{DB_NAME}?retryWrites=true&w=majority")
db_users = client.users
db_technologies = client.technologies
db_questions = clients.questions
db_coments = clients.comments
