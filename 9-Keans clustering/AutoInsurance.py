# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 16:38:43 2023

@author: Atharv Joshi
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('AutoInsurance.csv')
df

df.columns
a=df.describe()
df.drop(['Education','Customer','Policy'],axis=1)

df_new=pd.get_dummies(df)
df_new.columns
v=df_new.drop(df_new.loc[:,'Customer_AA10041':],axis=1)
# There is scale difference in columns so we normalize or standardized it
#Whenever there is mixed data we use normalizaion 

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#It normalize the all the columns and make values between 0 and 1
#apply above function to the dataframe
df_norm=norm_fun(v)

df_norm

# we can check the scale of the df dataframe which is between 0 and 1

b=df_norm.describe()
# we can observe that the min() value is 0 and that of max value is 1 after 
# Normalizaion

#For visualzing the cluster of  the above dataframe we  have to draw
# Dendodron first then we cluster the datapoints

from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

# linkage function give the hierarchical and Agglomotive clustering
 

z=linkage(df_norm,method='complete',metric='euclidean')

plt.figure(figsize=(15,8))
plt.title('Hierarchical Clustering')
plt.xlabel('Index')
plt.ylabel('Disance')
#sch is help to draw 
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()