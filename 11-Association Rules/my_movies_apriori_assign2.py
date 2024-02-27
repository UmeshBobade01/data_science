# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 22:37:49 2023

@author: Lenovo
"""
#---------------------------------------my_movies Assignment--------------------

#------split the all transactions
movies=[]
#first read the csv file
f=open(r"D:\DATA SCIENCE\Machine_learning\ML ALGORITHM\aproiry\my_movies.csv")
#store it into empty list
movies=f.read()
movies

#here we create new list which split elment from \n
movies=movies.split('\n')
movies
len(movies)
#Out[71]: 12

movie_list=[]
for i in movies:
    movie_list.append(i.split(','))
movie_list
#here we split value with comma

all_movies=[j for i in movie_list for j in i]
all_movies
#here we get all movies
len(all_movies)
#Out[100]: 111

#-----------------count the freq of movies
from collections import Counter

movie_freq=Counter(all_movies)
movie_freq
#'Harry Potter2': 1,
#'LOTR': 1,
#'0': 70,
#'': 1})

#now we will get output in the form of dict
#now we need to divide frq and items 

#here we have total item freq
item_freq=sorted(movie_freq.items(),key=lambda x:x[1])
item_freq

#now we print it into reverse form
item=list(reversed([i[0] for i in item_freq]))
item

#here freq
freq=list(reversed([i[1] for i in item_freq]))
freq

#-------------------------now plot the frequencies

import matplotlib.pyplot as plt
plt.bar(x=list(range(0,4)), height=freq[0:4])
plt.xlabel('items')
plt.ylabel('Freq/count')
plt.show()

#-------------convert into dataframe
import pandas as pd
from mlxtend.frequent_patterns import association_rules,apriori
df=pd.DataFrame(pd.Series(movie_list))
df
# the last row of the dataframe is empty so we will remove it
df=df.iloc[0:11,:]
df

#rename the column name
df=df.rename(columns={0:'transactions'})

x=df['transactions'].str.join(sep='*')
x

#now we used one hot encoding
x=x.str.get_dummies(sep='*')
x
#this kind of data we will apply for approri algo

#----------apply apriori
frequent_item=apriori(x,min_support=0.0075,max_len=4,use_colnames=True)
frequent_item.columns
# You will get support value for 1,2,3,4 max items

frequent_item.sort_values('support')

#------------apply association rule

rule=association_rules(frequent_item,metric='lift',min_threshold=1)
rule.head()
