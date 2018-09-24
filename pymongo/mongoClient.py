import pymongo

def showDatabases(client):
    # Show databases
    print(client.database_names())

def checkIfDatabaseExist(client,databaseName):
    databaseNames = client.database_names()
    if databaseName in databaseNames:
        print('The database exists.')
    else:
        print('The database doesn\'t exists.')

def showCollections(database):
    collections = database.list_collection_names()
    return collections

def checkIfCollectionExist(database, collection):
    collections = database.list_collection_names()
    if collection in collections:
        print("The collection exists.")
    else:
        print('The collection doesn\'t exists.')

def insert(collection,payload):
    x = collection.insert_one(payload)
    return x

def insertBulk(collection,payload):
    x = collection.insert_many(payload)
    return x

def showTable(collection):
    for element in collection.find():
        print(element)

# only show fields with name and address, but NO _id
def showTableWithoutID(collection):
    for element in collection.find({},{ "_id": 0, "name": 1, "address": 1 }):
        print(element)

def excludeElement(collection,payload):
    queryResult = collection.find({},payload)
    for element in queryResult:
        print(element)


def query(collection, payload):
    queryResult = collection.find(payload)
    for element in queryResult:
        print(element)
    # return elements

def queryRegex(collection, payload):
    queryResult = collection.find(payload)
    for element in queryResult:
        print(element)
    # return elements

def queryRegexExample(collection):
    payload = { "address": { "$regex": "^S" } }
    queryResult = collection.find(payload)
    for element in queryResult:
        print(element)
    # return queryResult

def querySort(collection, field):
    queryResult = collection.find().sort(field)
    for element in queryResult:
        print(element)
    # return queryResult

def querySortAscending(collection, field):
    queryResult = collection.find().sort(field, 1)
    for element in queryResult:
        print(element)
    # return queryResult

def querySortDescending(collection, field):
    queryResult = collection.find().sort(field, -1)
    for element in queryResult:
        print(element)
    # return queryResult

def deleteElement(collection, payload):
    collection.delete_one(payload)

# with regex or id, payloa = { "address": {"$regex": "^S"} }
def deleteElements(collection, payload):
    queryResult = collection.delete_many(payload)
    print(queryResult.delete_count, ' documents deleted')

def deleteAll(collection):
    queryResult = collection.delete_many({})
    print(queryResult.delete_count, ' documents deleted')

def deleteCollection(collection):
    collection.drop()

def deleteTable(table):
    table.drop()

def update(collection, payload, updatePayload):
    queryResult = collection.update(payload, updatePayload)
    # return queryResult

def updateBulk(collection, payload, updatePayload):
    queryResult = collection.update_many(payload, updatePayload)
    print(queryResult.modified_count, ' documents updated.')
    # return queryResult

def queryLimit(collection, payload, limit):
    queryResult = collection.find(payload).limit(limit)
    # return queryResult

if __name__ == "__main__":
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["myDatabase"]
    collection = mydb["collection"]
    showTableWithoutID(collection)
    showTable(collection)
    # payload = {
    #     'name': "Jose Luis",
    #     'lastName':"Alonzo Velazquez",
    #     'edad': "34"
    # }
    #
    # insert(collection, payload)
else:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["myDatabase"]
    collection = mydb["collection"]
    payload = [
    {
        'name': "Nombre 1",
        'lastName':"Apellido 1",
        'edad': "34"
    },
    {
        'name': "Nombre 2",
        'lastName':"Apellido 2",
        'edad': "34"
    },
    {
        'name': "Nombre 3",
        'lastName':"Apellido 3",
        'edad': "34"
    },
    {
        'name': "Nombre 4",
        'lastName':"Apellido 4",
        'edad': "34"
    },
    {
        'name': "Nombre 5",
        'lastName':"Apellido 5",
        'edad': "34"
    },
    {
        'name': "Nombre 6",
        'lastName':"Apellido 6",
        'edad': "34"
    },
    {
        'name': "Nombre 7",
        'lastName':"Apellido 7",
        'edad': "34"
    },
    ]
    mylist = [
      { "_id": 1, "name": "John", "address": "Highway 37"},
      { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
      { "_id": 3, "name": "Amy", "address": "Apple st 652"},
      { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
      { "_id": 5, "name": "Michael", "address": "Valley 345"},
      { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
      { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
      { "_id": 8, "name": "Richard", "address": "Sky st 331"},
      { "_id": 9, "name": "Susan", "address": "One way 98"},
      { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
      { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
      { "_id": 12, "name": "William", "address": "Central st 954"},
      { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
      { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
    ]
    print('This is not a library')
