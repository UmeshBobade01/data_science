#Creating a Set
basket = {'apple', 'orange', 'apple', 'pear','orange', 'banana'}
print(basket)
#When run this code will show that apple is only added once to the set:
#Accessing Elements in a Set
for item in basket:
   print(item)
#################
#Adding Items to set
basket = {'apple', 'orange', 'banana'}
basket.add('apricot')
print(basket)
#If you want to add more than one item to a Set you can use the update() method:
basket = {'apple', 'orange', 'banana'}
basket.update(['apricot', 'mango', 'grapefruit'])
print(basket)
######################
#Obtaining the Length of a Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange','banana'}
print(len(basket))
#Obtaining the Max and Min Values in a Set
basket2={23,45,67,12,456}
print(max(basket2))
print(min(basket2))
#Removing an Item
basket = {'apple', 'orange', 'apple', 'pear', 'orange','banana'}
print(basket)
basket.remove('apple')
basket.discard('apricot')
print(basket)
#Set Operations
s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}
print('Union:', s1 | s2)
print('Intersection:', s1 & s2)
print('Difference:', s1 - s2)
############################################