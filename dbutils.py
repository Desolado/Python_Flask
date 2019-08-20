from pymongo import MongoClient

MONGO_URL = "mongodb+srv://admin:admin@cluster0-oqrr8.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(MONGO_URL)

def db_connect(MONGO_URI, db_name, col_name):
    client = MongoClient(MONGO_URI)
    database = client[db_name]
    collection = database[col_name]
    return collection

def db_insert_user(collection, user):
    return collection.insert_one(user)

def db_find_all(collection, query={}):
    return collection.find(query)


if __name__ == '__main__':
    print("MongoClient imported successfully!")

    database = client["mi_app"]

    users = database["users"]

    usuario_demo = {
        "user": "Eduardo P",
        "email": "eperezc37@gmail.com"
    }

    users.insert_one(usuario_demo)