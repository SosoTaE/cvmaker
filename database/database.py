from pymongo import MongoClient
from configs.config import CONNECTION_STRING, DATABASE, USERS_COLLECTION, UNIVERSITY_COLLECTION, PROFESSION_COLLECTION

client = MongoClient(CONNECTION_STRING)

database = client.get_database(DATABASE)

# collection includes users information
usersCollection = database.get_collection(USERS_COLLECTION)
universityCollection = database.get_collection(UNIVERSITY_COLLECTION)
professionsCollection = database.get_collection(PROFESSION_COLLECTION)