#!/usr/local/bin/python3
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

#userInput = input("")
# print(converse(userInput))
#converse(userInput)

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.







#wordList = nltk.word_tokenize(inputString)
        
        #for i in range(len(wordList)):
        #    wordList[i] = lem.lemmatize(wordList[i], pos="v")

        #wordList = processText(wordList)