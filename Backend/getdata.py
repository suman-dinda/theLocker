from connection import dbConnect

conn = dbConnect.connection("connection","config/dbSettings.json")
dbObj = conn[1]
dbName = conn[0]
dblist = dbObj.list_database_names()
if dbName in dblist:
    print(dbObj.list_database_names())