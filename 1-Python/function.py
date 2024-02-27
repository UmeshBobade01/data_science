def build_person(first_name, last_name):
    person = {"first": first_name, "last":last_name};
    return person
musician = build_person("ram", "sarkar")
print(musician)

#next
def great_user(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
username = ["Yash","Aaryan","Vikas"]
great_user(username)

#next
def make_pizza(*toppings):
    print(toppings)
make_pizza("pepperoni")
make_pizza("mushrooms","green chillis","extra cheese")

#next
def make_pizza(*toppings):
    print("\nmaking a pizza with the following toppings:")
    for toppin in toppings:
        print(f"{toppin}")
make_pizza("pepperoni")
make_pizza("mushrooms","green chillis","extra cheese")
        
#next
def make_pizza(size,*toppings):
    print(f"\nmaking a {size}-inch pizza with the following toppings:")
    for toppin in toppings:
        print(f"-{toppings}")
make_pizza(16,"pepperoni")
make_pizza("12", "green","vegitable","red chilli")    
import pizza

pizza.make_pizza("12", "green","vegitable","red chilli")  

#importing specific function

from pizza import make_pizza as p
p(10, "pepproni") 

#import more than 1 function
from pizza import *
make_pizza(10, "pepperoni")
make_pizza("12", "green","vegitable","red chilli")  

#lamdba function
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
add=lambda a,b,c:a+b+c
add(4,5,6) 

#lamda fumction multi
def multi(a,b,c):
    multi=a*b*c
    return multi
print(multi(4,5,6))
multi=lambda a,b,c:a*b*c
multi(4,5,6) 
#next
val=lambda *args:sum(args)
val(1,2,3,4,5,6)
val(1,2,3,4,5,7,8,9)

###
def person(name,**data):
    print(name)
    print(data)
person(name="navin", age=28,place="mumbai",mob_no=778899)

###

def person(name,**date):
    print(name)
    for i,j in date.items():
        print(i,j)
person("navin", age=28,place="mumbai",mob_no=778899)

###
val=lambda **data:sum(data.values())
val(a=2,b=6,c=6,d=10)

max=lambda a,b:x if(a>b) else b
print(max(1,2))















































  