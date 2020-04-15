#!/usr/local/bin/python3
import numpy, sys
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint


file = open("84-0.txt").read()

def tokenize_words(input):
    # convert everything to lowercase to standardize it
    input = input.lower()

    # instantiate the tokenizer
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(input)

    # if the created token isn't in the stop words, make it part of "filtered"
    filtered = filter(lambda token: token not in stopwords.words('english'), tokens)
    return " ".join(filtered)

processed_inputs = tokenize_words(file)

"""
A neural network works with numbers, not text characters. 
So we'll need to convert the characters in our input to numbers. 
We'll sort the list of the set of all characters that appear in our input text, 
then use the enumerate function to get numbers which represent the characters. 
We then create a dictionary that stores the keys and values, 
or the characters and the numbers that represent them:"""

chars = sorted(list(set(processed_inputs)))
char_to_num = dict((c, i) for i, c in enumerate(chars))


input_len = len(processed_inputs) #100581
vocab_len = len(chars) #42
# print ("Total number of characters:", input_len)
# print ("Total vocab:", vocab_len)


# print(char_to_num)
seq_length = 100
x_data = []
y_data = []


# loop through inputs, start at the beginning and go until we hit
# the final character we can create a sequence out of
for i in range(0, input_len - seq_length, 1):
    # Define input and output sequences
    # Input is the current character plus desired sequence length
    in_seq = processed_inputs[i:i + seq_length]

    # Out sequence is the initial character plus total sequence length
    out_seq = processed_inputs[i + seq_length]

    # We now convert list of characters to integers based on
    # previously and add the values to our lists
    x_data.append([char_to_num[char] for char in in_seq])
    y_data.append(char_to_num[out_seq])


n_patterns = len(x_data) #100481

"""
Now we'll go ahead and convert our input sequences into a processed numpy array that our network can use. 
We'll also need to convert the numpy array values into floats so that the sigmoid activation function our 
network uses can interpret them and output probabilities from 0 to 1:"""
X = numpy.reshape(x_data, (n_patterns, seq_length, 1))
X = X/float(vocab_len)

# We'll now one-hot encode our label data:

y = np_utils.to_categorical(y_data)

"""Since our features and labels are now ready for the network to use, 
let's go ahead and create our LSTM model. 
We specify the kind of model we want to make (a sequential one), and then add our first layer.

We'll do dropout to prevent overfitting, followed by another layer or two. 
Then we'll add the final layer, a densely connected layer that will output 
a probability about what the next character in the sequence will be:
"""
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

# filepath = "model_weights_saved.hdf5"
# checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
# desired_callbacks = [checkpoint]


# # """Now we'll fit the model and let it train."""
# model.fit(X, y, epochs=4, batch_size=256, callbacks=desired_callbacks)

"""After it has finished training, we'll specify the file name and load in the weights. 
Then recompile our model with the saved weights:"""
filename = "reverseVectorized.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')




"""
Since we converted the characters to numbers earlier, 
we need to define a dictionary variable that will convert the output of the model back into numbers:
"""
num_to_char = dict((i, c) for i, c in enumerate(chars))

"""To generate characters, we need to provide our trained model with a 
random seed character that it can generate a sequence of characters from:"""
start = numpy.random.randint(0, len(x_data) - 1)
pattern = x_data[start]
print("Random Seed:")
print("\"", ''.join([num_to_char[value] for value in pattern]), "\"")


"""Now to finally generate text, we're going to iterate through our chosen number of characters and convert our input (the random seed) into float values.
We'll ask the model to predict what comes next based off of the random seed, convert the output numbers to characters and then append it to the pattern, 
which is our list of generated characters plus the initial seed:"""

for i in range(1000):
    x = numpy.reshape(pattern, (1, len(pattern), 1))
    x = x / float(vocab_len)
    prediction = model.predict(x, verbose=0)
    index = numpy.argmax(prediction)
    result = num_to_char[index]
    seq_in = [num_to_char[value] for value in pattern]

    sys.stdout.write(result)

    pattern.append(index)
    pattern = pattern[1:len(pattern)]

