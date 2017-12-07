from pymongo import MongoClient
from pprint import pprint
from bson.json_util import dumps
client = MongoClient('localhost', 27017)
db = client.twitter #twitter db
collection = db.twitter_collect
#print(collection.find({"_id":"joke"}).count())
cursor = collection.find({"_id":"apple"})
ret = dumps(cursor)
print(ret)
#for document in cursor:
#    pprint(document)
