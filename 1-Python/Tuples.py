'''
#Tuples A Tuple represents a collection of objects that are ordered and immutable
(cannot be modified).
#Lists Lists hold a collection of objects that are ordered and mutable (changeable),
they are indexed and allow duplicate members.
#Sets Sets are a collection that is unordered and unindexed. They are mutable
(changeable) but do not allow duplicate values to be held.
#Dictionary A dictionary is an unordered collection that is indexed by a key
which references a value. The value is returned when the key is provided.
'''
#Creating Tuples
tup1 = (1, 3, 5, 7)
#Accessing Elements of a Tuple
print(f'tup1[0]:\t{tup1[0]}')
print('tup1[1]:\t', tup1[1])
print('tup1[2]:\t', tup1[2])
print('tup1[3]:\t', tup1[3])

#Tuples Can Hold Different Types
tup2 = (1, 'John',  True, -23.45)
print(tup2)
#Iterating Over Tuples
tup3 = ('apple', 'orange', 'plum', 'apple')
for x in tup3:
   print(x)
#Tuple Related Functions
#You can also find out the length of a Tuple
len(tup3)
#You can count how many times a specified value 
#appears in a Tuple 
tup4 = ('apple', 'orange', 'plum', 'apple','apple')
#Tuples allow duplicates;
tup4.count('apple')
#You can also find out the (first) index of a value in a Tuple:
print(tup4.index('apple'))
print(tup4.index('plum'))
#Checking if an Element Exists
if 'orange' in tup3:
   print('orange is in the Tuple')
#Nested Tuples
#Tuples can be nested within Tuples; 
#that is a Tuple can contain, as one of its
#elements, another Tuple.
tuple1 = (1, 3, 5, 7)
tuple2 = ('John', 'Denise', 'Phoebe', 'Adam')
tuple3 = (42, tuple1, tuple2, 5.5)
print(tuple3)
#It is not possible to add or remove 
#elements from a Tuple; they are immutable.
#############################################