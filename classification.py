#!/usr/local/bin/python3
import nltk
from nltk.corpus import webtext as web
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.naive_bayes import MultinomialNB #Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
from sklearn.model_selection import train_test_split


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('train.tsv', sep='\t')
# data.head()
# data.info()





#tokenizer to remove unwanted elements from the data like symbols and numbers
token = RegexpTokenizer(r'[a-zA-Z0-9]+')
cv = CountVectorizer(lowercase=True, stop_words='english', ngram_range = (1,1), tokenizer = token.tokenize)
text_counts= cv.fit_transform(data['Phrase'])
X_train, X_test, y_train, y_test = train_test_split(text_counts, data['Sentiment'], test_size=0.3, random_state=1)





clf = MultinomialNB().fit(X_train, y_train)
predicted= clf.predict(X_test)
print("MultinomialNB Accuracy:",metrics.accuracy_score(y_test, predicted))









monty = nltk.sent_tokenize(web.raw('grail.txt'))




# [print(monty[i], end = "\n") for i in range(len(monty))]
# print(data.Sentiment.value_counts())

# Sentiment_count=data.groupby('Sentiment').count()
# plt.bar(Sentiment_count.index.values, Sentiment_count['Phrase'])
# plt.xlabel('Review Sentiments')
# plt.ylabel('Number of Review')
# plt.show()