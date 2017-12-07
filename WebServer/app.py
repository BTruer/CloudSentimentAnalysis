from flask import Flask, request
import os
import twitter
from pymongo import MongoClient

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


@app.route("/", methods=['GET'])
def index():
    return "working"

#take in a string and return the twitter data
@app.route("/search", methods=['GET'])
def search():
    query = request.args.get('query')
    data = getTheData(query)
    return str(data)

def getTheData(query):
    #if its in the db (been spark processed) get it from there
    
    #send the data to react
    #no go to twitter
    string_query = "q=%s&lang=en&locale=us&count=100" % query
    results = api.GetSearch(raw_query=string_query)
    #then send it to spark
    #sparkNN(twitter data)
    #get the result spark
    #send to react
    return results

if __name__ == '__main__':
    app.run(debug=True)
