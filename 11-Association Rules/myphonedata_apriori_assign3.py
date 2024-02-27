# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 23:36:19 2023

@author: Lenovo
"""
#---------------------------myphonedata assign
phone=[]
f=open(r"D:\DATA SCIENCE\Machine_learning\ML ALGORITHM\aproiry\myphonedata.csv")
phone=f.read()
phone

phone=phone.split('\n')
phone

phone_list=[i.split(',') for i in phone]
phone_list

all_phone=[j for i in phone_list for j in i]
all_phone
#here all phones data are perfectly split
#now count the values

#--count the values

from collections import Counter
freq=Counter(all_phone)
freq

#now convert it into proper key values pair
item_freq=sorted(freq.items(),key=lambda x:x[1])
item_freq

#now seperate the item and it's freq
#in reverse order
item=list(reversed([i[0] for i in item_freq]))
item

freqencies=list(reversed([i[1] for i in item_freq]))
freqencies
#now plot the freq

#------------plot
import matplotlib.pyplot as plt
plt.bar(x=list(range(1,5)), height=freqencies[0:4])
plt.xlabel('items')
plt.ylabel('count/freq')
plt.show()

#now create a dataframe
import pandas as pd
from mlxtend.frequent_patterns import association_rules,apriori

df=pd.DataFrame(pd.Series(phone_list))
df
#remove last empty list
df=df.iloc[0:11,:]

#rename the col
df=df.rename(columns={0:'phones'})
df

#now join phones using *
x=df['phones'].str.join(sep='*')
x

#now apply one hot encoder
x=x.str.get_dummies(sep='*')
x

#now apply apriori algo.
freq_item=apriori(x,min_support=0.0075,max_len=4,use_colnames=True)
freq_item

#sort the support
freq_item.sort_values('support',ascending=False,inplace=True)
freq_item

#now apply association rule
rule=association_rules(freq_item,metric='lift',min_threshold=1)
rule.head()
