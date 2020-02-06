import nltk
from nltk.text import Text
import stemming as stemmer
import tagging as tag


def converse(userInput):
    conversation = True
    while conversation is True:
        userInput = nltk.sent_tokenize(userInput)
        output = tag.assignTags(userInput)
        print(userInput)
        conversation = False


    return output


userInput = input("")
converse(userInput)



# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
