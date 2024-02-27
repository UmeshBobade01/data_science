#here we first read the csv file
retail=[]
#and store it into list
with open(r"D:\DATA SCIENCE\Machine_learning\ML ALGORITHM\aproiry\transactions_retail1.csv") as f:retail=f.read()
retail

retail=retail.split('\n')
#here we split the data from \n

retail_list=[i.split(',') for i in retail]
retail_list
#here we split the transactions from ,

all_retail=[j for i in retail_list for j in i]
all_retail
len(all_retail)
#here our all transactions_retail data is properly distribute/splited
#now lets count the values

#------------count 

from collections import Counter
item_freq=Counter(all_retail)
item_freq
# item_frequencies will be contain key and dictionary 
# we want to sort it into count frequencies 
# means it will show he count of item purchased
# let us sort the frequencies in ascending order

item_freq=sorted(item_freq.items(),key=lambda x:x[1])
item_freq

#now seperate the item and key in reverse format

item=list(reversed([i[0] for i in item_freq]))
item

freq=list(reversed([i[1] for i in item_freq]))
freq
#here we seperate the frequencies and items

#-----------now plot the graph

import matplotlib.pyplot as plt
plt.bar(height=freq[0:25],x=list(range(0,25)))
plt.xlabel('items')
plt.ylabel('count')
plt.show()

#now convert it into Data Frame

import pandas as pd
from mlxtend.frequent_patterns import association_rules,apriori
df=pd.DataFrame(pd.Series(retail_list))

#here we remove the last empty list
df=df.iloc[0:50000,:]
df

#now rename the column
df=df.rename(columns={0:'retail'})
df

#now join the values using *
x=df['retail'].str.join(sep='*')
x

#now apply one hot encoder on it
y=x.str.get_dummies(sep='*')


#now apply apriori algorithm
retail_freq=apriori(y,min_support=0.0075,max_len=4,use_colnames=True)
retail_freq

retail_freq.sort_values('support')

rules=association_rules(retail_freq,metric='lift',min_threshold=1)
rules.head()
