#!/usr/local/bin/python3

import os, sys, random, nltk, stanfordnlp, nltk.data, nltk.text

# nlp = stanfordnlp.Pipeline() # This sets up a default neural pipeline in English
# doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
# doc.sentences[0].print_dependencies()

grail = nltk.corpus.webtext.words('grail.txt')

monty = " ".join(grail)
montyTokens = nltk.word_tokenize(monty)

montyText = nltk.Text(montyTokens)
montyText.findall(r"<French>")



# # m = scene1[8]
# # line8 = nltk.word_tokenize(m)

# #  Find the most commonly occuring lines
# fDist = nltk.FreqDist(scene1[i] for i in range(len(scene1)))
# print(fDist.most_common(2), end = " ")

# # Lemmatization with StanfordNLP
# # words = nlp(m)
# # words.sentences[0].print_dependencies()
# # print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in words.sentences for word in sent.words], sep='\n')



# lines = [line for line in open('MontyPython.txt', 'r') if not line.startswith('\n')]
# monty = "".join(lines)

# [print(lines[i]) for i in range(len(lines))]
# scene1 = []
# for i in range(len(lines)):
#     if lines[i].startswith("Scene 2"):
#         break
#     scene1.append(lines[i])
# [print(scene1[i]) for i in range(len(scene1))]

# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
''' STANFORD NLP: Peng Qi, Timothy Dozat, Yuhao Zhang and Christopher D. Manning. 2018. 
Universal Dependency Parsing from Scratch In Proceedings of the CoNLL 2018 Shared Task: 
Multilingual Parsing from Raw Text to Universal Dependencies, pp. 160-170. [pdf] [bib] '''

