import nltk
from nltk.text import Text
# import gui 
import tagging as tag


def converse(inputString):

    conversation = True
    while conversation is True:
        inputList = inputString.split(" ")

        output = tag.assignTags(inputList)
        conversation = False
    return output

# userInput = input("")
# converse(userInput)



# NLTK: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
