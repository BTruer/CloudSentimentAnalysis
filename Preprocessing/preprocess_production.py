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
