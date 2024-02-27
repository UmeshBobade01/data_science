import pandas as pd
df=pd.read_csv("C:/2-Dataset/ethnic diversity.csv")
df.dtypes
#salaries data type is float let us convert into int 
#df1=df.Salaries.astype(int)
df.Salaries =df.Salaries.astype(int)
df.dtypes
#now the data type of Salaries is int 
#Similarly age data type must be float which is int 
df.age=df.age.astype(float)
df.dtypes
########################################################

df_new = pd.read_csv("C:/2-Dataset/ethnic diversity.csv")
df_new

duplicate = df_new.duplicated()
#output of this function is single column 
#if there is duplicate records output - True 
#if there is no duplicate record output - False 
#Series will be created
duplicate
sum(duplicate)
#output will be 0 
#Now let us import another dataset
df_new1 = pd.read_csv("C:/2-Dataset/mtcars_dup.csv")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)
#There are 3 duplicate records 
#row 17 is duplicate of row  2 like wise you get 3 duplicate records 

############################################################

#outliers treatment 
import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/2-dataset/ethnic diversity.csv")
#Now let us find outliers in Salaries 
sns.boxplot(df.Salaries)
#There are outliers 
#Let us check outliers in age column 
sns.boxplot(df.age)
#There are no outliers 
#Let us calculate IQR
IQR =df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#have oserved IQR in ariable explorer 
#no, because IQR is in capital 
#treated as constant 
IQR
#but if we will try as I, Iqr then it is showing 
#I =df.Salaries.quantile(0.75) -df.Salaries.quantile(0.25)

lower_limit = df.Salaries.quantile(0.25)- 1.5*IQR
upper_limit=df.Salaries.quantile(0.75) + 1.5*IQR
#Now if you will check the lower limit of 
#Salary, it is -19446.9675
#There is negative salary 
#so make it as 0
#how to make it 
#go to variable explorer and make it 0

#################################################################

#Trimming 
import numpy as np
outliers_df=np.where(df.Salaries>upper_limit,True,np.where(df.Salaries<lower_limit, True, False))
#you can check outliers_df column in variable explorer 
df_trimmed = df.loc[~outliers_df]
df.shape
#(310,13)
df_trimmed.shape
#(306,13)

#################################################################

#Replacement Technique 
#Drawback of trimming technique is we are losing the data 
df =pd.read_csv("C:/2-Dataset/ethnic diversity.csv")
df.describe()

#record no. 23 has got outliers
#map all the outlier values to upper limit 
df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,upper_limit, np.where(df.Salaries<lower_limit, lower_limit, df.Salaries)))
#if the values are greater than Upper_limit 
#map it to upper limit, and less than lower_limit
#map it to lower limit, if it is within the range 
sns. boxplot(df_replaced[0])

#################################################################

#winsorizer
from feature_engine.outliers import Winsorizer
winsor = Winsorizer(capping_method = 'iqr',
                    tail = 'both',
                    fold = 1.5,
                    variables = ['Salaries'])


df_t = winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])

#################################################################

#zero variance and near zero variance
#if there is no variance in the feature ML will not get any intelligence
#so it is better to ignore those feature

import pandas as pd
df = pd.read_csv("C:/2-Dataset/ethnic diversity.csv")
df.var()

#below code will give True if there is variance
df.var()==0
df.var(axis=0)==0

#################################################################

#missing values
import pandas as pd 
import numpy as np

df = pd.read_csv("C:/2-Dataset/income.xls",names=["name","income"],skiprows=[0])
df

#no null values in data so we have make the NaN values by our own
df["income"][3]=np.NaN
df

#mean imputation
#when there is no outliers then missing values replaced with mean values of that column
df_new = df.fillna(df.income.mean())
df_new

#median imputation
#when there are outliers then missing values replaced with median value of that column
df_new = df.fillna(df.income.median())
df_new

#handling missing values using imputer in sklearn library
df = pd.read_csv("C:/2-Dataset/modified ethnic.csv")
df

#find how many null values in each column
df.isna().sum()

#create an imputer that creates NaN values
#mean and median is used for numeric data
#mode is used for discrete data(position,sex,MaritalDes) 
from sklearn.impute import SimpleImputer
mean_imputer = SimpleImputer(missing_values=np.nan,strategy='mean')

#fill the missing values with using mean imputer
df['Salaries']=pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))

#check whether the missing values are filled or not
df['Salaries'].isna().sum()

#################################################################

#discritization
import pandas as pd
data = pd.read_csv("C:/2-Dataset/ethnic diversity.csv")

#to view the sample data(above 5 records)
data.head()
#gives the information about each column like how much records and how much null values in each column
#and data type of each column
data.info()

#gives five number summary
data.describe()

#binning
data["Salaries_new"] = pd.cut(data["Salaries"],
                              bins=[min(data.Salaries),
                                    data.Salaries.mean(),
                                    max(data.Salaries)],
                              labels=["low","high"])

data.Salaries_new.value_counts()

data["Salaries_new"] = pd.cut(data["Salaries"],
                              bins=[min(data.Salaries),
                                    data.Salaries.quantile(0.25),
                                    data.Salaries.mean(),
                                    data.Salaries.quantile(0.75),
                                    max(data.Salaries)],
                              labels=["group1","group2","group3","group4"])

data.Salaries_new.value_counts()

#################################################################

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

df = pd.read_csv("C:/2-Dataset/animal_category.csv")
df

df.shape
df = df.drop(["Index"],axis=1)

df_new = pd.get_dummies(df)
df_new
df_new.shape
#here we will get 30 rows and 14 columns

#delete gender_male and homely_yes columns
df_new = df_new.drop(["Gender_Male","Homly_Yes"],axis=1,inplace=True)
df_new

#rename gender_female and homly_no columns as gender and homly resp.
df_new = df_new.rename(columns={"Gender_Female":'Gender',"Homly_No":'Homly'})
df_new.columns

##################################################################

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

df = pd.read_csv("C:/2-Dataset/ethnic diversity.csv")
df

df.shape
df.info()

df_new = pd.get_dummies(df["Race"])
df_new
df_new.shape

###############second method to convert data in dummy ver#############################

#using encoding create dummy variable
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()

data=pd.read_csv("C:/2-Dataset/ethnic diversity.csv")
data
data.columns

#inn columns we identify that salary and age column at last thats why we 
#take it first
#for that we inplace function

data=data[['Employee_Name', 'EmpID', 'Position', 'State', 'Zip', 'Sex',
       'MaritalDesc', 'CitizenDesc', 'EmploymentStatus', 'Department', 'Race']]


enc_data=pd.DataFrame(enc.fit_transform(data.iloc[:,2:]).toarray())
enc_data

###########################################################

#lable encoder
#disavantage-> last col not having a name
from sklearn.preprocessing import LabelEncoder

lableencoder=LabelEncoder()

x=data.iloc[:,0:9]
y=data['Race']
data.columns

x['Sex']=lableencoder.fit_transform(x['Sex'])

x['MaritalDesc']=lableencoder.fit_transform(x['MaritalDesc'])

x['CitizenDesc']=lableencoder.fit_transform(x['CitizenDesc'])

#lable necoder
y=lableencoder.fit_transform(y)
#this is going to create an array, hence convert
#it back to dataframe
y=pd.DataFrame(y)

df_new=pd.concat([x,y],axis=1)
df_new
df_new=df_new.rename(columns={0:'Race'})
df_new

###############################################################
#standardization and normalization

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

d=pd.read_csv("C:/2-Dataset/ethnic diversity.csv")
a=d.describe()
a

#initialize the scalar
scalar=StandardScaler()
df=scalar.fit_transform(d)
dataset=pd.DataFrame(df)

res=dataset.describe()
res
#here if you check res 

""" Standardisation """

#one hot encoder
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("C:/2-Dataset/mtcars.csv")
df.describe()

a = df.describe()

#initialize the scaler
scalar = StandardScaler()
df1 = scalar.fit_transform(df)
dataset = pd.DataFrame(df1)
res = dataset.describe()
#

###########################################################

#normalization
df = pd.read_csv("C:/2-Dataset/ethnic diversity.csv")
df.columns
#delete useless columns
df.drop(["Employee_Name","EmpID","Zip"],axis=1,inplace=True)
#read max and min valuesof salaries and age
a1 = df.describe()
#there is large diff in max and min values of
#hence we need normalization

ethnic = pd.get_dummies(df,drop_first=True)
ethnic

def norm_fun(i):
    x = (i-i.min())/(i.max()-i.min())
    return x

df_norm = norm_fun(ethnic)
b = df_norm.describe()
b

############################################################





















