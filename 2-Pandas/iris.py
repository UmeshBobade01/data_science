""" Pandas Operations on iris dataset """
import pandas as pd
df = pd.read_csv("C:/2-Dataset/iris_data.csv")

df.dtypes

df1 = df.convert_dtypes()
df1.dtypes

df1 = df.astype(str)
df1.dtypes

df.shape
df.size

df.columns
df.columns.values

df.index

df.info()
df.describe()

#select particular records
df[0:50]

#select particular columns
df[['5.1','3.5']]

#renaming columns
df.columns = ['c1','c2','c3','c4','c5']
df.columns

#renaming selected columns
df = df.rename({'c1': 'a', 'c2': 'b'}, axis=1)
df = df.rename({'c3': 'c', 'c4': 'd'}, axis='columns')
df = df.rename(columns={'c5': 'e'}) 
df.columns

#droping columns
df1 = df.drop(['a'],axis=1)
df1

df1 = df.drop(columns=['b'],axis=1)
df1

df1 = df.drop(labels=['a','b'],axis=1)
df1

#droping records using index
df1 = df.drop(df.index[100:])
df1

#drop records using range
df1 = df.drop(range(100,149))
df1

#drop several records
df1 = df.drop([0,1,2,3,4,5,6,7,8,9,10])
df1

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
df1 = df.loc[:,'a':'c']
df1

df1 = df.loc[0:10,'b':]
df1

#queries
print(df.query("e == 'Iris-setosa'"))

print(df.query("a > 3"))

#to get number of columns
no_of_cols = len(df.axes[1])
no_of_cols = df.shape[1]
print("No. of columns::",no_of_cols)

#to get number of rows
no_of_rows = len(df.axes[0])
no_of_rows = df.shape[0]
no_of_rows = len(df.index)
print("No. of rowss::",no_of_rows)

#getting the column headers
df.columns
column_headers = list(df.columns.values)
print("Column headers of::",column_headers)


#shuffling records
df1 = df.sample(frac=1)
df1
#gives index to shuffeled data
df1 = df.sample(frac=1).reset_index()
df1
#drop the shuffeled index and not include it in dataframe
df1 = df.sample(frac=1).reset_index(drop=True)
df1

#group by
df1 = df.groupby(['e']).sum()
df1
