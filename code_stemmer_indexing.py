#!/usr/local/bin/python3
import os, sys, random, nltk, stanfordnlp, nltk.data, nltk.text
from random import randint


# Natural Language Toolkit: code_stemmer_indexing. 
# Source: NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
# Chapter 3

'''Indexing a Text Using a Stemmer'''
class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer 
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))

    #FIND THE SPECIFIED WORD AT EVERY POINT IT APPEARS IN THE TEXT
    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/4)                # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i-wc:i])
            rcontext = ' '.join(self._text[i:i+wc])
            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
            print(ldisplay, rdisplay)

    def _stem(self, word):
        return self._stemmer.stem(word).lower()


# TOKENIZE TEXT, LEAVING WORDS WITH SYMBOLS (HYPHENS, APOSTROPHES, ETC) AS THE SAME TOKEN
def tokenize(self, text):
    pattern = r'''(?x) (?:[A-Z]\.)+ | \w+(?:-\w+)*| \$?\d+(?:\.\d+)?%?| \.\.\.| [][.,;"'?():-_`]'''
    return nltk.regexp_tokenize(text, pattern)

'''Reconstruct Segmented Text from String Representation: seg1 and seg2 represent the initial and final segmentations 
of some hypothetical child-directed speech; the segment() function can use them to reproduce the segmented text. '''
def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words


'''Computing the Cost of Storing the Lexicon and Reconstructing the Source Text'''
def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = sum(len(word) + 1 for word in set(words))
    return text_size + lexicon_size

 	


'''Non-Deterministic Search Using Simulated Annealing: begin searching with phrase segmentations only; 
randomly perturb the zeros and ones proportional to the "temperature"; 
with each iteration the temperature is lowered and the perturbation of boundaries is reduced. 
As this search algorithm is non-deterministic, you may see a slightly different result.'''
def flip(segs, pos):
    return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

def flip_n(segs, n):
    for i in range(n):
        segs = flip(segs, randint(0, len(segs)-1))
    return segs

def anneal(text, segs, iterations, cooling_rate):
    temperature = float(len(segs))
    while temperature > 0.5:
        best_segs, best = segs, evaluate(text, segs)
        for i in range(iterations):
            guess = flip_n(segs, round(temperature))
            score = evaluate(text, guess)
            if score < best:
                best, best_segs = score, guess
        score, segs = best, best_segs
        temperature = temperature / cooling_rate
        print(evaluate(text, segs), segment(text, segs))
    print()
    return segs


