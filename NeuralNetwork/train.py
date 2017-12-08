from model import init_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import os
import numpy as np

model = init_model()
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # to disable tensorflow debugging. It gets rather annoying
docs = ['Well done!',
		'Good work',
		'Great effort',
		'nice work',
		'Excellent!',
		'Weak',
		'Poor effort!',
		'not good',
		'poor work',
		'Could have done better.',
		'I hate you',
		'I love you']
labels = [1,1,1,1,1,0,0,0,0,0, 0, 1]
t = Tokenizer()
t.fit_on_texts(docs)
vocab_size = len(t.word_index) + 1
encoded_docs = t.texts_to_sequences(docs)
max_length = 4
padded_docs = pad_sequences(encoded_docs, maxlen=max_length, padding='post')



test_doc = ['I totally love it', "you're so annoying hate"]
encode = t.texts_to_sequences(test_doc)
pad = pad_sequences(encode, maxlen=max_length, padding='post')
model.fit(padded_docs, labels, epochs=100, verbose=0)
# evaluate the model
#a = model.evaluate(padded_docs, labels, verbose=0)
a = model.predict( pad )
print(np.round(a))

print()