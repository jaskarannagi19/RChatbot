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



# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
''' STANFORD NLP: Peng Qi, Timothy Dozat, Yuhao Zhang and Christopher D. Manning. 2018. 
Universal Dependency Parsing from Scratch In Proceedings of the CoNLL 2018 Shared Task: 
Multilingual Parsing from Raw Text to Universal Dependencies, pp. 160-170. [pdf] [bib] '''

