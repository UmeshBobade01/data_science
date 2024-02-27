#Assingment
"""
Q1. 1.	Perform clustering for the airlines data to obtain optimum number of clusters. 
Draw the inferences from the clusters obtained. Refer to EastWestAirlines.xlsx dataset."""

import pandas as pd
import matplotlib.pyplot as plt

#import file
df = pd.read_csv("C:/2-Dataset/EastWestAirlines.csv")
df.columns
a = df.describe()

#drop the unwanted columnn
df1 = df.drop(["ID#","Award?"],axis=1)

# Normalization
def norm_fun(i):
    x = (i-i.min())/(i.max()-i.min())
    return x

#normalized dataset
df_norm = norm_fun(df1.iloc[:,:])
#the values are get scaled between 0 to 1
b = df_norm.describe()

# Generate dendrogram
#before applying clusters you need to plot dendrogram first
#to create dendrogram we need to measure distance and we have to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

#linkage function gives us clustering type i.e. hierarchical or agglomerative
z = linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(15,8))
plt.title("Heirarchical Clustering Dendrogram")
plt.xlabel("Index")
plt.ylabel("Distance")

#plot dendrogram
sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()


from sklearn.cluster import AgglomerativeClustering
h_complete = AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(df_norm)
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

#assign clusters column to dataframe
df1['cluster'] = cluster_labels
#
summary = df1.iloc[:,:].groupby(df1.cluster).mean()

"""Q2. Perform clustering for the crime data and identify the number of clusters            
formed and draw inferences. Refer to crime_data.csv dataset."""

cd = pd.read_csv("C:/2-Dataset/crime_data.csv")
a = cd.describe()

def norm_fun(i):
    x = (i-i.min())/(i.max()-i.min())
    return x


df_norm = norm_fun(cd.iloc[:,1:])

b = df_norm.describe()

# Generate dendrogram
#before applying clusters you need to plot dendrogram first
#to create dendrogram we need to measure distance and we have to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

#linkage function gives us clustering type i.e. hierarchical or agglomerative
z = linkage(df_norm,method='complete',metric='euclidean')
plt.figure(figsize=(15,8))
plt.title("Heirarchical Clustering Dendrogram")
plt.xlabel("Index")
plt.ylabel("Distance")
#
sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#appling dendrogramagglomerative clustering choosing 3 as clusters from dendrogram
#dendrogram just shows the number of possible clusters

from sklearn.cluster import AgglomerativeClustering
h_complete = AgglomerativeClustering(n_clusters=5,linkage='complete',affinity='euclidean').fit(df_norm)
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

#assign the series to 'un' dataframe
cd['cluster'] = cluster_labels
#
summary = cd.iloc[:,1:].groupby(cd.cluster).mean()


"""Q3 Perform clustering analysis on the telecom data set.
The data is a mixture of both categorical and numerical data.
It consists of the number of customers who churn out.
Derive insights and get possible information on factors that may affect the churn decision.
Refer to Telco_customer_churn.xlsx dataset."""

import pandas as pd
import matplotlib.pyplot as plt

tcc = pd.read_csv("C:/2-Dataset/Telco_customer_churn.csv")
tcc.nunique(axis=0)
a = tcc.describe()

#delete useless columns
tcc1 = tcc.drop(["Count","Quarter"])