#!/usr/local/bin/python3
import os, sys, random, nltk, stanfordnlp, nltk.data, nltk.text
from random import randint
from nltk.stem.wordnet import WordNetLemmatizer


# Natural Language Toolkit: code_stemmer_indexing. 
# Source: NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
# Chapter 3

'''Indexing a Text Using a Stemmer'''
class IndexedText(object):
    
    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer 
        self._lem = WordNetLemmatizer()
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

    def _lemmatize(self, word):

        # Lemmatization with StanfordNLP
        # word = nltk.word_tokenize(word)
        # words = nlp(word)
        # words.sentences[0].print_dependencies()
        # print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in words.sentences for word in sent.words], sep='\n')


        return self._lem.lemmatize(word).lower()


# TOKENIZE TEXT, LEAVING WORDS WITH SYMBOLS (HYPHENS, APOSTROPHES, ETC) AS THE SAME TOKEN
def tokenize(text):
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


# text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
# seg1 = "0000000000000001000000000010000000000000000100000000000"
# seg2 = "0100100100100001001001000010100100010010000100010010000"
# seg3 = "0000100100000011001000000110000100010000001100010000001"
# anneal(text, seg1, 5000, 1.2)

