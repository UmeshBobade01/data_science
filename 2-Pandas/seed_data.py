""" operation on Seed data"""

import pandas as pd
#create data frame from csv file
df = pd.read_csv("C:/2-Dataset/Seeds_data.csv")
df

# to find data types of each columns
df.dtypes

#converting datatypes to best possible data type
df1 = df.convert_dtypes()
df1.dtypes

#converting datatypes to string
df1 = df.astype(str)
df1.dtypes

#dataframe properties
df.shape
df.size

#to find name of columns
df.columns
df.columns.values

#to find index of dataframe
df.index

#generate summary of dataframe
df.info()
df.describe()

#select particular records
df[0:100]

#select particular columns
df[['Area','Type']]

#renaming all columns
df.columns = ['c1','c2','c3','c4','c5','c6','c7','c8']
df

#renaming selected columns
df = df.rename({'c1': 'a', 'c2': 'b','c3':'c'}, axis=1)
df = df.rename({'c4': 'd', 'c5': 'e','c6':'f'}, axis='columns')
df = df.rename(columns={'c7': 'g', 'c8': 'h'})


df = pd.read_csv("C:/2-Dataset/Seeds_data.csv")
df

#droping columns
df1 = df.drop(['Assymetry_coeff'],axis=1)
df1

df1 = df.drop(columns=['len_ker_grove'],axis=1)
df1

df1 = df.drop(labels=['Assymetry_coeff','len_ker_grove'],axis=1)
df1


#droping records using index
df1 = df.drop(df.index[100:])
df1

#drop records using range
df1 = df.drop(range(100,210))
df1

#drop several records
df1 = df.drop([1,2,3,4,5,6,7,8,9,10])
df1

#using inplace
df.drop(df.columns[[5,6]],axis = 1, inplace = True )
df

#slicing using iloc
df1 = df.iloc[0]
df1

df1 = df.iloc[[0,1,2,3]]
df1

df1 = df.iloc[0:10]
df1

df1 = df.iloc[:3,0:2] #[index(:),cols(:)]
df1

#slicing using loc
#we can give column names for slicing
df1 = df.loc[:,'Area':'length']
df1

df1 = df.loc[0:10,'length':]
df1

#queries
print(df.query("Type == 1"))

print(df.query("Area > 15"))


#add new column
df.rename({'Perimeter ':'Perimeter'},axis=1,inplace=True)
df1 = df.assign(half_perimeter = lambda x : x.Perimeter*0.5)
df1


#to get number of columns
no_of_cols = len(df.axes[1])
no_of_cols = df.shape[1]
print("No. of columns::",no_of_cols)

#to get number of rows
no_of_rows = len(df.axes[0])
no_of_rows = df.shape[0]
no_of_rows = len(df.index)
print("No. of rowss::",no_of_rows)

df.shape
#save as csv
df.to_csv("final_seed.csv")
