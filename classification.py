#!/usr/local/bin/python3
import nltk, csv
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as panda
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier

def tokenize(text):
    # pattern derived from NLTK book, chapter on tokenization
    pattern = r'''(?x) (?:[A-Z]\.)+ | \w+(?:-\w+)*| \$?\d+(?:\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]'''
    return nltk.regexp_tokenize(text, pattern)


# GET THE DATA/TEXT
with open("MontyPython.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines] 

# NOISE REMOVAL
tempLines = []
for i in range(len(lines)):
    if not lines[i].startswith('['):
        if ":" in lines[i]:
            startIndex = lines[i].index(":")+1
        else:
            startIndex = 0
        tempLines.append(lines[i][startIndex:])
lines = tempLines

# # TOKENIZE THE TEXT
# lines = [nltk.tokenize(lines[i]) for i in range(len(lines))]
lines = [tokenize(str(lines[i])) for i in range(len(lines))]

# # TAG THE TEXT
lines = [pos_tag(lines[i]) for i in range(len(lines))]

# # NORMALIZE (STEM OR LEMMATIZE) - GO WITH LEMMATIZE
def sentLemmatizer(sentence):
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

# lines = [sentLemmatizer(lines[i]) for i in range(len(lines))]
# [print(lines[i], end ="\n") for i in range(len(lines))]

# Identify the most common words in the script
def countWords(sentences):
    for words in sentences:
        for token in words:
            yield token

uniqueWords = countWords(lines)

# frequencies = FreqDist(uniqueWords)
# print(frequencies.most_common(10))

# CLASSIFICATION AND TRAINING BEGINS HERE
# COPY THE DATA INTO A CSV FILE AND ADD TAGS

def writeToFile(listToWrite, fileName):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["SentenceID", "Sentence"])
        for i in range(len(listToWrite)):
            writer.writerow([i+1, listToWrite[i]])

trainingSize = int(len(lines) * 0.7)
trainingSents = lines[:trainingSize]
testSents = lines[trainingSize:]
# writeToFile(tempLines[:trainingSize], 'trainer.csv')
# writeToFile(tempLines[trainingSize:], 'tester.csv')


"""SENTIMENT ANALYSIS"""
sentimentTags = ["irrelevant", "negative", "sarcastic", "neutral", "positive", "exclamation"] 
# 0 - Narrator, 1 - Negative, 2 - Sarcastic, 3 - Neutral, 4 - Positive, 5 - Excalmation


"""BEGIN CLASSIFICATION"""
trainingLines, trainingData, categories, testingData = [], [], [], []

with open('trainer.csv') as trainer:
    reader = csv.reader(trainer)
    for row in reader:
        trainingData.append(row[1])
        categories.append(row[2])

with open('tester.csv') as tester:
    reader = csv.reader(tester)
    for row in reader:
        testingData.append(row[1])


# [print(trainingData[i], " ", trainingSents[i], end ="\n") for i in range(len(trainingData))]



# categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

# # The training data
# twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

# docs_new = ['I am not a religious person', 'Photoshop is reliable', "My Macbook has a retina display", "My phone has a good camera and takes clear pictures", "I took a picture yesterday", "I'm afraid of my doctor"]
# twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
# docs_test = twenty_test.data

def nbClassify(trainSet, trainCategories, testSet):
    # Build a pipeline to simplify the process of creating the vector matrix, transforming to tf-idf and classifying
    text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
    # text_clf.fit(twenty_train.data, twenty_train.target)
    text_clf.fit(trainSet, trainCategories)


    # Evaluating the performance of the classifier

    predictions = text_clf.predict(testSet)
    return predictions


"""ALTERNATIVE TO MULTINOMINAL NB CLASSIFIER"""
# CLASSIFYING USING SVM (SUPPORT VECTOR MACHINE)
def svmClassify(trainSet, trainCategories, testSet):
    text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None))])
    text_clf.fit(trainSet, trainCategories)

    predictions = text_clf.predict(testSet)



nbClassify(trainingData, categories, testingData)
svmClassify(trainingData, categories, testingData)








# https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
