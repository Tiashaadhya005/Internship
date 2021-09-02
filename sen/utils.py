from pymongo import MongoClient
from .config import USERNAME,PASSWORD

#client=MongoClient('localhost', 27017)
#uri = "mongodb://127.0.0.1:27017"
uri =f"mongodb://{USERNAME}:{PASSWORD}@0.0.0.0:27017"
#client = MongoClient("mongodb://root:rootpassword@localhost:27017") 
client= MongoClient(uri)
mydb=client['myproject']

def get_db():
    return mydb, client

def get_coll():
    c='firstcollect'
    return mydb[c]