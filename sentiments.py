#!/usr/local/bin/python3
import nltk, tagging as tag, stemming as stem, csv
from nltk.corpus import webtext as web


monty = nltk.sent_tokenize(web.raw('grail.txt'))
sentenceTypes = [1, 2, 3, 4] # 1- Simple/Declarative, 2 - Imperative, 3 - Interrogative, 4 - Exclamatory
sentimentTags = [1, 2, 3, 4, 5, 6] # 1 - Negative, 2 - Somewhat Negative, 3 - Sarcastic, 4 - Neutral, 5 - Somewhat positive, 6 - Positive
# THINK ABOUT SEPARATING QUESTIONS FROM STATEMENTS


trainingSize = int(len(monty) * 0.7)
trainingSents = monty[:trainingSize]
testSents = monty[trainingSize:]


with open('montyPython.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["PhraseID", "SentenceID", "Sentence"])

    for i in range(len(trainingSents)):
        if not trainingSents[i].startswith("SCENE"):
            writer.writerow([i, i, trainingSents[i]])


