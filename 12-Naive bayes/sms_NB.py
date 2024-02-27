#import necessary libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split

#read the csv file
email_data = pd.read_csv("C:/2-Dataset/sms_raw_NB.csv",encoding="ISO-8859-1")

#define function to clean the data
import re
def cleaning_data(i):
    w = []
    i = re.sub("[^A-Za-z""]+"," ",i).lower()
    for word in i.split(" "):
        if len(word)>3:
            w.append(word)
    return(" ".join(w))

#testing above function
cleaning_data("Hope you are having a good week. Just checking in")
cleaning_data("hope i can understand your feelings 123121.123.hi how are you")
cleaning_data("hi how are you, I am sad")

#apply cleaning data function to complete dataset
email_data.text = email_data.text.apply(cleaning_data)
email_data = email_data.loc[email_data.text != "",:]

#split the dataset into test and train
email_train,email_test = train_test_split(email_data,test_size=0.2)


#creating matrix of token count for entire text document
def split_into_words(i):
    return [word for word in i.split(" ")]

email_bow = CountVectorizer(analyzer=split_into_words).fit(email_data.text)
all_emails_matrix = email_bow.transform(email_data.text)
#for training data
train_emails_matrix = email_bow.transform(email_train.text)
#for testing data
test_emails_matrix = email_bow.transform(email_test.text)

tfidf_transformer = TfidfTransformer().fit(all_emails_matrix)
#preparing TFIDF for train data
train_tfidf = tfidf_transformer.transform(train_emails_matrix)
#preparing TFIDF for train data
test_tfidf = tfidf_transformer.transform(test_emails_matrix)
test_tfidf.shape


#now let us apply Naive bayes to this
from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb = MB()
classifier_mb.fit(train_tfidf, email_train.type)

#evalution on test data
test_pred_m = classifier_mb.predict(test_tfidf)
accuracy_test_m = np.mean(test_pred_m==email_test.type)
accuracy_test_m