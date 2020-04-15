#!/usr/local/bin/python3
import sys, re, tarfile, nltk, numpy 
from keras.models import Sequential, Model
from keras.layers.embeddings import Embedding
from keras.layers import Input, Activation, Dense, Permute, Dropout, LSTM, add, dot, concatenate
from keras.utils.data_utils import get_file
from keras.preprocessing.sequence import pad_sequences
from functools import reduce

def tokenize(text):
    return nltk.sent_tokenize(text)

def vectorizer(inputData, sequenceLength, text=None):
    inputs, queries, inputLabel = [], [], []

    # Condition for processing NLTK corpora
    if text is not None:
        for i in range(0, len(inputData) - sequenceLength, 1):
            
            # Define the necessary input and output vector sequences
            inputSequence = text[i:i + sequenceLength]
            outputSequence = text[i + sequenceLength]

            # Convert the characters to integers for use by the network and add the values to the appropriate lists
            inputs.append([vectorizedVocab[character] for character in inputSequence])
            inputLabel.append(vectorizedVocab[outputSequence])

        return (inputSequence, outputSequence, inputs, inputLabel)

    # Condition for processing the data at the bottom of this file
    # Gotten from https://keras.io/examples/babi_memnn/
    else:        
        for story, query, labels in inputData:
            inputs.append([vectorizedVocab[w] for w in story])
            queries.append([vectorizedVocab[w] for w in query])
            inputLabel.append(vectorizedVocab[labels])

        return (pad_sequences(inputs, maxlen=maxInputLength), pad_sequences(queries, maxlen=maxQueryLength), numpy.array(inputLabel))


def defineModel(vocabLen, outputDimension, dropout, length=None):
    """ Define a sequential model and add input, output and hidden layers (and embedding/dropout) to the model"""
    model = Sequential()

    model.add(Embedding(input_dim = vocabLen, output_dim = outputDimension, input_length = length))
    model.add(Dropout(dropout))

    return model

def loadModel(model, filepath):
    """Load a model to use for prediction """
    model.load_weights(filepath)
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    return model

def predictResponse(model, userInput):
    """ Predict a the response to a give user input
    This should also be used when testing the model """
    output = model.predict(userInput)

    return output

def provideResponse(model, filepath, userInput):
    loadModel(model, filepath)
    
    return predictResponse(model, userInput)



""""
THIS REST OF THIS FILE IS AN EXAMPLE USED FOR UNDERSTANDING HOW TO BUILD A NEURAL NETWORK USING KERAS  
SOME VARIABLES WERE RENAMED TO MAKE THE CODE EASIER TO UNDERSTAND

WEBSITES USED:
https://keras.io/examples/babi_memnn/
https://karpathy.github.io/2015/05/21/rnn-effectiveness/ - No code was used from this website, 
            it was only used as extra reading on Neural Networks

OTHER WEBSITES USED AS REFERENCE/FOR UNDERSTANDING INCLUDE
https://stackabuse.com/text-generation-with-python-and-tensorflow-keras/  
https://towardsdatascience.com/deep-learning-for-nlp-anns-rnns-and-lstms-explained-95866c1db2e4
"""


def parse_stories(lines, only_supporting=False):
    '''Parse stories provided in the bAbi tasks format. 
    If only_supporting is true, only the sentences that support the answer are kept. '''
    data = []
    story = []
    for line in lines:
        line = line.decode('utf-8').strip()
        nid, line = line.split(' ', 1)
        nid = int(nid)
        if nid == 1:
            story = []
        if '\t' in line:
            q, a, supporting = line.split('\t')
            q = tokenize(q)
            if only_supporting:
                # Only select the related substory
                supporting = map(int, supporting.split())
                substory = [story[i - 1] for i in supporting]
            else:
                # Provide all the substories
                substory = [x for x in story if x]
            data.append((substory, q, a))
            story.append('')
        else:
            sent = tokenize(line)
            story.append(sent)
    return data

def get_stories(f, only_supporting=False, max_length=None):
    '''Given a file name, read the file, retrieve the stories, and then convert the sentences into a single story. 
    If max_length is supplied, any stories longer than max_length tokens will be discarded. '''
    data = parse_stories(f.readlines(), only_supporting=only_supporting)
    flatten = lambda data: reduce(lambda x, y: x + y, data)
    data = [(flatten(story), q, answer) for story, q, answer in data
            if not max_length or len(flatten(story)) < max_length]
    return data

try:
    path = get_file('babi-tasks-v1-2.tar.gz', origin='https://s3.amazonaws.com/text-datasets/'
                'babi_tasks_1-20_v1-2.tar.gz')
except:
    print('Error downloading dataset, please download it manually:\n'
          '$ wget http://www.thespermwhale.com/jaseweston/babi/tasks_1-20_v1-2'
          '.tar.gz\n'
          '$ mv tasks_1-20_v1-2.tar.gz ~/.keras/datasets/babi-tasks-v1-2.tar.gz')
    raise


challenges = {
    # QA1 with 10,000 samples
    'single_supporting_fact_10k': 'tasks_1-20_v1-2/en-10k/qa1_'
                                  'single-supporting-fact_{}.txt',
    # QA2 with 10,000 samples
    'two_supporting_facts_10k': 'tasks_1-20_v1-2/en-10k/qa2_'
                                'two-supporting-facts_{}.txt',
}
challenge_type = 'single_supporting_fact_10k'
challenge = challenges[challenge_type]


with tarfile.open(path) as tar:
    train_stories = get_stories(tar.extractfile(challenge.format('train')))
    test_stories = get_stories(tar.extractfile(challenge.format('test')))

combinedStories = train_stories + test_stories
trainingVocabulary = set()
for inputStory, query, answer in combinedStories:
    trainingVocabulary |= set(inputStory + query + [answer]) # |= performs a union on the sets

trainingVocabulary = sorted(trainingVocabulary)

vocabLength = len(trainingVocabulary) + 1
maxInputLength = max(map(len, (x for x, _, _ in combinedStories)))
maxQueryLength = max(map(len, (x for _, x, _ in combinedStories)))
vectorizedVocab = dict((c, i + 1) for i, c in enumerate(trainingVocabulary))
inputData, queryData, labelData = vectorizer(train_stories, len(train_stories))
testInputData, testQueryData, testLabelData = vectorizer(test_stories, len(test_stories))

# Create tensors for the input data and the input question
input_sequence = Input((maxInputLength,))
question = Input((maxQueryLength,))

# embed the input sequence into a sequence of vectors
mainModel = defineModel(vocabLength, 64, 0.3)
inputEncoder = defineModel(vocabLength, maxQueryLength, 0.3)
questionEncoder = defineModel(vocabLength, 64, 0.3, maxQueryLength)

# encode input sequence and questions (which are indices) to sequences of dense vectors
mainEncodedInput = mainModel(input_sequence)
encodedInput = inputEncoder(input_sequence)
encodedQuestion = questionEncoder(question)

# compute a 'match' between the first input vector sequence and the question vector sequence
match = dot([mainEncodedInput, encodedQuestion], (2, 2))
match = Activation('softmax')(match)

# add the match matrix with the second input vector sequence
response = add([match, encodedInput]) 
response = Permute((2, 1))(response)  

# concatenate the match matrix with the question vector sequence
answer = concatenate([response, encodedQuestion])

# the original paper uses a matrix multiplication for this reduction step, we choose to use a RNN instead.
answer = LSTM(256)(answer)  

# one regularization layer -- more would probably be needed.
answer = Dropout(0.3)(answer)
answer = Dense(vocabLength)(answer)  

# we output a probability distribution over the vocabulary
answer = Activation('softmax')(answer)

# # build the final model
# model = Model([input_sequence, question], answer)
model = Model()
model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# # train   
# model.fit([inputData, queryData], labelData, batch_size=256, epochs=120, validation_data=([testInputData, testQueryData], testLabelData))

# # save the model 
# filename = 'largeDataset120epochs.hdf5'
# model.save(filename)
