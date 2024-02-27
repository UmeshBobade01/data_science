"""
Given is the diabetes dataset. Build an ensemble model to correctly classify
the outcome variable and improve your model prediction by using GridSearchCV.
You must apply Bagging, Boosting, Stacking, and Voting on the dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import stats

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('C:/2-Dataset/Diabeted_Ensemble.csv')

#data information
df.head()
df.info()
df.describe()
df.isna().sum()

#EDA
target = df[' Class variable']
sns.countplot(x = target,palette='winter')

#generating histogram
df.hist(bins=30,figsize=(20,15),color='#005b96')

#cheking for outliers
sns.boxplot(x=df[' Number of times pregnant'])
sns.boxplot(x=df[' Plasma glucose concentration'])
sns.boxplot(x=df[' Diastolic blood pressure'])
sns.boxplot(x=df[' Triceps skin fold thickness'])
sns.boxplot(x=df[' 2-Hour serum insulin'])
sns.boxplot(x=df[' Body mass index'])
sns.boxplot(x=df[' Diabetes pedigree function'])
sns.boxplot(x=df[' Age (years)'])
#it is observed that all columns contains some outliers so 
#we have to remove these outliers

#winsorizer for removing outliers
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = [' Number of times pregnant'])
df[' Number of times pregnant'] = winsor.fit_transform(df[[' Number of times pregnant']])

winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = [' Plasma glucose concentration'])
df[' Plasma glucose concentration'] = winsor.fit_transform(df[[' Plasma glucose concentration']])

winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = [' Diastolic blood pressure'])
df[' Diastolic blood pressure'] = winsor.fit_transform(df[[' Diastolic blood pressure']])

winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = [' Triceps skin fold thickness'])
df[' Triceps skin fold thickness'] = winsor.fit_transform(df[[' Triceps skin fold thickness']])

winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = [' 2-Hour serum insulin'])
df[' 2-Hour serum insulin'] = winsor.fit_transform(df[[' 2-Hour serum insulin']])

winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = [' Body mass index'])
df[' Body mass index'] = winsor.fit_transform(df[[' Body mass index']])

winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = [' Diabetes pedigree function'])
df[' Diabetes pedigree function'] = winsor.fit_transform(df[[' Diabetes pedigree function']])

winsor = Winsorizer(capping_method = 'iqr',tail = 'both',fold = 1.5,variables = [' Age (years)'])
df[' Age (years)'] = winsor.fit_transform(df[[' Age (years)']])

#all outliers are now removed























