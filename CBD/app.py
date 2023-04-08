from pymongo import MongoClient

connection_string= "mongodb://localhost:27017/"
client = MongoClient()
print(client.list_database_names())