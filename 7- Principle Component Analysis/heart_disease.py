import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read the csv file and create dataframe
df=pd.read_csv('PCA/heart_disease.csv')
df

#EDA
#check the no. of columns and rows
df.shape
#dataset contains total 303 rows and 14 columns

#find the columns in dataset
df.columns
'''
Index(['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'],
      dtype='object')
'''

#load the sample data to have quick view
df.head()

#find out the data types of columns
df.dtypes
'''
age           int64
sex           int64
cp            int64
trestbps      int64
chol          int64
fbs           int64
restecg       int64
thalach       int64
exang         int64
oldpeak     float64
slope         int64
ca            int64
thal          int64
target        int64
dtype: object

The all the columns of Numeric Type
'''

#generate 5 number summary
a=df.describe()
a
# Observe that the diffrence between mean and meadian is nearly same but have somewhat
# diffrenece and also the standard deviation is not near to zero its value is more


#Check for the null values
n=df.isnull()
n.sum()
#There is no null value is present in the dataset

# Check for the outlier
# Plot a boxplot to check whether it contain an outlier or not
import seaborn as sns
sns.boxplot(df)
# the trestbps,chol and thalach column contain the outlier

#generate histogram
sns.histplot(df)

#find correlation
corr=df.corr()
sns.heatmap(corr)
# As there is 2-3 columns showing the darkcolour so they arestrictly co-related to each other
# So there is outlier is present and also the the column shows skewness propery
# and there is scale difference in mean and std so we use standardization technique as we are going to use 

"""Kmeans algorithm without PCA"""
from sklearn.cluster import KMeans
def norm_func(i):
    x = (i-i.min())/(i.max()-i.min())
    return x
#Now apply this normalization function to Univ datframe for all the row
df_norm = norm_func(df.iloc[:,1:])
#What will be ideal cluster number, will it be 1,2 or 3


TWSS  = []
k = list(range(2,8))
for i in k:
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)#total within sum of square

TWSS 
#As k value incteases the TWSS value decreases 
plt.plot(k,TWSS,'ro-')
plt.xlabel("No_of_clusters")
plt.ylabel("Total_within_SS")
#select the no. of clusters by using elbow method
model=KMeans(n_clusters=4)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
df['cluster']=mb
df.head()

df.iloc[:,:].groupby(df.cluster).mean()


""" Perform PCA on data to extract 3 principle components"""
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import scale

#Considering only numerical data 
df.data=df.iloc[:,:]

#Normalizing the numerical data
df_normal = scale(df.data)
df_normal

pca = PCA(n_components = 3)
pca_values = pca.fit_transform(df_normal)

#The amount of variance that each PCA explains is 
var = pca.explained_variance_ratio_
var

#cumulative variance 
var1 = np.cumsum(np.round(var, decimals = 4 )*100)
var1

#Variance plot for PCA components obtained 
plt.plot(var1, color = 'red')

#PCA scores 
pca_values

pca_data = pd.DataFrame(pca_values)
pca_data.columns = 'comp0','comp1','comp2'

#Scatter diagram
import matplotlib.pylab as plt 
ax = pca_data.plot(x='comp0',y='comp1',kind='scatter',figsize=(12,8))


"""Kmeans algorithm without PCA"""
from sklearn.cluster import KMeans
def norm_func(i):
    x = (i-i.min())/(i.max()-i.min())
    return x
#Now apply this normalization function to datframe for all the row
df_norm = norm_func(pca_data.iloc[:,:])
#What will be ideal cluster number, will it be 1,2 or 3


TWSS  = []
k = list(range(2,8))
for i in k:
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)#total within sum of square

TWSS 
#As k value incteases the TWSS value decreases 
plt.plot(k,TWSS,'ro-')
plt.xlabel("No_of_clusters")
plt.ylabel("Total_within_SS")
#select the number of clusters by using elbow method

model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
pca_data['cluster']=mb
pca_data.head()

pca_data.iloc[:,:].groupby(pca_data.cluster).mean()
