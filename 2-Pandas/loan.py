""" operation on loan data"""

import pandas as pd
#create data frame from csv file
df = pd.read_csv("C:/2-Dataset/loan.csv")
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
df[['id','member_id']]


#renaming selected columns
df = df.rename({'id': 'ID', 'member_id': 'Member_ID'}, axis=1)
df = df.rename({'id': 'ID', 'member_id': 'Member_ID'}, axis='columns')
df = df.rename(columns={'id': 'ID', 'member_id': 'Member_ID'})
df

#droping columns
df = df.drop(['dti_joint','annual_inc_joint'],axis=1)
df

df = df.drop(columns=['open_acc_6m'],axis=1)
df

df = df.drop(labels=['open_il_6m','open_il_12m'],axis=1)
df

df.shape

#droping records using index
df = df.drop(df.index[1000:])
df

#drop records using range
df = df.drop(range(500,1000))
df

#drop several records
df = df.drop([496,497,498,499])
df

#using inplace
df.drop(df.columns[[56,57]],axis = 1, inplace = True )
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
df = df.loc[:,:'application_type']
df

df1 = df.loc[0:10,'id':'loan_amnt']
df1

#queries
print(df.query("loan_amnt > 5000"))

print(df.query("grade =='A'"))


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
df.to_csv("final_loan.csv")
