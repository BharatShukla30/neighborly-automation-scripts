import pymongo
import random
from bson.objectid import ObjectId

# Connect to the MongoDB server
client = pymongo.MongoClient(
    "mongodb+srv://neighborlysocialapp:cluster01@cluster0.cncxy2q.mongodb.net/")

# Access a specific database
db = client["Neighborly-production"]

# Access a specific collection (similar to a table in SQL)
collection = db["users"]

# Query all documents
results = collection.find()

# List of award types
awardTypes = ['Local Legend', 'Sunflower', 'Streetlight', 'Park Bench', 'Map']

# Iterate through the documents and print each one
for document in results:
    document_id = document['_id']
    flag = True
    for award in awardTypes:
        if document['awards'][award] != 0:
            flag = False
            break
    if flag:
        index = random.randrange(0,5)
        collection.update_one(
            {"_id": document_id},
            {"$inc": {"awards."+awardTypes[index]: 1}}
        )
        updated_doc = collection.find_one({"_id": ObjectId(document_id)})
        print(updated_doc)
