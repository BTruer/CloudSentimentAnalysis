from pymongo import MongoClient
import json
from bson.json_util import dumps
import re
client = MongoClient('localhost', 27017)
db = client.twitter #twitter db
collection = db.twitter_collect
#print(collection.find({"_id":"joke"}).count())
cursor = collection.find({"_id":"apple"})
ret = dumps(cursor)
d = json.loads(ret)
data = d[0]['data']
puredata = ""
matched = re.match(r'(ScreenName=.*?,)|(Created=.*?,)|(Text=.*?, S)',data,re.M|re.I)
print(matched.group())
#cursor.pretty()
#print(ret)
#for document in cursor:
#    pprint(document)



#dbs = client.database_names()
#for db in dbs:
#    print(db)#
#    for col in client[db].collection_names():
#        print('\t', col)
#        for pag in client[db][col].find():
#            print(pag)
