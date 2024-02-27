""" operation on bank data"""

import pandas as pd
#create data frame from csv file
df = pd.read_csv("C:/2-Dataset/bank_data.csv")
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
df[['age','balance']]

#renaming selected columns
df = df.rename({'age': 'Age', 'balance': 'Balance','loan':'Loan'}, axis=1)
df


#droping columns
df = df.drop(['jotechnician'],axis=1)
df = df.drop(columns=['jostudent'],axis=1)
df = df.drop(labels=['y','jounknown'],axis=1)
df


#droping records using index
df = df.drop(df.index[1000:])
df

#drop records using range
df = df.drop(range(500,1000))
df

#drop several records
df = df.drop([495,496,497,498,499])
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
df1 = df.loc[:,'Age':'Balance']
df1

df = df.loc[0:10,'Balance':]
df

#queries
print(df.query("Loan == 1"))

print(df.query("Age > 50"))


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
df.to_csv("final_bank.csv")
