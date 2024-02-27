# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:22:50 2023

@author: Atharv Joshi 
"""
import pandas as pd
import matplotlib.pyplot as plt 

df=pd.read_excel('EastWestAirLines.xlsx')
df
df.columns

#there is an #Id column which is not affect on data

df_new=df.drop(['ID#'],axis=1)
a=df_new.describe()

#There is  a large scale in between mean and the Standard Deviation so we 
# normalize it

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#It normalize the all the columns and make values between 0 and 1
#apply above function to the dataframe
df_norm=norm_fun(df_new)

v=df_norm.describe()

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

#appying agglomerative clustering choose 1 as a cluster from dendogram

# In dedrogram is not show the clustering it only shows how many clusters are there

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=2,linkage='complete',affinity='euclidean').fit(df_norm)

#apply labels to the cluster
h_complete.labels_
# so these all are in the form of array we have to convert the Series
cluster_labels=pd.Series(h_complete.labels_)

df_new['clust']=cluster_labels
df_new

