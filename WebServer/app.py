from flask import Flask, request
import os
import twitter
app = Flask(__name__)
tck = os.environ['TWITTER_consumer_key']
tcs = os.environ['TWITTER_consumer_secret']
tatk = os.environ['TWITTER_access_token_key']
tats = os.environ['TWITTER_access_token_secret']
api = twitter.Api(consumer_key=tck,
                  consumer_secret=tcs,
                  access_token_key=tatk,
                  access_token_secret=tats)
print(api.VerifyCredentials())
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
    #if its in the db get it from there
    #no go to twitter
    return query

if __name__ == '__main__':
    app.run(debug=True)
