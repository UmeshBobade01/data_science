"""
Advanced python 
1. list compression(LC)
"""

#appending elements in list by regular method
l1 = []
for i in range(0,20):
    l1.append(i)
print(l1)

#appending elements by LC
l1 = [i for i in range(0,20)]
print(l1)

#modification in list using LC
names = ['umesh','aryan','yash','tejax']
l1 = [i.capitalize() for i in names]
print(l1)

#LC with if statement for printing even numbers
def is_even(i):
    return i%2==0
l1 = [i for i in range(10) if is_even(i)]
print(l1)
#or 
l1 = [i for i in range(10) if i%2==0]
print(l1)

#for 2 for loops
l1 = [f"{x}{y}" for x in range(3) for y in range(3)]
print(l1)

#set compression (not used)
s1 = {x for x in range(3)}
print(s1)

#dict compression
d1 = {x:x*x for x in range(3)}
print(d1)

"""2. generator"""
#when we apply compression to tuple it will create an object which can be accessed by for loop
gen = (i for i in range(3))
print(gen)
for num in gen:
    print(num)

#to access elements in generator step by step
gen = (i for i in range(3))
print(gen)
next(gen)
next(gen)
next(gen)

#function with multiple values in return
#suppose a function is returning multiple values and we have to iterate through the results
#then we use yeild keyword

def range_even(end):
    for i in range(0,end,2):
        yield i

#printing result by for loop
for i in range_even(6):
    print(i)

#printing result by next
gen = range_even(6)
print(next(gen))
print(next(gen))
print(next(gen))


"""chaning generators"""
# function to find length of each password in given list of passwords
def lengths(password):
    for i in password:
        yield len(i)

#function to convert the password into "********" format
def hide(password):
    for i in password:
        yield i*'*'

passwords = ['uiqgsdccd','djhdwuy','n3i27633']
#for loop below will call the length generator inside hide generator
for i in hide(lengths(passwords)):
    print(i)


"""3. Enumarate"""
#printing list with index by range
l1 = ['umesh','aryan','yash','tejas']
for i in range(len(l1)):
    print(f'{i+1} {l1[i]}')
print("\n")
#using enumerate 
l1 = ['umesh','aryan','yash','tejas']
for i,item in enumerate(l1,start=1):
    print(f'{i} {item}')
