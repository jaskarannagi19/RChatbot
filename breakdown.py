#!/usr/local/bin/python3
import os, sys, random, nltk, stanfordnlp, nltk.data, nltk.text
import code_stemmer_indexing as stemmer

porter = nltk.PorterStemmer()
grail = nltk.corpus.webtext.words('grail.txt') #retrieve the script
text = stemmer.IndexedText(porter, grail) # convert it to indexed text that can be searched with a stemmer
text.concordance('woman')


montyStrings = " ".join(grail)
montyTokens = nltk.word_tokenize(montyStrings)

montyText = nltk.Text(montyTokens)
# montyText.findall(r"<French>")

text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"
seg3 = "0000100100000011001000000110000100010000001100010000001"
stemmer.anneal(text, seg1, 5000, 1.2)

# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
''' STANFORD NLP: Peng Qi, Timothy Dozat, Yuhao Zhang and Christopher D. Manning. 2018. 
Universal Dependency Parsing from Scratch In Proceedings of the CoNLL 2018 Shared Task: 
Multilingual Parsing from Raw Text to Universal Dependencies, pp. 160-170. [pdf] [bib] '''

