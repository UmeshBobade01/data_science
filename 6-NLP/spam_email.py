""" Spam mail detection """

#import libraries
import pandas as pd
import numpy as np
#read file
df = pd.read_csv('2-Dataset/spam.csv')
#view sample data
df.head()
#find out the number of records and no. of columns
df.shape
#find the count of categorical data
df.Category.value_counts()
"""ham     4825
spam     747"""
#add new column which contains value 0 or 1 according to message is spam or not
df['spam'] = df['Category'].apply(lambda x:1 if x=='spam' else 0)
df.shape

###############################################################################

#train_test_split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)

#let's check the x_train and x_test datasets
x_train.shape
x_test.shape
#check the type of x_train and x_test
type(x_train)
type(x_test)

###############################################################################

#create BoW representations using countvectorizer
from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
x_train_cv = v.fit_transform(x_train.values)
x_train_cv

#after creation let's check the shape of BoW representation
x_train_cv.shape

###############################################################################

#train the naive bayes model
from sklearn.naive_bayes import MultinomialNB
#initialize the model
model = MultinomialNB()
#train the model
model.fit(x_train_cv,y_train)

###############################################################################

#create the BoW representation for using countvectorizer for x_test
x_test_cv = v.transform(x_test)

###############################################################################

#evaluate performance
from sklearn.metrics import classification_report
y_pred = model.predict(x_test_cv)
print(classification_report(y_test, y_pred))

##############################################################################