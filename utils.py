from pymongo import MongoClient

client=MongoClient('localhost', 27017)
mydb=client['myproject']

def get_db():
    #client=MongoClient('localhost', 27017)
    #mydb= client['myproject']
    #mycoll=mydb['collections']
    #print(client)
    return mydb, client

def get_coll():
    c='firstcollect'
    return mydb[c]