
"""EDA""" 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:/2-Dataset/Telco_customer_churn.csv")
df
#######################
#1.column
df.columns
#######################
#2.shape
df.shape  
#There are total 7043 rows and 30 columns in the dataframe


df.dtypes 
# The dataframe is of mixed datatype so we have to find the relationship
# between the columns so we draw the heatmap and pairplot for the understanding

df.isna()
# It does not contain any null value

corr=df.corr()
sns.heatmap(corr)
# The column noof refferrals,tenue of Months,Long distance charges
# ,Monthly gb dowmload,Total Refund ,Total extra data charges,long distance
# charges these columns are corelated

# plot the pairplot tounderstand more about the data
sns.pairplot(df)
#description of the dataframe
a=df.describe()
# there is slight difference in the mean and mesian of some columns and
# and standard deviation is also higher so it contain some outlier 
# plot the boxplot so we understand the outlier conaining coluumns
sns.boxplot(df)
# Total Extra Data Charges and Total Long Distance Charges columns contain 
# the outliers so we will remove or normalize it
df.columns
df.nunique(axis=0)
# we are checking which column is not necserray or
# the column which is  numerical data  that can be place in the datframe
df1=df.drop(['Customer ID','Count', 'Quarter', 'Referred a Friend', 'Offer', 'Phone Service',
       'Multiple Lines', 'Contract','Paperless Billing','Payment Method'],axis=1) 
df1.columns
df1.shape

df_dummies=pd.get_dummies(df1)
df_dummies.columns

v=df_dummies.drop(['Device Protection Plan_No','Premium Tech Support_No','Online Security_No',
                 'Streaming TV_Yes','Streaming Movies_No','Streaming Music_Yes',
                 'Unlimited Data_No','Internet Service_No','Internet Type_None','Online Security_No'
                 ,'Online Backup_No'],axis=1)
#there are scale differenece between the column value so we 
#can remove that value from the Dataframe
# by using the normalization or standardization
#so we can use the normalization
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now we can apply this noramlization function to df2 dataframe for all the rows and column from 1 until end
# since 0 th column has Universcity name hence skipped
df2= norm_fun(v.iloc[:,:])
#here we can use the data make it as noramlize that is in the 0 and 1 form and we can 
# now we can descrine the df2 after we can make it in the normalize form
b=df2.describe()
#####################
#before you can applying the clustering you need to plot dendrogram first
# now to create the dendrogram , we need to measure distance
#we have import the linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hierarchical or aglomerative clustering
#ref the help for linkage
p=linkage(df2,method="complete",metric="euclidean")
plt.figure(figsize=(16,8));
plt.title("Hierarchical Clustering Dendrogram");
plt.xlabel("phone");
plt.ylabel("internet_servise")
#ref help of dendogram
#sch.dendrogram
sch.dendrogram(p,leaf_rotation=0,leaf_font_size=10)
plt.show()

#apply  agglomertive clustering choosing 5 a clusters from dendrogram
from sklearn.cluster import AgglomerativeClustering
dendo=AgglomerativeClustering(n_clusters=5,linkage='complete',affinity='euclidean').fit(df2)
#apply labels to the cluster
dendo.labels_
cluster_labels=pd.Series(dendo.labels_)
#assign this series to df2 dataframe as column and name the column as 'cluster'
df['cluster']=cluster_labels
df.drop('cluster',axis=1)
########################################
df.shape
#we want to realocate th ecolumnn 7 to 0 th postion
df=df.iloc[:,[1,2,3,4,5,6,7,8,9,10]]
#now check the Dataframe
df.iloc[:,:].groupby(df.cluster).mean()