#!/usr/local/bin/python3
import nltk, csv
import smallerNeuralNetwork as sNetwork
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier


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

# CLASSIFICATION AND TRAINING BEGINS HERE
# COPY THE DATA INTO A CSV FILE AND ADD TAGS

def writeToFile(listToWrite, fileName):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["SentenceID", "Sentence"])
        for i in range(len(listToWrite)):
            writer.writerow([i+1, listToWrite[i]])



# writeToFile(trainingSents, 'trainer.csv')
# writeToFile(testSents, 'tester.csv')


"""SENTIMENT ANALYSIS"""
sentimentTags = ["negative", "sarcastic", "neutral", "positive", "exclamation"] 
# 1 - Negative, 2 - Sarcastic, 3 - Neutral, 4 - Positive, 5 - Excalmation

"""BEGIN CLASSIFICATION AFTER MANUALLY TAGGING THE TEST DATA"""
trainingLines, trainingData, categories, testingData = [], [], [], []

# #Read the files and get the classification tags
# with open('trainer.csv') as trainer:
#     reader = csv.reader(trainer)
#     for row in reader:
#         trainingData.append(row[1])
#         categories.append(row[2])

# with open('tester.csv') as tester:
#     reader = csv.reader(tester)
#     for row in reader:
#         testingData.append(row[1])


# [print(trainingData[i], " ", trainingSents[i], end ="\n") for i in range(len(trainingData))]

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
    return predictions


