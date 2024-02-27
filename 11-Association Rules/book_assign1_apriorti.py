# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:25:47 2023

@author: Lenovo
"""
from mlxtend.frequent_patterns import apriori,association_rules

#-----------------------read and split the all data/transaction

book=[]
f= open(r"D:\DATA SCIENCE\Machine_learning\ML ALGORITHM\aproiry\book.csv") 
book=f.read()
book
# it will split data in the comma separater form

book=book.split('\n')
book
#Earlier it was in the format of srin g it will convert it into the form of
# list
book_list=[]
for i in book:
    book_list.append(i.split(','))
# it will separate items from each list so further we can separe it for support caculation
book_list
len(book_list)
#Out[112]: 2002

all_book=[j for i in book_list for j in i]
all_book
# we will get all the transactions/item 
# we will get 22012 items in various transaction
len(all_book)

#--------------------count the frequency of each item 
#split frequency and item from dict

from collections import Counter
item_frequencies=Counter(all_book)
item_frequencies
#'Florence': 1,
#'0': 17155,
#'1': 4845,
#'': 1})

# item_frequencies will be contain key and dictionary 
# we want to sort it into count frequencies 
# means it will show he count of item purchased
# let us sort the frequencies in ascending order

item_frequencies=sorted(item_frequencies.items(),key=lambda x:x[1])
item_frequencies

#when we execute this,items frequencies will be in sorted form 
# item name with count

items=list(reversed([i[0] for i in item_frequencies]))
items
# This is the list comprehenssion it will give the items from dictionaries 

frequencies=list(reversed([i[1] for i in item_frequencies]))
frequencies
#This will  give he frequencies of each items

#-----------------------------we will plot the frequencies

import matplotlib.pyplot as plt
plt.bar(height=frequencies[0:3],x=list(range(0,3)))
#here we just plot graph of 3 freq
plt.xlabel('items')
plt.ylabel('count')
plt.show()

#----------------Now we will convert it into dataframe
import pandas as pd
book_series=pd.DataFrame(pd.Series(book_list))
book_series
# Now we will get the the  dataframe of size 
# the last row of the dataframe is empty so we will remove it

book_series=book_series.iloc[:2001,:]
book_series
book_series.head(5)
# So it will remove the last row

# groceries_series having column name 0 so rename as Transaction
book_series.columns=['Transactions']
book_series

# So there is various elements which is separeted by , = we will seperate using
# * we can join it
x=book_series['Transactions'].str.join(sep='*')
x

# Now we will apply one-hot encoding to convert it into numeric form
x=x.str.get_dummies(sep='*')
x

# This is the data which we are going to apply for the Apriori algorithm
frequency_items=apriori(x,min_support=0.0075,max_len=4,use_colnames=True)
frequency_items
# You will get support value for 1,2,3,4 max items

# let us sort the support values
frequency_items.sort_values('support',ascending=False,inplace=True)
frequency_items

# This will sort the support the value in descending order 
# in EDA also there was same trend there it was a count
# and here it was support value

rules=association_rules(frequency_items,metric='lift',min_threshold=1)
# This generate association rule of size 1198x9 columns
# comprises of antescends,consequences
rules.head()
rules.columns
rules.sort_values('lift',ascending=False).head()