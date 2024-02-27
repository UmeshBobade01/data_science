""" operation on crime data"""

import pandas as pd
#create data frame from csv file
df = pd.read_csv("C:/2-Dataset/crime_data.csv")
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
df[0:10]

#select particular columns
df[['Murder','Assault']]


#renaming selected columns
df = df.rename({'Unnamed: 0': 'City'}, axis=1)
df = df.rename({'Assault': 'No. of Assaults', 'UrbanPop': 'Urban Pop'}, axis='columns')
df = df.rename(columns={'Rape': 'No. of Rapes'})
df

#droping columns
df1 = df.drop(['Urban Pop'],axis=1)
df1 = df.drop(columns=['Urban Pop'],axis=1)
df1 = df.drop(labels=['Urban Pop'],axis=1)
df1


#droping records using index
df1 = df.drop(df.index[41:])
df1

#drop records using range
df1 = df.drop(range(41,50))
df1

#drop several records
df1 = df.drop([41,42,43,44,45,46,47,48,49])
df1

#using inplace
df.drop(df.columns[[3,4]],axis = 1, inplace = True )
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
df1 = df.loc[:,'City':'No. of Assaults']
df1

df1 = df.loc[0:10,'No.of Murders':]
df1

df
#queries
print(df.query("City == 'Texas'"))

#add new column
df = df.assign(total_crimes = lambda x : x.Murder + x.Assault + x.UrbanPop + x.Rape)
df


#to get number of columns
no_of_cols = len(df.axes[1])
no_of_cols = df.shape[1]
print("No. of columns::",no_of_cols)

#to get number of rows
no_of_rows = len(df.axes[0])
no_of_rows = df.shape[0]
no_of_rows = len(df.index)
print("No. of rowss::",no_of_rows)

#save as csv
df.to_csv("final_crime.csv")
