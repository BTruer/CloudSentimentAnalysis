from model import init_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import os
import numpy as np
import cPickle as pickle
import csv
import re
from elephas.utils.rdd_utils import to_simple_rdd
from elephas.spark_model import SparkModel
from elephas import optimizers as elephas_optimizers
import pyspark 


model_file_name = "twitter_sentiment_analysis_model.model"
sc = pyspark.SparkContext(appName="Neural Network")


def strip_data(tweet):
    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r"#\S+", "", tweet)
    tweet = re.sub(r"@\S+", "", tweet)
    return tweet



'''
    Load a dataset of raw tweets into memory, preprocess them, and then start training the model 
    in a distributed way.
    Elephas allows distributed training of keras models on a cluster which saves time
'''
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
    adagrad = elephas_optimizers.Adagrad()
    spark_model = SparkModel(sc,model, optimizer=adagrad, frequency='epoch', mode='asynchronous', num_workers=4)
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
                if(len( tweets_list ) >= 300000 ):
                    encoded_tweets = t.texts_to_sequences(tweets_list)
                    padded_docs = pad_sequences(encoded_tweets, maxlen=280, padding='post')
                    rdd = to_simple_rdd(sc, padded_docs, tweets_labels)
                    spark_model.train(rdd, nb_epoch=7, batch_size=512, verbose=0)
                    #model.fit(padded_docs, tweets_labels, epochs=7, verbose=1, batch_size=512)
                    trained_data += 300000
                    model.save(model_file_name)
                    print "%d k tweets trained!" % (trained_data / 1000)
                    tweets_labels = []
                    tweets_list = []
    model.save(model_file_name)



if __name__ == '__main__':
    main()
