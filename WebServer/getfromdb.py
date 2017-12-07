from pymongo import MongoClient
from pprint import pprint
client = MongoClient('localhost', 27017)
db = client.twitter #twitter db
collection = db.twitter_collect
cursor = collection.find({"_id":"apple"})
for document in cursor:
    pprint(document)
