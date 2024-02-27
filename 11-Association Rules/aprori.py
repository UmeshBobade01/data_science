"""Apriori Algorithm"""

#pip install mlxtend
from mlxtend.frequent_patterns import apriori, association_rules

groceries=[]
with open("C:/1-Python/2-dataset/groceries.csv.xls") as f:groceries=f.read()
groceries=groceries.split("\n")
groceries_list=[]
for i in groceries:
    groceries_list.append(i.split(","))
#split function will seperate each item from each list,whenever it will
#in order in generate association rules, u can directly use gloceries_list
#now let us seperate out each item from the glorceries list
all_groceries_list=[i for item in groceries_list for i in item]
#u will get all the item occured in all transaction
#we will get 43368 item in various transaction
#now let us count the frequently of each item
#we will import collections package which has counter function which will
from collections import Counter
item_frequencies=Counter(all_groceries_list)
#item_frequencies is basically dictionary having x[0] as key and x[1]=value
#we want to access values and sort based on the count that occured in it.
#it will show the count of each purchsed i every transaction.
#now let us sort these frquencies in ascending order
item_frequencies=sorted(item_frequencies.item(),key=lambda x:x[1])
#when we excute this,item frequencies will be in sorted form,in the form
#in the form of tuple
#item name with count
#let us seoerate out item and their count
item=list(reversed([i[0] for i in item_frequencies]))
#this is list comprehension for each item in item frequencies access the key
#here you will get item list
frequencies=list(reversed([i[1] for i in item_frequencies]))
#here you will get count of purchase of each item
#now let us plot bar graph of item frequencies
import matplotlib.pyplot as plt
#here we are taking frequencies from zero to 11,you can try 0-15 or any other
plt.bar(height=frequencies[0:11],x=list(range(0,11)))
plt.xticks(list(range(0,11)),item[0:11])

#plt.xticks, you can specify a rotation for the tick
#labels in degree or with keyword
plt.xlabel("items")
plt.ylabel("count")
plt.show()
import pandas as pd
groceries_series=pd.DataFrame(pd.Series(groceries_list))
# now we will get dataframe of size column comprises of multiple
# we had extra row created check groceries series last row is empty
groceries_series=groceries_series.iloc[:9835,:]
# we have taken rows from 0 to 9834 and column 0 to all
# groceries series has column having name 0,let us rename as transactions
groceries_series.columns=['Transactions']
# Now we will have to apply 1-hot encodfing before that in
# one column there are various items seperated by ,
# let us seperate it with "
x=groceries_series['Transactions'].str.join(sep='*')
x=x.str.get_dummies(sep='*')
# you will get one hot encoded dataframe of size
# this is our input data to apply to apriori algorithms it will generate
# is you can give any number but must be
frequent_itemsets=apriori(x,min_support=0.0075,max_len=4,use_colnames=True)
# support values will be sorted in descending order
# Even EDA was also have the same trand in eda there was count
# and here it is support value

# we will generate association rules this association
# rule will calcul;ate all the matrix
# of each and every combination
rules=association_rules(frequnet_itemsets,metric='lift',min_threshold=1)
# This generate association rules of size
# comprises of antescenda 4
rules.head(29)
rules.sort_values('lift',ascending=False).head(10)
































