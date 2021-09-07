from pymongo import MongoClient

uri ="mongodb://mongo/myproject"
client= MongoClient(uri)

mydb=client['myproject']

def get_db():
    return mydb, client

def get_coll():
    c='firstcollect'
    return mydb[c]
