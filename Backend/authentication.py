from connection import dbConnect
import json

conn = dbConnect.connection("connection","config/dbSettings.json")
dbObj = conn[1]
dbName = conn[0]
dblist = dbObj.list_database_names()

class signup:
    def __init__(self,full_name,email,password):
        self.name = full_name
        self.email = email
        self.password = password
        signup.register(self)

    def register(self):
        if dbName in dblist:
            print(dbObj.list_database_names())
            res = {"email": self.email,"full_name": self.name}
            res = json.loads(res)
            return str(res)

class signin:
    def __init__(self,email,password):
        self.email = email
        self.password = password
        signin.login(self)

    def login(self):
        if dbName in dblist:
            print(dbObj.list_database_names())
            res = {
                "email": self.email,
                "password": self.password
            }
            
            return "res"
