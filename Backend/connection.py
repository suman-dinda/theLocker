import pymongo
import json, pprint

class dbConnect:
    
    def connection(self, dbConfig):
        with open(dbConfig, 'r') as dbSettings:
            data = dbSettings.read()
        dbObject = json.loads(data)
        connectionArr = []
        connectionString = str(dbObject['connectionString'])
        dbName = str(dbObject['dbName'])
        mongoClient = pymongo.MongoClient(connectionString)
        connectionArr.append(dbName)
        connectionArr.append(mongoClient)
        return connectionArr


