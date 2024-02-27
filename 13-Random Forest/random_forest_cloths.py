"""
A cloth manufacturing company is interested to know about the different attributes 
contributing to high sales. Build a random forest model with Sales as target
variable (first convert it into categorical variable).
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:/2-Dataset/Company_Data.csv")
df
"""EDA"""

df.head()
"""
Sales  CompPrice  Income  Advertising  ...  Age  Education Urban   US
0   9.50        138      73           11  ...   42         17   Yes  Yes
1  11.22        111      48           16  ...   65         10   Yes  Yes
2  10.06        113      35           10  ...   59         12   Yes  Yes
3   7.40        117     100            4  ...   55         14   Yes  Yes
4   4.15        141      64            3  ...   38         13   Yes   No"""

df.info()
"""
Data columns (total 11 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   Sales        400 non-null    float64
 1   CompPrice    400 non-null    int64  
 2   Income       400 non-null    int64  
 3   Advertising  400 non-null    int64  
 4   Population   400 non-null    int64  
 5   Price        400 non-null    int64  
 6   ShelveLoc    400 non-null    object 
 7   Age          400 non-null    int64  
 8   Education    400 non-null    int64  
 9   Urban        400 non-null    object 
 10  US           400 non-null    object 
dtypes: float64(1), int64(7), object(3)"""
#dataset does not contains any null values

#we have to convert sales column to categorical data as it is our target column
df['sales_category'] = 'average'
df.loc[df['Sales']<7,'sales_category'] = 'low'
df.loc[df['Sales']>12,'sales_category'] = 'good'

#there are some categorical data that we have to convert into numerical
df['ShelveLoc'].unique()
df['ShelveLoc'] = pd.factorize(df.ShelveLoc)[0]
df['Urban'] = pd.factorize(df.Urban)[0]
df['US'] = pd.factorize(df.US)[0]
df = df.drop('Sales',axis=1)

df.describe()
"""
CompPrice      Income  Advertising  ...   Education       Urban          US
count  400.000000  400.000000   400.000000  ...  400.000000  400.000000  400.000000
mean   124.975000   68.657500     6.635000  ...   13.900000    0.295000    0.355000
std     15.334512   27.986037     6.650364  ...    2.620528    0.456614    0.479113
min     77.000000   21.000000     0.000000  ...   10.000000    0.000000    0.000000
25%    115.000000   42.750000     0.000000  ...   12.000000    0.000000    0.000000
50%    125.000000   69.000000     5.000000  ...   14.000000    0.000000    0.000000
75%    135.000000   91.000000    12.000000  ...   16.000000    1.000000    1.000000
max    175.000000  120.000000    29.000000  ...   18.000000    1.000000    1.000000"""
#data is widely distriduted so we have to normalize it 

#normalization function
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

X = df.drop('sales_category',axis=1)
X = norm_fun(X)
Y = df.sales_category

#split tha data into train and test dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,Y,test_size=0.2)

#build the model for random forest classifier
from sklearn.ensemble import RandomForestClassifier
model  = RandomForestClassifier(n_estimators=20)
#train model
model.fit(x_train,y_train)

#cheking acuuracy score
model.score(x_test,y_test)
"""accuracy of model :- 0.775"""
y_predicted = model.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm
"""
array([[27,  0,  6],
       [ 4,  0,  0],
       [ 5,  0, 38]], dtype=int64)"""

#matplotlib
import matplotlib.pyplot as mt
import seaborn as sns
mt.figure(figsize=(12,7))
sns.heatmap(cm,annot=True)
mt.xlabel('Predicted')
mt.ylabel('Truth')