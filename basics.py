import nltk
from nltk.text import Text

conversation = True
print("Hello, I'm a ChatBot. Ask me anything")


while conversation is True:
    user = input("")
    words = nltk.word_tokenize(user)
    for i in range(len(words)):
        words[i] = str.lower(words[i])

    if words.__contains__("hello") or words.__contains__("hi"):
        print("Hello")
    elif words.__contains__("sad"):
        print("That's too bad")
    elif words.__contains__("where"):
        print("Up North")
    elif words.__contains__("?"):
        print("Ask me again some other time")
    elif words.__contains__("bye") or words.__contains__("goodbye"):
        print("I have to leave now")
        conversation = False
    else:
        print("I'm afraid I can't respond to that")

    


