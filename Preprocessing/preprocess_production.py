'''
Preprocessing twitter API queries live using PySpark.
'''

import csv
import keras
import pyspark
import numpy as np
from pyspark.sql import SparkSession
from keras.preprocessing.text import Tokenizer
#from pyspark.ml.feature import NGram
import re
import cPickle as pickle
from pyspark.sql import SQLContext
from pyspark.sql import Row

sc = pyspark.SparkContext(appName="preprocessor")
ss = SparkSession(sc)
sqlContext = SQLContext(sc)

def preprocess(filename):

    def remove_urls(tweet):
	    return re.sub(r"http\S+", "", tweet)

    import ast

    def parse(s):
	    tuples = s.split('), ')
	    out = []
	    for x in tuples:
	
	    # print(x)
	    # a, b, c, d = x.strip('(').split(',', 3).strip("(")
	        a = x.strip("(").strip(")").split(',', 3)# x.strip("(").split(',', 3))  # ((int(a), str(b), str(c), str(d)))
	    return a

    # jdf = ss.read.json("../WebServer/sampledata_apple").rdd.map(list)
    jdf = ss.read.json("../WebServer/"+filename).rdd.map(list)
    twitter_data = jdf.map(lambda l: l[1].encode("utf-8").replace("Status", ""))

    clean_data = twitter_data.map(lambda l: l.replace("[", "").replace("]", ""))
    clean_data = clean_data.map(remove_urls).map(lambda l: re.sub(r"@\S+", "", l))
    clean_data = clean_data.map(lambda l: re.sub(r"#\S+", "", l))
    # print(clean_data.first())
    # cleaner_data = clean_data.map(parse)
    flat_data = clean_data.flatMap(lambda l: l.split("),"))
    flat_data = flat_data.map(lambda l: l+")")
    flat_data = flat_data.map(lambda l: l.replace("ID=", "").replace("ScreenName=","").replace("Created=","").replace("Text=",""))
    flat_data = flat_data.map(lambda l: parse(str(l)))

    return_data = flat_data.map(lambda l: str(l[3]))

    return return_data.collect()


       
preprocess()


