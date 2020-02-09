#!/usr/local/bin/python3
import nltk, csv

# TOKENIZE TEXT, LEAVING WORDS WITH SYMBOLS (HYPHENS, APOSTROPHES, ETC) AS THE SAME TOKEN
def tokenize(text):
    pattern = r'''(?x) (?:[A-Z]\.)+ | \w+(?:-\w+)*| \$?\d+(?:\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]'''
    return nltk.regexp_tokenize(text, pattern)

def assignTags(items):
    
    items = [tokenize(str(items[i])) for i in range(len(items))]
    taggedItems = []
    for i in range(len(items)):
        item = nltk.pos_tag(items[i])
        taggedItems.append(item)

    return evaluateTags(taggedItems)

def evaluateTags(trainingList, testList=None):	
    t0 = nltk.DefaultTagger("NN")
    t1 = nltk.UnigramTagger(trainingList, backoff=t0)
    t2 = nltk.BigramTagger(trainingList, backoff=t1)
    t3 = nltk.TrigramTagger(trainingList, backoff=t2)

    if testList is not None:
        if t3.evaluate(testList) > 0.7:
                return testList
        else:
            return None
    else:
        return trainingList
    
with open("MontyPython.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines] 

tempLines = []
for i in range(len(lines)):
    if not lines[i].startswith('['):
        tempLines.append(lines[i])
lines = tempLines

lines = [nltk.sent_tokenize(lines[i]) for i in range(len(lines))]
# taggedLines = assignTags(lines)
# [print(taggedLines[i], end="\n") for i in range(len(taggedLines))]
# trainingSize = int(len(lines) * 0.7)
# trainingSents = lines[:trainingSize]
# testSents = lines[trainingSize:]
# evaluateTags(testSents, trainingSents)

"""SENTIMENT ANALYSIS"""

sentenceTypes = [1, 2, 3, 4] # 1- Simple/Declarative, 2 - Imperative, 3 - Interrogative, 4 - Exclamatory 5 - Sound Effects, 6 - Descriptions, 7 - Non-English
sentimentTags = [1, 2, 3, 4, 5, 6] # 1 - Negative, 2 - Somewhat Negative, 3 - Sarcastic, 4 - Neutral, 5 - Somewhat positive, 6 - Positive

def writeToFile(listToWrite, fileName):
    with open(fileName, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["SentenceID", "Sentence"])
        for i in range(len(listToWrite)):
            writer.writerow([i+1, listToWrite[i]])

# writeToFile(tempLines[:trainingSize], 'trainingList.csv')
# writeToFile(tempLines[trainingSize:], 'testList.csv')




"""WORKING WITH GRAMMARS"""
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

# def chunkSentence(inputSentence):
#     grammar = "NP: {<DT>?<JJ>*<NN>}" 
#     cp = nltk.RegexpParser(grammar) 
#     result = cp.parse(inputSentence) 
#     print(result) 

# # (S
# #   (NP the/DT little/JJ yellow/JJ dog/NN)
# #   barked/VBD
# #   at/IN
# #   (NP the/DT cat/NN))
# result.draw() 

# grammar1 = nltk.data.load('file:grammars.cfg')
# sent = "Mary saw Bob".split()
# rd_parser = nltk.RecursiveDescentParser(grammar1)
# for tree in rd_parser.parse(sent):
#     print(tree)









# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.

