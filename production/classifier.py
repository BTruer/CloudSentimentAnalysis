from model import init_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import cPickle as pickle

from preprocess_production import preprocess
import itertools as it

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

model_file_name = "twitter_sentiment_analysis_model.model"
#sc = pyspark.SparkContext(appName="preprocessor")
company = "apple"
global t
global model


def get_dummy_data():
    data = preprocess(company)
    return data


'''
init the base keras model so that the analyse method may be called
'''
def init_classifier():
    global model
    global t
    model = init_model()
    model.load_weights(model_file_name)
    with open('tokenizer.pickle', 'rb') as handle:
        t = pickle.load(handle)
    

'''
    data: preprocessed twitter tweets
    company: company_name for graphing purposes
    return: sentiment graph based on data as plot.png
'''
def analyse(data, company):
    encoded_tweets = t.texts_to_sequences(data)
    padded_tweets = pad_sequences(encoded_tweets, maxlen=280, padding='post')
    result = model.predict(padded_tweets)
    result = list(it.chain.from_iterable(result))
    result = map(lambda x: float(x), result)
    average = float(np.average(result))
    line = [average for i in range(len(result))]
    figure = plt.figure()
    plt.bar(range(len(result)), result)
    plt.plot(range(len(result)), line, 'r' )
    red_patch = mpatches.Patch(color='red', label='Average')
    plt.legend(handles=[red_patch])
    plt.title("Overall Sentiment: " + company)
    figure.savefig('plot.png')
    return None
