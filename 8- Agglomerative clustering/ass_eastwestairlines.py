# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 08:36:11 2023

@author: nisha
"""



#1.	Perform clustering for the airlines data to obtain optimum number of clusters. 
#Draw the inferences from the clusters obtained. 
#Refer to EastWestAirlines.xlsx dataset.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
airline1=pd.read_excel("C:/dataset/EastWestAirlines.xlsx")
airline1
a=airline1.describe()


airline=airline1.drop(['ID#'],axis=1)

def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm =norm_func(airline.iloc[:,1:])
b=df_norm.describe()

from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

z=linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(20,15));
plt.title("Hierarchical clustering dendrogram")
plt.xlabel('Index')
plt.ylabel('Distance')

sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=5,linkage='complete',affinity='euclidean').fit(df_norm)

h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
airline['clust']=cluster_labels
#new_univ=airline.iloc[:,[7,1,2,3,4,5,6]]
airline.iloc[:,2:].groupby(airline.clust).mean()


airline1.to_csv('Airline_final.csv',encoding='utf8')

import os
os.getcwd()


TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_) #total within sum of square


TWSS
#as k value increses the TWSS value decreases
plt.plot(k,TWSS,'ro-');
plt.xlabel('No_of clusters');
plt.ylabel("total within SS")


model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)

###################################################################################