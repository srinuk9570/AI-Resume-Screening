import pymongo
import pandas as pd
import json
import os

# Load MongoDB URL from environment variable instead of hardcoding
def getURL():
    return os.getenv("MONGO_URI")


def serializeJSON(json_data):
    result = {}

    for key in list(json_data.keys()):
        if isinstance(json_data[key], list):
            result[key] = "$".join(json_data[key])
        else:
            result[key] = str(json_data[key])

    return result


def connect():
    url = getURL()
    if url is None:
        raise ValueError("MongoDB URI not found. Set MONGO_URI environment variable.")
        
    myclient = pymongo.MongoClient(url)
    mydb = myclient["resume"]
    return mydb


def insertOne(mydb, data):
    mycol = mydb["resume"]

    data = serializeJSON(data)

    # insert_many expects list of documents
    if isinstance(data, dict):
        data = [data]

    result = mycol.insert_many(data)
    return result


def getAll(mycol):
    return mycol.find()


def getbyAtt(mycol, key, value):
    return mycol.find({key: value})