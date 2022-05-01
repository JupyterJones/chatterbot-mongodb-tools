from os.path import join
import pymongo
from bson.json_util import dumps

def backup_db(backup_db_dir):
    client = pymongo.MongoClient(host="mongodb://localhost", port=27017)
    database = client["super-chatbot"]
    collections = database.list_collection_names()

    for i, collection_name in enumerate(collections):
        col = getattr(database,collections[i])
        collection = col.find()
        jsonpath = collection_name + ".json"
        jsonpath = join(backup_db_dir, jsonpath)
        with open(jsonpath, 'wb') as jsonfile:
            jsonfile.write(dumps(collection).encode())


backup_db('./superchatbackup')
