import csv
import keras
import re
import cPickle as pickle
from keras.preprocessing.text import Tokenizer

t = Tokenizer(filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True)
max_tweet_length = 280

def remove_urls(tweet):
    return re.sub(r"http\S+", "", tweet)

def preprocess():
    i = 0
    header = ""

    tweets_list = []
    tweets_labels = []

    with open("Sentiment Analysis Dataset.csv", 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            if i == 0:
                header = row
                i += 1
            else:
                # i += 1
                tweets_list.append(remove_urls(row[3]))
    return tweets_list
                    
t.fit_on_texts(preprocess())

# saving
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(t, handle, protocol=pickle.HIGHEST_PROTOCOL)


