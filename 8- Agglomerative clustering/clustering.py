"""   Machine Learning Algorithms      """
"""   Unsupervised Learning algorithm  """

#1. Clustering

"""Example 1 university data"""
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

#import file
un1 = pd.read_excel("C:/2-Dataset/University_Clustering.xlsx")
a = un1.describe()

#drop the unwanted columnn here we have column "State" which is useless
un = un1.drop(["State"],axis=1)

# Normalization
#there is lagre scale difference in given columns
#so apply normalization or standardization
#whenever there is mixed data apply normalization
def norm_fun(i):
    x = (i-i.min())/(i.max()-i.min())
    return x

#apply the normalization function to un dataframe
#for all columns except column 0 as it contains the univercity names
#normalized dataset
df_norm = norm_fun(un.iloc[:,1:])
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
#
sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#appling dendrogramagglomerative clustering choosing 3 as clusters from dendrogram
#dendrogram just shows the number of possible clusters

from sklearn.cluster import AgglomerativeClustering
h_complete = AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(df_norm)
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

#assign the series to 'un' dataframe
un['cluster'] = cluster_labels
#add cluster column at index 0
un1 = un.iloc[:,[7,1,2,3,4,5,6]]
#check the un1 dataframe
un1.iloc[:,2:].groupby(un1.cluster).mean()
# from the output cluster 2 has got the highest top 10, lowest accept ratio, 
#best faculty ratio and highest expenses, highest graduates ratio

#save file to csv
un1.to_csv("Univercity.csv",encoding="utf-8")

import os
os.getcwd()


"""Example 2:- Autoinsurance data"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

#import file
df = pd.read_csv("C:/2-Dataset/AutoInsurance.csv")
a = df.describe()

#drop the unwanted columnn here we have column "State" which is useless
df1 = df.drop(["State","Location Code","Marital Status","Policy Type",
               "Policy","Renew Offer Type","Sales Channel","Vehicle Class",
               "Vehicle Size","Gender","EmploymentStatus","Effective To Date",
               "Education","Coverage","Response","Customer"],axis=1)

# Normalization
#there is lagre scale difference in given columns
#so apply normalization or standardization
#whenever there is mixed data apply normalization
def norm_fun(i):
    x = (i-i.min())/(i.max()-i.min())
    return x

#apply the normalization function to un dataframe
#for all columns except column 0 as it contains the univercity names
#normalized dataset
df_norm = norm_fun(df1.iloc[:,1:])
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
#
sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#appling dendrogramagglomerative clustering choosing 3 as clusters from dendrogram
#dendrogram just shows the number of possible clusters

from sklearn.cluster import AgglomerativeClustering
h_complete = AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(df_norm)
h_complete.labels_

cluster_labels = pd.Series(h_complete.labels_)

#assign the series to 'un' dataframe
df1['cluster'] = cluster_labels
#add cluster column at index 0
df1 = df1.iloc[:,[8,0,1,2,3,4,5,6,7]]
#check the un1 dataframe
df1.iloc[:,2:].groupby(df1.cluster).mean()
# from the output cluster 2 has got the highest top 10, lowest accept ratio, 
#best faculty ratio and highest expenses, highest graduates ratio

#save file to csv
un1.to_csv("Univercity.csv",encoding="utf-8")