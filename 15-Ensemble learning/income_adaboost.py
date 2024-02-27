""" Adaboost """

import pandas as pd 
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics 
import warnings 
warnings.filterwarnings('ignore')
#read csv file
loan_data = pd.read_csv("C:/2-dataset/Incomeadaboost.csv")
loan_data.columns
loan_data.head()
#let us split the data in input and output 
x = loan_data.iloc[:,0:6]
y = loan_data.iloc[:,6]
#split the dataset 
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)

#create adaboost classifier 
ada_model = AdaBoostClassifier(n_estimators = 100, learning_rate = 1)
#n_estimatiors = number of weak learners 
#learning rate, it contributes weights of weak learner, by default it is 1

#Train the model 
model = ada_model.fit(x_train,y_train)

#predict the results 
y_pred = model.predict(x_test)
print("accuracy", metrics.accuracy_score(y_test, y_pred)) #accuracy 0.8392875422254069


#let us try for another base model 
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

#here base model is changed 
Ada_model = AdaBoostClassifier(n_estimators=50, base_estimator = lr,learning_rate = 1)
model = ada_model.fit(x_train, y_train )    
y_pred = model.predict(x_test)
print("accuracy", metrics.accuracy_score(y_test, y_pred)) #accuracy 0.8327679394001433
                                                   











