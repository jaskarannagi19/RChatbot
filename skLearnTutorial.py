from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
import numpy as np


# print(len(twenty_train.data))
# print((twenty_train.filenames))
# print(len(twenty_train.filenames)) -- 2257 items in the dataset
# print(twenty_train.target_names)

# # print("\n".join(twenty_train.data[0].split("\n")[:3]))

# count_vect = CountVectorizer()
# X_train_counts = count_vect.fit_transform(twenty_train.data) # Creates a matrix with all the words in the dataset

# print(X_train_counts.shape) # (2257, 35788) - the size of the matrix

# print(count_vect.vocabulary_.get(u'printer')) # returns the index value of the word put as a parameter


# Perform Tf-Idf down-scaling on the matrix for words that occur in many datasets/documents
# tfidf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts) # Fits the estimator to the data
# X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts) # Transform the count matrix to a tf-idf matrix
# # print(X_train_tfidf.shape) # (2257, 35788)
# print(X_train_tfidf) 

# print(twenty_train.target)
# clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target) # Build the classifier and fit it to the training data

# X_new_counts = count_vect.transform(docs_new) # Transform the test data to a count matrix
# X_new_tfidf = tfidf_transformer.transform(X_new_counts) # Transform this matrix to a tf-idf representation

# predicted = clf.predict(X_new_tfidf) # Use the classifier to predict the labels for the test set

# for doc, category in zip(docs_new, predicted):
#     print('%r => %s' % (doc, twenty_train.target_names[category]))

# The categories being used for classification
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']

# The training data
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

docs_new = ['I am not a religious person', 'Photoshop is reliable', "My Macbook has a retina display", "My phone has a good camera and takes clear pictures", "I took a picture yesterday", "I'm afraid of my doctor"]
twenty_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data



def nbClassify():
    # Build a pipeline to simplify the process of creating the vector matrix, transforming to tf-idf and classifying
    text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', MultinomialNB())])
    text_clf.fit(twenty_train.data, twenty_train.target)


    # Evaluating the performance of the classifier

    predicted = text_clf.predict(docs_test)
    print(np.mean(predicted == twenty_test.target))



"""ALTERNATIVE TO MULTINOMINAL NB CLASSIFIER"""
# CLASSIFYING USING SVM (SUPPORT VECTOR MACHINE)
def svmClassify(dataset):
    text_clf = Pipeline([('vect', CountVectorizer()),('tfidf', TfidfTransformer()),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, random_state=42, max_iter=5, tol=None))])
    text_clf.fit(twenty_train.data, twenty_train.target)

    predicted = text_clf.predict(docs_test)
    print(np.mean(predicted == twenty_test.target))

    # VIEW THE PERFORMANCE METRICS OF THE MODELS 
    print(metrics.classification_report(twenty_test.target, predicted, target_names=twenty_test.target_names))
    print(metrics.confusion_matrix(twenty_test.target, predicted))

# nbClassify()
print(twenty_train.target)
