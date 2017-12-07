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
print(api.VerifyCredentials())
print()
print()
results = api.GetSearch(raw_query="q=apple&lang=en&locale=us&count=100") # apple
print()
print()
results = api.GetSearch(raw_query="q=%40apple&lang=en&locale=us&count=100") #  @apple
print()
print()
results = api.GetSearch(raw_query="q=%23apple&lang=en&locale=us&count=100") # #apple
print(results)
