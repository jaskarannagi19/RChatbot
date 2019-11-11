#!/usr/local/bin/python3

import nltk, stanfordnlp
from nltk.text import Text
import stemming as stemmer
from nltk.tokenize import sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import webtext as web
from nltk.tag import StanfordPOSTagger, StanfordNERTagger
# from pickle import load, dump

monty = nltk.sent_tokenize(web.raw('grail.txt'))
# nlp = stanfordnlp.Pipeline(processors='tokenize,mwt,pos')
# tagList = []
# for i in range(len(monty)):
#     doc = nlp(monty[i])
#     # print(*[f'word: {word.text+" "}\tupos: {word.upos}\txpos: {word.xpos}' for sent in doc.sentences for word in sent.words], sep='\n')
#     tags = {word.text:word.upos for sent in doc._sentences for word in sent.words}
#     tagList.append(tags)

# [print(tagList[i], end = '\n') for i in range(len(tagList))]

jar = 'stanford-postagger-2018-10-16/stanford-postagger.jar'
model = 'stanford-postagger-2018-10-16/models/english-left3words-distsim.tagger'

spt = StanfordPOSTagger(model, jar, encoding='utf8')
nrt = StanfordNERTagger(model, jar, encoding='utf8')


def assignTags(items):
    for i in range(len(items)):
        text = nltk.word_tokenize(items[i])
        items[i] = nltk.pos_tag(text, tagset="universal")
        # print(line)

def evaluateTags(testList, trainingList):	
    t0 = nltk.DefaultTagger("NN")
    t1 = nltk.UnigramTagger(trainingList, backoff=t0)
    t2 = nltk.BigramTagger(trainingList, backoff=t1)
    t3 = nltk.TrigramTagger(trainingList, backoff=t2)

    # For storing trained tags on large pieces of text
    # output = open('t2.pkl', 'wb')
    # dump(t2, output, -1)
    # output.close()
    
    if t3.evaluate(testList) > 0.7:
        return testList
    else:
        return None

def printTags(items):
    for i in range(len(items)):
        print(items[i], end="")

assignTags(monty)

trainingSize = int(len(monty) * 0.7)
trainingSents = monty[:trainingSize]
testSents = monty[trainingSize:]

evaluateTags(testSents, trainingSents)


# print(evaluateTags(trainingSents, testSents)) # = 0.8096951735817104
# print(testSents)
# print(evaluateTags(nltk.word_tokenize("What is the airspeed of an unladen swallow?")))




# ADJ: adjective, ADP: adposition, ADV: adverb, AUX: auxiliary, CCONJ: coordinating conjunction, DET: determiner
# INTJ: interjection, NOUN: noun, NUM: numeral, PART: particle, PRON: pronoun, PROPN: proper noun, PUNCT: punctuation 
# SCONJ: subordinating conjunction, SYM: symbol, VERB: verb, X: other
# © 2014–2017 Universal Dependencies contributors. Site powered by Annodoc and brat
# Source: https://universaldependencies.org/u/pos/

# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
''' STANFORD NLP: Peng Qi, Timothy Dozat, Yuhao Zhang and Christopher D. Manning. 2018. 
Universal Dependency Parsing from Scratch In Proceedings of the CoNLL 2018 Shared Task: 
Multilingual Parsing from Raw Text to Universal Dependencies, pp. 160-170. [pdf] [bib] '''

