import threading
import time
# import utils
# import pymongo  

# db_name,client=utils.get_db()  #for storing the database name and  instances 
# coll_name=utils.get_coll()     #for storing the collection name
# updval=list(coll_name.find())  #list of all documents

class createdata(threading.Thread):
    def run(self):
        try:
            for i in range(1,11):
                print(i)
            # for value in updval:
                #print(value)
                # i=value["_id"]
                # coll_name.update({"_id":i},{"$set":{"Location":"Bangalore"}})
                # print("Location updated")
                time.sleep(1)
        except Exception as err:
            print(err)

class createdatatwo(threading.Thread):
    def run(self):
        try:
            for i in range(10):
                print(i)
                time.sleep(1)
        except Exception as err:
            print(err)


    