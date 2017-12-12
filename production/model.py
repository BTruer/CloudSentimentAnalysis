import keras
from keras.layers import recurrent, LSTM, Dense, Embedding, Conv1D, MaxPooling1D
from keras.models import Sequential



number_inputs = 250
learning_rate = 10e-3
epochs = 10
vocabulary_size = 10000

#, trainable=False
def init_model():
    model = Sequential()
    model.add(Embedding(vocabulary_size, 280, input_length=280))
    model.add(Conv1D(64,10, activation='relu'))
    model.add(MaxPooling1D(pool_size=9))
    model.add(LSTM(128, activation='tanh', recurrent_activation='hard_sigmoid', use_bias=True, kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros', unit_forget_bias=True, kernel_regularizer=None, recurrent_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, recurrent_constraint=None, bias_constraint=None, dropout=0.0, recurrent_dropout=0.0, implementation=1, return_sequences=False, return_state=False, go_backwards=False, stateful=False, unroll=False))
    #model.add( LSTM(128, activation='tanh', recurrent_activation='hard_sigmoid', use_bias=True, kernel_initializer='glorot_uniform', recurrent_initializer='orthogonal', bias_initializer='zeros', unit_forget_bias=True, kernel_regularizer=None, recurrent_regularizer=None, bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, recurrent_constraint=None, bias_constraint=None, dropout=0.0, recurrent_dropout=0.0, implementation=1, return_sequences=False, return_state=False, go_backwards=False, stateful=False, unroll=False) )
    model.add(Dense(32, activation="linear"))
    model.add(Dense(1, activation="sigmoid"))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
    model.summary()
    return model

def main():
    model = init_model()
    from keras.utils import plot_model
    #plot_model(model, to_file='model.png', show_shapes=True)

if __name__ == '__main__':
    main()
