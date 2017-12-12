from flask import Flask, request, render_template
import os
import twitter
from pymongo import MongoClient
from bson.json_util import dumps
from preprocess_production import preprocess
from classifier import analyse, init_classifier
#make sure all dependences are installed before moving on
app = Flask(__name__)
#get from the enviroment all twitter required keys
tck = os.environ['TWITTER_consumer_key']
tcs = os.environ['TWITTER_consumer_secret']
tatk = os.environ['TWITTER_access_token_key']
tats = os.environ['TWITTER_access_token_secret']
api = twitter.Api(consumer_key=tck,
                  consumer_secret=tcs,
                  access_token_key=tatk,
                  access_token_secret=tats)
#use this print statement to check if you have successfully linked your twitter keys to this application
#print(api.VerifyCredentials())
init_classifier()
#look for mongo db on this machine localhost at port 27017
client = MongoClient('localhost', 27017)
db = client.twitter #twitter db
collection = db.twitter_collect #twitters data collection
collection2 = db.nn_data #sparks post processed data that is ready for the neural net

#load the search page
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

#take in a string and return the twitter data
@app.route("/search", methods=['POST'])
def search():
    query = request.form['query']
    #get the twitter data
    data = getTwitterData(query)
    #write the data to the file
    file = open("preproc",'w')
    file.write(data)
    file.close()
    #let the preprocessor process the file
    proc_data = preprocess("preproc")
    #send it to the neural net and wait
    done = analyse(proc_data, query)
    return render_template('result.html')



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
