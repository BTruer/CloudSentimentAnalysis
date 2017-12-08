'''
Distributed preprocessing of csv file using Spark RDDs
'''


import csv
import keras
import pyspark
import numpy as np
from pyspark.sql import SparkSession
from keras.preprocessing.text 
import Tokenizer
import re
import cPickle as pickle

sc = pyspark.SparkContext(appName="preprocessor")
ss = SparkSession(sc)

def preprocess_csv()

    with open('tokenizer.pickle', 'rb') as handle:
        t = pickle.load(handle)
    
    max_tweet_length = 280
    vocab_size = len(t.word_index)

    def get_tweets(row):
        return row[3]

    def remove_urls(tweet):
        return re.sub(r"http\S+", "", tweet)

    rdd = ss.read.csv("Sentiment Analysis Dataset.csv").rdd.map(list)
    # header = rdd.first()
    rdd = rdd.filter(lambda line: line != header)
    tweets_rdd = rdd.map(lambda line: get_tweets(line).encode('utf-8'))
    tweets_rdd = tweets_rdd.map(lambda line: remove_urls(line).lstrip(' '))
    # tweets_rdd.first()

    digits_rdd = tweets_rdd.map(lambda line: t.texts_to_sequences([line]))

    def pad(seq):
        return pad_sequences(seq, maxlen=max_tweet_length, padding='post')

    padded_rdd = digits_rdd.map(lambda line: pad(line))

    return padded_rdd.collect()

     

    


