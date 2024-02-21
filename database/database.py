from pymongo import MongoClient
from configs.config import CONNECTION_STRING, DATABASE, USERS_COLLECTION

client = MongoClient(CONNECTION_STRING)

database = client.get_database(DATABASE)

# collection includes users information
usersCollection = database.get_collection(USERS_COLLECTION)