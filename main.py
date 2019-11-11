import nltk
from nltk.text import Text
import stemming as stemmer
import tagging as tag


def converse(userInput):
    conversation = True
    while conversation is True:
        userInput = nltk.sent_tokenize(userInput)
        userTags = tag.assignTags(userInput)
        print(userInput)
        conversation = False

        # for i in range(len(words)):
        #     words[i] = str.lower(words[i])
        # if words.__contains__("hello") or words.__contains__("hi"):
        #     print("Hello")
        # elif words.__contains__("sad"):
        #     print("That's too bad")
        # elif words.__contains__("where"):
        #     print("Up North")
        # elif words.__contains__("?"):
        #     print("Ask me again some other time")
        # elif words.__contains__("bye") or words.__contains__("goodbye"):
        #     print("I have to leave now")
        #     conversation = False
        # else:
        #     print("I'm afraid I can't respond to that")

# def getTokens(userInput):
#     words = stemmer.tokenize(userInput)
#     return words

print("Hello, I'm a ChatBot. Ask me anything")
user = input("")
converse(user)



# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
''' STANFORD NLP: Peng Qi, Timothy Dozat, Yuhao Zhang and Christopher D. Manning. 2018. 
Universal Dependency Parsing from Scratch In Proceedings of the CoNLL 2018 Shared Task: 
Multilingual Parsing from Raw Text to Universal Dependencies, pp. 160-170. [pdf] [bib] '''

