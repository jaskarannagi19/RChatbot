#!/usr/local/bin/python3
import nltk, csv, numpy, sys, classifier
import largerNeuralNetwork as lNetwork
from keras.utils import np_utils as nUtilities
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential
from keras.layers import Input, Activation, Dense, Dropout, LSTM, Embedding, add

# ==============================================================================================
# ==============================================================================================
# A MUCH SIMPLER MODEL FOR PROCESSING SMALLER DATASETS (INCLUDING THE NLTK DATA) AND USER INPUTS

# GET THE DATA/TEXT 
with open("MontyPython.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines] 

# NOISE REMOVAL
tempLines = []
for i in range(len(lines)):
    if not lines[i].startswith('['): #get rid of any lines that only provide descriptions
        if ":" in lines[i]:
            startIndex = lines[i].index(":")+1 #remove the character names to improve prediction accuracy
        else:
            startIndex = 0
        tempLines.append(lines[i][startIndex:])

lines = tempLines
# [print(lines[i], end ="\n") for i in range(len(lines))]

monty = ",".join(lines)
# print(monty)

# Split the data into training and testing
trainingSize = int(len(monty) * 0.7)
trainingSents = monty[:trainingSize]
testSents = monty[trainingSize:]


# Sort the data and convert the words in the vocabulary into numbers for use by the model
vocab = sorted(set(trainingSents))
vectorizedMonty = dict((i, v) for v, i in enumerate(vocab))
trainingLength = len(trainingSents) 
vocabLen = len(vocab) 
sequenceLength = 50 
# print ("Total number of characters in sequence:", trainingLength)
# print ("Total vocabulary:", vocabLen)

inputData, inputLabels = [], []
loopCount = trainingLength - sequenceLength

# Generate a range of sequences (based on the sequenceLength variable) to use for 
# classifying the text. The sequence length defines the number of words that will be 
# considered in context with each other when analysing the data and building the model

for i in range(0, loopCount):
    # For each iteration, create new input and output sequences 
    # (The higher the value of sequenceLength, the more accurate the model is
    # but also the more time and processing power required to fit the model
    inputSequence = trainingSents[i:i + sequenceLength]
    outputSequence = trainingSents[i + sequenceLength]

    # Convert the words and input labels in the sequences into numbers 
    inputData.append([vectorizedMonty[char] for char in inputSequence])
    inputLabels.append(vectorizedMonty[outputSequence])

''' Alternatively, use the vectorizer method from the larger neural network to perform the above operation'''
# inSequence, outSequence, inputData, inputLabels = lNetwork.vectorizer(processedMonty, sequenceLength, processedMonty)



# After generating the sequences, use numpy to reshape the data
# and convert the values into floats/decimals and then perform 'one-hot encoding' 
# on the data in the event that a bag-of-words is used for text classification
values = numpy.reshape(inputData, (len(inputData), sequenceLength, 1))
values = values/float(vocabLen)
valueLabels = nUtilities.to_categorical(inputLabels) 


# BUILDING AND FITTING THE MODEL ON THE TRAINING DATA
model = Sequential()

# The input layer
model.add(LSTM(256, input_shape=(values.shape[1], values.shape[2]), return_sequences=True))

# Add a series of hidden layers with dropout

# After testing with different values, 0.3 seems to be the 
# optimal trade-off value (in terms of the time spent training the model and accuaracy) for dropout
model.add(Dropout(0.3))  
model.add(LSTM(256, return_sequences=True))

# model.add(Embedding(input_dim=montyLength, output_dim=100)) #reduces accuracy 

model.add(Dropout(0.3))
model.add(LSTM(256))

model.add(Dropout(0.3))
model.add(Dense(valueLabels.shape[1], activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')


# filename = "montyWeights4Epochs.hdf5"
filename = "montyWeights10Epochs.hdf5"

# Add a checkpoint to prevent data loss in the event that the training process is interrupted
# and training data is lost
checkpoint = ModelCheckpoint(filename, monitor='loss', verbose=1, save_best_only=True, mode='min')


""" Fit/train the model against the training data and save it to prevent having to fit the
model everytime it is used. The higher the number of epochs/batch size, the more accurate the model
but there is also a trade-off between number of epochs/accuracy and the time it takes to train the model
"""
# model.fit(values, valueLabels, epochs=10, batch_size=256, callbacks=[checkpoint])
# model.save(filename)

# Load the model to prepare it for prediction
model = lNetwork.loadModel(model, filename)
reverseVectorized = dict((i, v) for i, v in enumerate(vocab))

# # PREDICTING TEXT AND PROVIDING RESPONSES FOR THE CHATBOT
def provideResponse(userInput):
    response = ""
    for i in range (len(userInput) * 2):
        # Convert the user's sentence into an array and predict the response
        # follow this up by re-converting the predicted numbers back into words
        userArray = numpy.reshape(userInput, (1, len(userInput)-1, 1))
        userArray = userArray / float(vocabLen)
        prediction = model.predict(userArray, verbose=0)

        index = numpy.argmax(prediction)
        characters = reverseVectorized[index]
        reversedSequence = [reverseVectorized[char] for char in userInput]

        response.join(reversedSequence)

    return response


# ALTERNATIVE (FOR IMPROVING ACCURACY)
# USING THE CLASSIFIER TO DETERMINE WHAT KIND OF RESPONSE TO PROVIDE TO THE USER
# nbPredictions = classifier.nbClassify(trainingData, categories, testingData)
# svmPredictions = classifier.svmClassify(trainingData, categories, testingData)
