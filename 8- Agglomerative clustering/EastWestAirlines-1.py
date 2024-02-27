"""
"""
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df=pd.read_csv('C:/2-Dataset/EastWestAirlines.csv')
df

"""EDA"""
df.head()

df.shape
#the dataset contain totally 3999 rows and 12 columns

df.columns

a=df.describe()
#It is observe that the difference between mean and median is small 
# but there is scale difference in the standard deviation 

#Check the datatype of columns
df.dtypes
#we observed that the all the columns are of the integer type
# check the relation between the columns so we draw the heatmap

corr=df.corr()
sns.heatmap(corr)
# we observe that the heatmap having the same colour at diagonal so it
# indicate that the data is arranged in particular pattern and it is almost
# Normally distributted

# To understand the more about data we plot the pairplot

sns.pairplot(df)

#we observe that the most of the columns are corelate with each other
# we drae the histogram for all the columns for checking the normalzation

sns.histplot(df.Balance,kde=True)
#Data is right skew
sns.histplot(df.Qual_miles,kde=True)
#Data is normally distributed
sns.histplot(df.cc1_miles,kde=True)
#data is bi_model
#from above we conclude that there is skewness in data

sns.boxplot(df)
# There is an outlier present in the Balance and the Bonus_miles
#There is  a large scale in between mean and the Standard Deviation so we 
# normalize it

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

#It normalize the all the columns and make values between 0 and 1
#apply above function to the dataframe
df_norm=norm_fun(df)

df_norm.columns
sns.histplot(df_norm.Balance,kde=True)
v=df_norm.describe()
# we see that the mean and median values are same so the data is norrmally
#distributed
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

df['clust']=cluster_labels
df

