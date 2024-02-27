# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:18:37 2024

@author: ASUS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from scipy.stats import skew

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("C:/2-Dataset/movies_classification.csv")

#data information
data.head()
data.info()
data.describe()
data.isna().sum()

#EDA
target = data['Start_Tech_Oscar']
sns.countplot(x = target,palette='winter')
plt.xlabel('Oscar_Rate')
#our data is evenly distributed
plt.Figure(figsize=(16,8))
sns.heatmap(data.corr(),annot=True,cmap='YLGnBu',fmt='.2f')
#observations

#
sns.countplot(x = 'Genre',data=data,hue='Start_Tech_Oscar',palette='pastel')
plt.title('0 chances based on ticket class',fontsize=10)
#
sns.countplot(x = '3D_available',data=data,hue='Start_Tech_Oscar',palette='pastel')
plt.title('0 chances based on ticket class',fontsize=10)
#
sns.set_context('notebook', font_scale=1.2)
fig, ax = plt.subplots(2,figsize=(20,13))

plt.suptitle('Distribution of Twitter_hastags and Collection based on target variable',fontsize=20)

ax1 = sns.histplot(x='Twitter_hastags',data=data,
                   hue='Start_Tech_Oscar',kde=True,ax=ax[0],
                   palette='winter')

ax1.set(xlabel= 'Collection',title='Distributionnof Collection based on target variable')

ax2 = sns.histplot(x='Collection',data=data,
                   hue='Start_Tech_Oscar',kde=True,ax=ax[1],
                   palette='winter')

ax2.set(xlabel= 'Collection',title='Distributionnof Collection based on target variable')

plt.show()

#genearate histogram
data.hist(bins=30,figsize=(20,15),color='#005b96')


#checking outliers in the data
#and remove outliers using winsorizer
from feature_engine.outliers import Winsorizer
sns.boxplot(x=data['Twitter_hastags'])
winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = ['Twitter_hastags'])
data['Twitter_hastags'] = winsor.fit_transform(data[['Twitter_hastags']])
sns.boxplot(x=data['Twitter_hastags'])

sns.boxplot(x=data['Marketing expense'])
winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = ['Marketing expense'])
data['Marketing expense'] = winsor.fit_transform(data[['Marketing expense']])
sns.boxplot(x=data['Marketing expense'])

sns.boxplot(x=data['Time_taken'])
winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = ['Time_taken'])
data['Time_taken'] = winsor.fit_transform(data[['Time_taken']])
sns.boxplot(x=data['Time_taken'])

sns.boxplot(x=data['Avg_age_actors'])
winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = ['Avg_age_actors'])
data['Avg_age_actors'] = winsor.fit_transform(data[['Avg_age_actors']])
sns.boxplot(x=data['Avg_age_actors'])

#cheking skewness
skew_df = pd.DataFrame(data.select_dtypes(np.number).columns,columns=['Feature'])
skew_df['Skew'] = skew_df['Feature'].apply(lambda feature: skew(data[feature]))
skew_df['Absolute Skew'] = skew_df['Skew'].apply(abs)
skew_df['Skewed'] = skew_df['Absolute Skew'].apply(lambda x: True if x >= 0.5 else False)
skew_df

#
for column in skew_df.query("Skewed == True")['Feature'].values:
    data[column] = np.log1p(data[column])

data.head()
#encoding
data1 = data.copy()
data1 = pd.get_dummies(data1)
data1.head()

#scaling
data2 = data1.copy()
sc = StandardScaler()
data2[data1.select_dtypes(np.number).columns] = sc.fit_transform(data2[data1.select_dtypes(np.number).columns])
data2.drop(['Start_Tech_Oscar'],axis=1,inplace=True)
data2.head()

#splitting
data_f = data2.copy()
target = data['Start_Tech_Oscar']
target = target.astype(int)
target
X_train, X_test, Y_train, Y_test = train_test_split(data_f,target,test_size=0.2,
                                                    stratify=target,random_state=42)

#modelling
from sklearn.ensemble import AdaBoostClassifier
ada_clf = AdaBoostClassifier(learning_rate=0.02,n_estimators=5000)
ada_clf.fit(X_train,Y_train)

#evalution on testing data
from sklearn.metrics import accuracy_score, confusion_matrix
confusion_matrix(Y_test,ada_clf.predict(X_test))
accuracy_score(Y_test,ada_clf.predict(X_test))