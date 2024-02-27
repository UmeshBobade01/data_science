#Dictionaries
#A Dictionary is a set of associations
# between a key and a value that is unordered,
#changeable (mutable) and indexed.
capitals = {
'Maharashtra': 'Mumbai',
'Gujrat': 'Ahmadbad',
'UP': 'Lakhnow',
'Karnataka': 'Banglore',
'Andhrapradesh': 'Hydrabad'
}
print(capitals)
#Accessing Items via Keys
print('capitals[Maharashtra]:', capitals['Maharashtra'])
#Adding a New Entry
capitals['West_Bengal']='Kolkatta'
capitals
#Changing a Keys Value
capitals['Gujrat'] = 'Gandhinagar'
print(capitals)
#Removing an Entry
capitals.pop('Karnataka')
print(capitals)
del capitals['UP']
print(capitals)
#Iterating over Keys
capitals = {
'Maharashtra': 'Mumbai',
'Gujrat': 'Ahmadbad',
'UP': 'Lakhnow',
'Karnataka': 'Banglore',
'Andhrapradesh': 'Hydrabad'
}
for states in capitals:
   print(states, end=', ')
   
for states in capitals:
     print(states, end=', ') 
     print(capitals[states])
#Values, Keys and Items
print(capitals.values())
print(capitals.keys())
print(capitals.items())
########################
#Checking Key Membership
print('Karnataka' in capitals)
print('Bihar' not in capitals)
#Obtaining the Length of a Dictionary
print(len(capitals))
#Dictionaries can have values in tuple
seasons = {'Summer': ('Feb','Mar', 'Apr', 'May'),
'Rainy': ('June', 'July', 'August','Sept'),
'Winter': ( 'Oct','Nov','December', 'January')}
print(seasons['Rainy'])
print(seasons['Rainy'][1])
#Dictionary Methods
#get() is a useful method to access the 
#values of a key in a dictionary.
print(capitals.get('UP'))
#Duplicates Not Allowed
#Dictionaries cannot have two items with the same
# key:
dict2 =	{
  "brand": "Maruti",
  "model": "Breeza",
  "year": 2021,
  "year": 2020
}
print(dict2)
#############################
#Loop Through a Dictionary,it will show only keys
for x in dict2:
  print(x) 
#Print all values in the dictionary, one by one:
for x in dict2:
  print(dict2[x]) 
#You can also use the values() method to return values of a dictionary:
for x in dict2.values():
  print(x) 
#you can use the keys() method to return the keys of a dictionary:
for x in dict2.keys():
  print(x) 
#Loop through both keys and values, by using the items() method:
for x, y in dict2.items():
  print(x, y) 
#Copy a Dictionary
#Make a copy of a dictionary with the copy() method:

mydict = dict2.copy()
print(mydict)
