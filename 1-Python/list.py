#Lists
#Lists are mutable ordered containers of other objects.
#Creating Lists
lst1 = ['John', 'Paul', 'George', 'Ringo']
#As with Tuples we can have nested lists and lists containing different types of
#elements.
lst1 = [1, 43.5, True]
lst2 = ['apple', 'orange', 31]
root_list = ['John', lst1, lst2, 'Denise']
print(root_list)
##########################
#Accessing Elements from a List
lst1 = ['John', 'Paul', 'George', 'Ringo']
print(lst1[-1])
lst1[-1]
lst1[-2]
##################
lst1 = ['John', 'Paul', 'George', 'Ringo']
print('lst1[1]:', lst1[1])
print('lst1[-1]:', lst1[-1])
print('lst1[1:3]:', lst1[1:3])
print('lst[:3]:', lst1[:3])
print('lst[1:]:', lst1[1:])
##########################
#Adding to a List
lst1 = ['John', 'Paul', 'George', 'Ringo']
lst1.append('Pete')
print(lst1)
#You can also add all the items in a list 
#to another list. There are several options
lst1 = ['John', 'Paul', 'George', 'Ringo', 'Pete']
print(lst1)
lst1.extend(['Albert', 'Bob'])
#here, we can use the extend()
lst1
#Inserting into a List
a_list = ['Adele', 'Madonna', 'Cher']
print(a_list)
a_list.insert(1, 'Paloma')
print(a_list)
#List Concatenation
lst1 = [3, 2, 1]
lst2 = [6, 5, 4]
lst3 = lst1 + lst2
print(lst3)
#Removing from a List
another_lst = ['Gary', 'Mark', 'Robbie', 'Jason', 'Howard']
print(another_lst)
another_lst.remove('Robbie')
print(another_lst)
#The pop() Method
#It removes an element from the List; 
#however, it differs from the remove()
#method in two ways:
# It takes an index which is the index of the item to remove from the list rather
#than the object itself.
lst6 = ['Once', 'Upon', 'a', 'Time']
print(lst6)
print(lst6.pop(2))
print(lst6)
#Inserting into a List
a_list = ['Adele', 'Madonna', 'Cher']
print(a_list)
a_list.insert(1, 'Paloma')
print(a_list)
#######################
#List Concatenation
list1 = [3, 2, 1]
list2 = [6, 5, 4]
list3 = list1 + list2
print(list3)
#####################################