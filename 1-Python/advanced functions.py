"""
Advanced python
"""

"""zip function"""
#using zip
name = ['uk','yc','ak','td']
info = [736,937,873,837]
for i,j in zip(name,info):
    print(i,j)
"""
o/p
uk 736
yc 937
ak 873
td 837
"""

name = ['uk','yc','ak','td']
info = [736,937]
for i,j in zip(name,info):
    print(i,j)
"""
o/p
uk 736
yc 937
"""

#using zip_longest
from itertools import zip_longest
name = ['uk','yc','ak','td']
info = [736,937]
for i,j in zip_longest(name,info):
    print(i,j)
"""
o/p
uk 736
yc 937
ak None
td None
"""

#use of fill value where value is null or None
from itertools import zip_longest
name = ['uk','yc','ak','td']
info = [736,937]
for i,j in zip_longest(name,info,fillvalue=0):
    print(i,j)
"""
o/p
uk 736
yc 937
ak 0
td 0
"""


""""All function"""
l1 = [2,4,5,0,-1,1]
if all(l1):
    print("True")
else:
    print("False")
#this code will return false if any value in list '0' or 'None'


""""Any function"""
l1 = [0,0,0,0,0,1]
if any(l1):
    print("True")
else:
    print("False")
#this function will return true if any value rather than '0' or 'None'


"""Count function"""
from itertools import count
counter = count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))


"""Cycle function"""
import  itertools as it
t1 = ("Eat","Sleep","Code")
for i in it.cycle(t1):
    print(i)


"""repeat"""
from itertools import repeat
for msg in repeat("hiii",times=10):
    print(msg)
# repeat the msg 10 times as defined


"""Combination"""
from itertools import combinations
l1 = [1,2,3]
for i in combinations(l1,2):
    print(i)
#this function is used to get combinations from list where 
#combinations(list,no.of combinations)


"""permutations"""
from itertools import permutations
l1 = [1,2,3]
for i in permutations(l1,2):
    print(i)
# this function is used to find permutations in the list
# for specific condition


"""Product"""
from itertools import product
l1 = ["rohit","pandya","boom"]
l2 = ["virat","ashwin","siraj"]
for i in product(l1,l2):
    print(i)


"""Filter"""
age = [98,86,83,27,10,12]
adults = filter(lambda age:age>=18,age)
print([i for i in adults])


"""assignment operation"""
l1 = [1,2,3,4,5,6]
l2 = l1
print(l2)
l2[0] = 10
print(l1)
print(l2)
#if we change values in in list l1 then it will also change the contents of list l2
#as we declared l2=l1


#shalow copy
import copy
l1 = [1,2,3,4,5,6]
l2 = copy.copy(l1)#this will copy l1 into l2 
print(l2)
l2[2]=10
print("list 2::",l2)
print("list 1::",l1)

#shalow copy
import copy
l1 = [1,2,[1,2],4,5,6]
l2 = copy.copy(l1)#this will copy l1 into l2 
print(l2)
l2[2][0]=10
print("list 2::",l2)
print("list 1::",l1)

#deep copy
import copy
l1 = [1,2,[1,2],4,5,6]
l2 = copy.deepcopy(l1)#this will copy l1 into l2 
print(l2)
l2[2][0]=10
print("list 2::",l2)
print("list 1::",l1)

"""Chain function"""
#for list
from itertools import chain
def chain_fun(l1,l2,l3):
    return chain(l1,l2,l3)

l = chain_fun([1,2,3],['a','b','c','d'],[4,5,6])
print("Type of new iterator::",type(l))
print("elements of new iterator")
for i in l:
    print(i)

#for tuples
from itertools import chain
def chain_fun(l1,l2,l3):
    return chain(l1,l2,l3)

l = chain_fun((1,2,3),('a','b','c','d'),(4,5,6))
print("Type of new iterator::",type(l))
print("elements of new iterator")
for i in l:
    print(i)

#python program that generates the running product of elements in an iterable
#for list
from itertools import accumulate
import operator
def run_pro(l1):
    return accumulate(l1,operator.mul)
l = run_pro([1,2,3,4,5,6])
print(type(l))
for i in l:
    print(i)

#for tuple
from itertools import accumulate
import operator
def run_pro(l1):
    return accumulate(l1,operator.mul)
l = run_pro((1,2,3,4,5,6))
print(type(l))
for i in l:
    print(i)

#write python program to construct an infinite iterator that returns evenly 
#spaced values starting with a specified number
import itertools as it
start = 10
step = 1
print("the starting is",start,"end step is",step)
my_counter = it.count(start,step)
for i in my_counter:
    print(i)


#write python program to construct an infinite cycle from ierator
#for list
import itertools as it
def cycle_data(i):
    return it.cycle(i)

l = cycle_data(['a','b','c'])
for i in l:
    print(i)

#for string
import itertools as it
def cycle_data(i):
    return it.cycle(i)
l = cycle_data("hii")
for i in l:
    print(i)


#write pyhton program to make an iterator that drops elements as soon as
#the positive value occurs

import itertools as it
def drop_pos(l1):
    return it.dropwhile(lambda x : x<0,l1)

l1 = [-1,-2,-3,1,2,-5,-7]
l = drop_pos(l1)
for i in l:
    print(i)
