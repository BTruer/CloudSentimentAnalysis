from model import init_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import os
import numpy as np
import cPickle as pickle
import csv
import re



model_file_name = "twitter_sentiment_analysis_model.model"
def strip_data(tweet):
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r"#\S+", "", tweet)
    tweet = re.sub(r"@\S+", "", tweet)
    return tweet

def main():
    model = init_model()
    max_tweet_length = 280
    with open('tokenizer.pickle', 'rb') as handle:
        t = pickle.load(handle)
    # vocab_size = len(t.word_index) + 1

    tweets_list = []
    tweets_labels = []
    i=0
    trained_data = 0
    with open("Sentiment Analysis Dataset.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if i == 0:
                    header = row
                    i += 1
                else:
                    # i += 1
                    data = strip_data(row[3].decode('utf-8'))
                    data = data.encode('ascii', 'ignore')
                    tweets_labels.append( row[1] )
                    #print data
                    tweets_list.append(data)
                if(len( tweets_list ) >= 100000 ):
                    encoded_tweets = t.texts_to_sequences(tweets_list)
                    padded_docs = pad_sequences(encoded_tweets, maxlen=280, padding='post')
                    model.fit(padded_docs, tweets_labels, epochs=7, verbose=1, batch_size=512)
                    trained_data += 100000
                    model.save(model_file_name)
                    print "%d k tweets trained!" % (trained_data / 1000)
                    tweets_labels = []
                    tweets_list = []
    # evaluate the model
    #a = model.evaluate(padded_docs, labels, verbose=0)
    model.save(model_file_name)
    test_tweets = ['I love using apple products', 'i hate iPhones', 'the sentiment analysis better work']
    encoded_tweets = t.texts_to_sequences(test_tweets)
    padded_tweets = pad_sequences(encoded_tweets, maxlen=280, padding='post')
    a = model.predict( padded_tweets )
    print(np.round(a))


if __name__ == '__main__':
    main()
