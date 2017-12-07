from pymongo import MongoClient
import twitter
import os



tck = os.environ['TWITTER_consumer_key']
tcs = os.environ['TWITTER_consumer_secret']
tatk = os.environ['TWITTER_access_token_key']
tats = os.environ['TWITTER_access_token_secret']
api = twitter.Api(consumer_key=tck,
                  consumer_secret=tcs,
                  access_token_key=tatk,
                  access_token_secret=tats)
query = "apple"
string_query = "q=%s&lang=en&locale=us&count=100" % query
results1 = api.GetSearch(raw_query=string_query)
string_query = "q=%40%%s&lang=en&locale=us&count=100" % query
results2 = api.GetSearch(raw_query=string_query)
string_query = "q=%23%%s&lang=en&locale=us&count=100" % query
results3 = api.GetSearch(raw_query=string_query)
results = str(results1) + "," + str(results2) + "," + str(results3)
data1 = str(results)


#results1 = api.GetSearch(raw_query="q=apple&lang=en&locale=us&count=100")
#results2 = api.GetSearch(raw_query="q=%40apple&lang=en&locale=us&count=100") #  @apple
#results3 = results = api.GetSearch(raw_query="q=%23apple&lang=en&locale=us&count=100") # #apple
#results = str(results1) + "," + str(results2) + "," + str(results3)
#data1 = str(results)

#results1 = api.GetSearch(raw_query="q=tesla&lang=en&locale=us&count=100")
#results2 = api.GetSearch(raw_query="q=%40tesla&lang=en&locale=us&count=100") #  @apple
#results3 = results = api.GetSearch(raw_query="q=%23tesla&lang=en&locale=us&count=100") # #apple
#results = str(results1) + "," + str(results2) + "," + str(results3)
#data2 = str(results)

#results1 = api.GetSearch(raw_query="q=adp&lang=en&locale=us&count=100")
#results2 = api.GetSearch(raw_query="q=%40adp&lang=en&locale=us&count=100") #  @apple
#results3 = results = api.GetSearch(raw_query="q=%23adp&lang=en&locale=us&count=100") # #apple
#results = str(results1) + "," + str(results2) + "," + str(results3)
#data3 = str(results)


client = MongoClient('localhost', 27017)
db = client.twitter #twitter db
db.twitter_collect.drop()
collection = db.twitter_collect
#db.products.insert( { _id: 10, item: "box", qty: 20 } )
collection.insert({"_id":"apple", "data":data1})
#collection.insert({"_id":"tesla", "data":data2})
#collection.insert({"_id":"adp", "data":data3})
