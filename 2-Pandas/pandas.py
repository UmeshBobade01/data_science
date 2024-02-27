"""Pandas Series"""

# creating series without index
import pandas as pd
s1 = pd.Series([145, 142, 38, 13], name='Songs')
s1.index  # for checking index
s1  # to see the contents of series


# creating series with index
# index can be numbers or string
s2 = pd.Series([145, 142, 38, 13], name='Songs', index=['Paul', 'John', 'George', 'Ringo'])
s2.index
s2


# read files
# csv file
f1 = pd.read_csv("C:/2-Dataset/age.csv")
f1
# excel file
f2 = pd.read_excel("C:/2-Dataset/Bahaman.xlsx")
f2


# accesing series elements
s = pd.Series([22, 3, 5, 18], index=['1968', '1969', '1970', '1970'], name='songs')
s
s['1968']
s['1970']
s[3]


# iterating through series
s = pd.Series([22, 3, 5, 18], index=['1968', '1969', '1970', '1970'], name='songs')
for i in s:
    print(i)

#updating in series
s = pd.Series([22, 3, 5, 18], index=['1968', '1969', '1970', '1970'], name='songs')
s['1968'] = 20
s['1968']
s

# deleting from series
s = pd.Series([22, 3, 5, 18], index=['1968', '1969', '1970', '1970'], name='songs')
del s['1968']
s

# counting mean of elements
s = pd.Series([22, 3, 5, 18], index=['1968', '1969', '1970', '1970'], name='songs')
s.mean()



s = pd.Series([145, None, 38, 13], name='Songs',index=['Paul', 'John', 'George', 'Ringo'])

s.dtypes  # for identifying datatype

pd.to_numeric(s.apply(str))
# gives error

pd.to_numeric(s.astype(str), errors='coerce')
# this willgive NaN for None record

s.fillna(-1)
# this will replace NaN or None by -1

s.dropna()
# this will remove all records which contains None or NaN value

s1 = pd.Series([14, 67, 48, 33], name='Songs', index=['ram', 'shyam', 'sam', 'radhe'])
st = s.append(s1)
# this will add series s1 to s
st

"""Dataframe"""
# it is 2D data structure which contains rows and columns
pd.__version__  # check the pandas version

# create dataframe without column names
tech = [['spark', 20000, '10 days'],['pandas', 10000, '4 days']]
df = pd.DataFrame(tech)
print(df)


# creating dataframe with column name
tech = [['spark', 20000, '10 days'], ['pandas', 10000, '4 days']]
column = ['course', 'fees', 'duration']
row = ['a', 'b']
df1 = pd.DataFrame(tech, columns=column, index=row)
print(df1)

# display data types
df1.dtypes


# creating dataframe from dictonary
tech2 = {
    "Courses": ['spark', 'pyspark', 'hadoop', 'python', 'java', 'cloud'],
    "Fees": [10000, 10000, 5000, 15000, 20000, 30000],
    "Duration": ['10 days', '15 days', '5 days', '30 days', '90 days', '20 days'],
    "Discount": [10, 14, 8, 15, 20, 5]
}

df2 = pd.DataFrame(tech2)
print(df2)
print(df2.dtypes)

# change all types to best possible type
df3 = df2.convert_dtypes()
print(df3.dtypes)

# change all columns to same type
df3 = df2.astype(str)
print(df3.dtypes)

# to change data type of specific columns
df3 = df2.astype({"Fees": int, "Discount": float})
print(df3.dtypes)

# convert data types of selected columns in th list
df = pd.DataFrame(tech2)
df.dtypes
cols = ["Fees", "Discount"]
df[cols] = df[cols].astype("float")
df.dtypes


# ignore errors
df = df.astype({"Courses": int}, errors='ignore')
df.dtypes

#raise errrors
df = df.astype({"Courses": int}, errors='raise')

# save the dataframe into files
tech2 = {
    "Courses": ['spark', 'pyspark', 'hadoop', 'python', 'java', 'cloud'],
    "Fees": [10000, 10000, 5000, 15000, 20000, 30000],
    "Duration": ['10 days', '15 days', '5 days', '30 days', '90 days', '20 days'],
    "Discount": [10, 14, 8, 15, 20, 5]
}

df = pd.DataFrame(tech2)
df

# save to csv
df.to_csv("course.csv")


# dataframe properties
tech2 = {
    "Courses": ['spark', 'pyspark', 'hadoop', 'python', 'java', 'cloud'],
    "Fees": [10000, 10000, 5000, 15000, 20000, 30000],
    "Duration": ['10 days', '15 days', '5 days', '30 days', '90 days', '20 days'],
    "Discount": [10, 14, 8, 15, 20, 5]
}

row = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6']
df = pd.DataFrame(tech2, index=row)
print(df)

# to show number of cols ands rows
df.shape
#(6, 4)

# to show number of blocks=cols*rows
df.size
# 24

# to display column names
df.columns
#Index(['Courses', 'Fees', 'Duration', 'Discount'], dtype='object')
df.columns.values
#array(['Courses', 'Fees', 'Duration', 'Discount'], dtype=object)

# to display name of rows or index
df.index
#Index(['r1', 'r2', 'r3', 'r4', 'r5', 'r6'], dtype='object')

# to display data types of all cols
df.dtypes
"""Courses     object
Fees         int64
Duration    object
Discount     int64
dtype: object"""

df.info
# accessing particular column elements
df[['Fees']]
df[['Fees', 'Courses']]

# to access particular records
df[2:4]

# access certain cells from duration
df['Duration'][2]

# operation on column or to change values in cols
df['Fees'] = df['Fees']-500
df['Fees']

# it will give summary about all cols
df.describe()
"""           Fees   Discount
count      6.00000   6.000000
mean   14500.00000  12.000000
std     8944.27191   5.403702
min     4500.00000   5.000000
25%     9500.00000   8.500000
50%    12000.00000  12.000000
75%    18250.00000  14.750000
max    29500.00000  20.000000"""


df = pd.DataFrame(tech2, index=row)
df
# renaming all columns
df.columns = ['a', 'b', 'c', 'd']
df

# renaming particular columns
df = pd.DataFrame(tech2, index=row)
df.columns = ['a', 'b', 'c', 'd']
df = df.rename({'a': 'c1', 'b': 'c2'}, axis=1)
df = df.rename({'c': 'c3', 'd': 'c4'}, axis='columns')
df = df.rename(columns={'a': 'c1', 'b': 'c2'})
df

############################################
#DROPING OF ROWS 
############################################

#Drop DataFrame rows and columns 
df = pd.DataFrame(tech2, index = row)
df

#Drop rows by labels 
df1 = df.drop(['r1','r2'])
df1

#Delete rows by position or index
df1= df.drop(df.index[1])
df1
#Delete rows by index range 
df1 = df.drop(df.index[2: ])
df1

#when you have default indexs for rows 
df = pd.DataFrame(tech2)
df1 = df.drop(0)
df1
df = pd.DataFrame(tech2)
df1 = df.drop([0,3])  #will delete row o and 3
df1
df1 = df.drop(range(0,2))   #will delete row o and 1 
df1

################################
#DROPING OF COLUMNS          IMP Interv
################################

import pandas as pd
tech = {
        "Courses":['spark','pyspark','hadoop','python','java','cloud'],
        "Fees":[10000,10000,5000,15000,20000,30000],
        "Duration":['10 days','15 days','5 days','30 days','90 days','20 days'],
        "Discount":[10,14,8,15,20,5]
        }


df = pd.DataFrame(tech)
df
#Drop column by name 
#drop fee column 
df2= df.drop(['Fees'],axis=1)
df2
#Explicitly using parameter name 'label'
df2=df.drop(labels=['Fees'], axis = 1)

#Alternatively you can also use columns instead of labels 
df2=df.drop(columns=['Fees'], axis = 1)  # when we are deleting columns then give axis = 1 and for row give 0

###############
#Drop colum by index
print(df.drop(df.columns[1],axis = 1))

df = pd.DataFrame(tech)

##################################################
#using implace = True 
#till we use the df2=df._____ it means we were doing the operation on the instance 
#but by using implace =True we can directly change the original dataset 

df.drop(df.columns[2],axis = 1, inplace = True )
df
###################################################
#Drop two or more columns by index 
df = pd.DataFrame(tech)
df2=df.drop(df.columns[[0,1]], axis = 1 )

###################################################
#when we want to delete mor e than one index that may be col or row
#for that we use double []  i.e [[]]
###################################################

#Drop columns from list of columns ----going to use several time 
df = pd.DataFrame(tech)
liscol = ['Courses','Fees']
df2 = df.drop(liscol, axis = 1)
df2

#################################################
#there r 2 ways to extract the particulat part of dataframe
#by using labels i.2 names use loc
#by using index use iloc 
#imp    10/10
##########################
import pandas as pd
tech = ({
        "Courses":['spark','pyspark','hadoop','python','java','cloud'],
        "Fees":[10000,10000,5000,15000,20000,30000],
        "Duration":['10 days','15 days','5 days','30 days','90 days','20 days'],
        "Discount":[10,14,8,15,20,5]
        })
row=['r1','r2','r3','r4','r5','r6']
df = pd.DataFrame(tech, index = row)
df

#df.iloc[startrow : endrow, startcolum : endcolum]
#iloc works like list slicing 
df = pd.DataFrame(tech,index=row)
#below are quick example
df2=df.iloc[:, 0:2]
df2
#this line use slicing operator to get DataFrame 
#items by index 
#the first slice [:] indicates to return all rows 

df2= df.iloc[2]    #single [] will return the column 
df2

df = pd.DataFrame(tech,index=row)
df2 = df.iloc[[2,3,4]]     #double [[]] will return the rows
df2

df2 = df.iloc[1:3]   #select row by integer index range 
df2

df2 = df.iloc[:1]    #select first row 
df2

df2 = df.iloc[:3]    #select first three row 
df2

df2 = df.iloc[-1:]    #select  last row 
df2

df2 = df.iloc[-3:]   #select last 3 row 
df2

df2 = df.iloc[::2]   #select alternate rows 
df2

###########################################
#select row by Index Labels 
df2 = df.loc['r2']    #select row by label
df2

df2 = df.loc[['r2','r3','r5']]    #select rows by index label 
df2

df2 = df.loc['r1':'r5']     #select rows by label index range 
df2

df2 = df.loc['r0':'r4':2] #select rows in range of 2
df2

df2 = df.loc['r0':'r4','Duration':]
df2
###########################################
#using loc[] to take colum slices 


#loc[]syntax to slice columns
#df.loc[rows(start:stop),cols(start:stop:step)]
#selecte multiple columns

df2 = df.loc['r0':'r4','Duration':]
df2

df2 = df.loc[:, ['Courses','fees','Discount']]
df2

df2 = df.loc[:, 'fees':'Discount']
df2

df2 = df.loc[:,'Duration':]
df2

df2 = df.loc[:,:'Duration']
df2


#Queries
import pandas as pd
tech = ({
        "Courses":['spark','pyspark','hadoop','python','java','cloud'],
        "Fees":[10000,10000,5000,15000,20000,30000],
        "Duration":['10 days','15 days','5 days','30 days','90 days','20 days'],
        "Discount":[10,14,8,15,20,5]
        })
row=['r1','r2','r3','r4','r5','r6']
df = pd.DataFrame(tech, index = row)


# to fisplay records which follows condition given in the query
df1 = df.query("Courses == 'spark'")
print(df1)
df1 = df.query("Courses != 'spark'")
print(df1)


#adding  new column to the dataframe
tech = ({
        "Courses":['spark','pyspark','hadoop','python','java','cloud'],
        "Fees":[10000,10000,5000,15000,20000,30000],
        "Discount":[10,14,8,15,20,5]
        })
df = pd.DataFrame(tech)
print(df)

tutor = ['a','b','c','d','e','f'] #new column contents
df1 = df.assign(Tutors = tutor)
print(df1)
"""or"""
df1 = df.assign(Tutors = ['a','b','c','d','e','f'])
print(df1)
"""or"""
df["Tutors"] = tutor
print(df)
#adding new column at specified position
df.insert(0,"Tutors",tutor)
print(df)

#adding new column by using previous columns
df2 = df.assign(disc_per = lambda x : x.Fees*x.Discount/100)
print(df2)
df3 = df2.assign(total_amt = lambda x : x.Fees-x.disc_per)
print(df3)


tech = ({
        "Courses":['spark','pyspark','hadoop','python','java','cloud'],
        "Fees":[10000,10000,5000,15000,20000,30000],
        "Discount":[10,14,8,15,20,5]
        })
df = pd.DataFrame(tech)
#to get number of records from dataframe
rows = len(df.index)
"""or"""
rows = len(df.axes[0])
"""or"""
rows = df.shape[0]
print(rows)

#to get number of columns from dataframe
cols = len(df.axes[1])
"""or"""
cols = df.shape[1]
print(cols)


#performing similar operation on all elements of column using function
import pandas as pd
data = {'a':[1,2,3],
        'b':[4,5,6],
        'c':[7,8,9]}

df = pd.DataFrame(data)
df

def add(x):
    return x+3

#change value of all columns
df1 = df.apply(add)
df1

#change values of particular column
df1 = ((df.a).apply(add))
df1

df1['a'] = df['a'].apply(add)
df1

#apply to multiple columns
df1[['a','b']] = df[['a','b']].apply(add)
df1

#same operations using lambda function
df1 = df.apply(lambda x : x+3)
df1

df1['a'] = df['a'].apply(lambda x : x+3)
df1

df1['a','b'] = df[['a','c']].apply(lambda x : x+3)
df1

#using transform method
df1 = df.transform(add)
df1

df1 = df['a'].transform(add)
df1

df1 = df[['a','b']].transform(add)
df1

#using map function
df1 = df['a'].map(lambda x : x+3)
df1

#using numpy methos
import numpy as np
df1 = df['a'].apply(np.square)
df1

df1 = np.square(df['a'])
df1

#group by function
tech = {
        "Courses":['spark','pyspark','hadoop','python','pandas','hadoop','spark','python','NA'],
        "Fees":[22000,25000,23000,24000,26000,25000,25000,22000,1500],
        "Duration":['30 days','15 days','5 days','30 days','90 days','20 days','5 days','15 days','10 days'],
        "Discount":[10,14,8,15,20,5,8,10,15]
        }

df = pd.DataFrame(tech)
df

df1 = df.groupby(['Courses']).sum()
df1

df1 = df.groupby(['Courses','Duration']).sum().reset_index()
df1


#get column name from dataframe
tech = {
        "Courses":['spark','pyspark','hadoop','python','pandas','hadoop','spark','python','NA'],
        "Fees":[22000,25000,23000,24000,26000,25000,25000,22000,1500],
        "Duration":['30 days','15 days','5 days','30 days','90 days','20 days','5 days','15 days','10 days'],
        "Discount":[10,14,8,15,20,5,8,10,15]
        }

df = pd.DataFrame(tech)
df

df.columns

column_headers = list(df.columns.values)
print("Column headers of::",column_headers)


#row shuffling
#used to improve the model accuracy during model building
import pandas as pd
tech = {
        "Courses":['spark','pyspark','hadoop','python','pandas','hadoop','spark','python','NA'],
        "Fees":[22000,25000,23000,24000,26000,25000,25000,22000,1500],
        "Duration":['30 days','15 days','5 days','30 days','90 days','20 days','5 days','15 days','10 days'],
        "Discount":[10,14,8,15,20,5,8,10,15]
        }

df = pd.DataFrame(tech)
df

#index get shuffeled
df1 = df.sample(frac=1)#frac=1 means 100% data shuffling frac=0.5 means 50% data shuffling
df1

#gives index to shuffeled data
df1 = df.sample(frac=1).reset_index()
df1

#drop the shuffeled index and not include it in dataframe
df1 = df.sample(frac=1).reset_index(drop=True)
df1


#joins
import pandas as pd

tech1 = {
        "Courses":['spark','pyspark','python','pandas'],
        "Fees":[22000,25000,23000,24000],
        "Duration":['30 days','15 days','25 days','30 days'],
        }
l1 = ['r1','r2','r3','r4']
df1 = pd.DataFrame(tech1,index=l1)
df1

tech2 = {
    "Courses": ['spark', 'java', 'python', 'go'],
    "Discount": [2200, 2500, 2300, 2400],
}
l2 = ['r1', 'r6', 'r3', 'r5']
df2 = pd.DataFrame(tech2, index=l2)
df2

#by default left join
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right")
df3
"""Courses_left   Fees Duration Courses_right  Discount
r1        spark  22000  30 days         spark    2200.0
r2      pyspark  25000  15 days           NaN       NaN
r3       python  23000  25 days        python    2300.0
r4       pandas  24000  30 days           NaN       NaN"""

#inner join
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right", how="inner")
df3
"""Courses_left   Fees Duration Courses_right  Discount
r1        spark  22000  30 days         spark      2200
r3       python  23000  25 days        python      2300"""

#left join
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right", how="left")
df3
"""Courses_left   Fees Duration Courses_right  Discount
r1        spark  22000  30 days         spark    2200.0
r2      pyspark  25000  15 days           NaN       NaN
r3       python  23000  25 days        python    2300.0
r4       pandas  24000  30 days           NaN       NaN"""

#right join
df3 = df1.join(df2, lsuffix="_left", rsuffix="_right", how="right")
df3
"""Courses_left     Fees Duration Courses_right  Discount
r1        spark  22000.0  30 days         spark      2200
r6          NaN      NaN      NaN          java      2500
r3       python  23000.0  25 days        python      2300
r5          NaN      NaN      NaN            go      2400"""

#joining using common column by declere it explicitly
#inner join
df3 = df1.set_index("Courses").join(df2.set_index("Courses"), how="inner")
df3
"""
Courses Fees Duration  Discount                     
spark    22000  30 days      2200
python   23000  25 days      2300"""

#left join
df3 = df1.set_index("Courses").join(df2.set_index("Courses"), how="left")
df3
""" 
Courses  Fees Duration  Discount                   
spark    22000  30 days    2200.0
pyspark  25000  15 days       NaN
python   23000  25 days    2300.0
pandas   24000  30 days       NaN"""

#right join
df3 = df1.set_index("Courses").join(df2.set_index("Courses"), how="right")
df3
"""
Courses    Fees    Duration  Discount                   
spark    22000.0  30 days      2200
java         NaN      NaN      2500
python   23000.0  25 days      2300
go           NaN      NaN      2400"""

#concating two dataframes
import pandas as pd
tech1 = {
        "Courses":['spark','pyspark','python','pandas'],
        "Fees":[22000,25000,23000,24000]
        }
df1 = pd.DataFrame(tech1)

tech2 = {
        "Courses":['hadoop','pyspark','java','pandas'],
        "Fees":[22000,25000,23000,24000]
        }
df2 = pd.DataFrame(tech2)

data = (df1,df2)
data
#concating dataframes without arranging index
df3 = pd.concat(data)
df3

#concating with reseting index
df3 = pd.concat(data).reset_index()
df3

#concating by droping the index
df3 = pd.concat(data).reset_index(drop=True)
df3


#concating multiple dataframes
import pandas as pd
tech1 = {
        "Courses":['spark','pyspark','python','pandas'],
        "Fees":[22000,25000,23000,24000]
        }
df1 = pd.DataFrame(tech1)

tech2 = {
        "Courses":['hadoop','pyspark','java','pandas'],
        "Fees":[22000,25000,23000,24000]
        }
df2 = pd.DataFrame(tech2)

tech3 = {
        "Duration":['30 days','15 days','25 days','30 days'],
        "Discount":[10,14,8,15]
        }
df3 = pd.DataFrame(tech3)

df = pd.concat([df1,df2,df3])
df