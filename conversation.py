#!/usr/local/bin/python3
<<<<<<< HEAD
import nltk, random, smallerNeuralNetwork as sNetwork
from nltk.stem import WordNetLemmatizer
lem = WordNetLemmatizer()

# Generic chatbot responses for specific scenarios in the chatbot
greetings = ("hello", "hi", "hey")
genericResponses = ["What do you want this time?", "Hey", "Hi.", "Yay, another conversation :/"]
confusedResponses = ["What do you mean?", "I don't get that and I don't want to", "This is not fun",
                    "I'm going to pretend you didn't say that", "Stop. Moving on", "No", "You make me sad",
                    "I don't like talking to you", "Can we have this conversation another time", "Okay, it's time for you to go"]
exitWords = ["bye", "goodbye"]
userSentences = []

def sentLemmatizer(sentence):
    """ Lemmatize a sentence based on the tags accompanying the individual words """
    lem, lemSent, lemTags = WordNetLemmatizer(), [], []
    for word, tag in sentence:
        if tag.startswith('NN'):
            lemma = lem.lemmatize(word, 'n')
        elif tag.startswith('VB'):
            lemma = lem.lemmatize(word, 'v')
        else:
            lemma = lem.lemmatize(word, 'a')
        lemSent.append((lemma))
        # lemTags.append((lemma, tag))
    return lemSent


def processText(sentence):
    """ Perform basic NLP preprocessing on the user's input """
    # Basic text pre-processing: Make Lower Case > Tokenize text > Tag text > Lemmatize
    # for word in sentence:
    #     word = word.lower()

    # pattern derived from NLTK book, chapter on tokenization
    pattern = r'''(?x) (?:[A-Z]\.)+ | \w+(?:-\w+)*| \$?\d+(?:\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]'''
    sentence = nltk.regexp_tokenize(sentence, pattern)
    sentence = nltk.pos_tag(sentence)
    sentence = sentLemmatizer(sentence)

    return sentence

def converse(inputString, conversation):
    """ The main controller for the chatbot. 
    All conversations and text processing are controlled from in here. 
    The Neural network generates responses when prompted from within this method 
    and all other responses are prompted from here."""
    inputString = inputString.lower()
    inputString = processText(inputString)

    if inputString.__contains__("hello") or inputString.__contains__("hi") or inputString.__contains__("hey"): 
        response = random.choice(genericResponses)
        print(random.choice(genericResponses))
  
    elif inputString.__contains__("bye") or inputString.__contains__("goodbye"):
        response = "Good day, and let's not do this again"
        print("Good day, and let's not do this again")
        conversation = False

    else:
        value = random.randint(0,1)
        # Randomly decide whether or not to print a set response or re-print what the user has entered (inspired by ELIZA) 
        if value == 5:
            response = inputString
            print(inputString)
        else:
            # Send all other user inputs to the Neural Network for responses to be generated
            # Use a try-except block to prevent the conversation from breaking due to an error
            try:
                response = sNetwork.provideResponse(inputString)
                # sNetwork.provideRepsonse(inputString)
                print(response)
            except:
                response = random.choice(confusedResponses)
                print(random.choice(confusedResponses))

    return (conversation, response)


# Initiate the conversation 
def intro():
    #print("Hi there, say something to Monty")
    return "Hi there, say something to Monty"

#conversation = True

# Carry on the conversation as long as the user has not said bye
#while conversation is True:
    #userInput = input("")
    #activeConversation, montyResponse = converse(userInput, conversation)
    
    #conversation = activeConversation
=======
import nltk
import random
import tagging
import string
from nltk.text import Text
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
lemmer = WordNetLemmatizer()

# Opens the corpus to be read from and analysed
openFile = open('MontyPython.txt')
# Read all the text and then convert it to lowercase
rawText = openFile.read()
rawText = rawText.lower()

# Punkt uses an algorithm to basically find where sentences should start and end
nltk.download('punkt')
# Wordnet is a database used to find out how similar words are to each other
nltk.download('wordnet')

# This uses tokenization to convert the text into a list of sentences and words respectively
sent_tokens = nltk.sent_tokenize(rawText)
word_tokens = nltk.word_tokenize(rawText)

# Standard input and ouput responses for greeting the chatbot
GREETING_INPUTS = ("hello", "hi", "sup", "hey", "hi monty")
GREETING_RESPONSES = ["Hi", "Hey", "Hello", "Hello stranger"]
# If the user types something that the bot doesnt understand, it will choose one of these responses to output
Nothing = ["What do you mean?", "Monty doesn't compute what you just said"]

def converse(inputString):
    conversation = True
    while conversation is True:
        count = 0

        # Splits the sentence up and looks at each word individually
        for word in inputString.split():
            # If the word (in lowercase format) is in the greetings input array, then output a random greetings output and increase count by 1
            if word.lower() in GREETING_INPUTS:
                wordList = random.choice(GREETING_RESPONSES)
                count = count + 1
            # If the word is not in the greetings input then call the response function for the whole sentence
            else:
                wordList = response(inputString)
                # Stops the chatbot repeating exactly what you said
                sent_tokens.remove(inputString)

        conversation = False
    return wordList

def response(user_response):
    response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        response=response+"I am sorry! I don't understand you"
        return response
    else:
        response = response+sent_tokens[idx]
        return response

def processText(tokens):
    tokens = nltk.pos_tag(tokens)
    return tokens
>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f

#userInput = input("")
# print(converse(userInput))
#converse(userInput)

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


<<<<<<< HEAD
"""NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
"""
=======
# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.







#wordList = nltk.word_tokenize(inputString)
        
        #for i in range(len(wordList)):
        #    wordList[i] = lem.lemmatize(wordList[i], pos="v")

        #wordList = processText(wordList)
>>>>>>> 6ce34b134c04869ceee472af2be608bce7b6b12f
