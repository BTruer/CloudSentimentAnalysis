from flask import Flask, request
import os
import twitter
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

tck = os.environ['TWITTER_consumer_key']
tcs = os.environ['TWITTER_consumer_secret']
tatk = os.environ['TWITTER_access_token_key']
tats = os.environ['TWITTER_access_token_secret']
api = twitter.Api(consumer_key=tck,
                  consumer_secret=tcs,
                  access_token_key=tatk,
                  access_token_secret=tats)
#print(api.VerifyCredentials())
client = MongoClient('localhost', 27017)
db = client.twitter #twitter db
collection = db.twitter_collect

@app.route("/", methods=['GET'])
def index():
    return "working"

#take in a string and return the twitter data
@app.route("/search", methods=['GET'])
def search():
    query = request.args.get('query')
    #get the twitter data
    data = getTwitterData(query)
    #send the twitter data to the neural net
    return data

def getTwitterData(query):
    #if twitter data is in db
    if(collection.find({"_id":query}).count()>0):
        return dumps(collection.find({"_id":query}))
    #no go to twitter
    at = "%40"
    hashtag = "%23"
    query2 = at+query
    query3 = hashtag+query
    string_query = "q=%s&lang=en&locale=us&count=100" % query
    results1 = api.GetSearch(raw_query=string_query)
    string_query = "q=%s&lang=en&locale=us&count=100" % query2
    results2 = api.GetSearch(raw_query=string_query)
    string_query = "q=%s&lang=en&locale=us&count=100" % query3
    results3 = api.GetSearch(raw_query=string_query)
    results = str(results1) + "," + str(results2) + "," + str(results3)
    data = str(results)
    #store to db
    collection.insert({"_id":query, "data":data})
    #get from db and return
    return dumps(collection.find({"_id":query}))


if __name__ == '__main__':
    app.run(debug=True)
