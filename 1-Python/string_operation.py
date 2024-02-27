#multiline strings
x="""this is python.
it is very powerfull"""
print(x)

#concatanation operation
str1="Hello"
str2=2
str3=str1+str2

#slicing operation
x='''this is python.
it is very powerful'''
print(x[2:])
print(x[-5:-2])

#escape sequence characters
x="this is the fun fair and it has got big \"round rigo\""
print(x)

#modify upper case
x='''this is python.
it is very powerful'''
print(x.upper())

#modify lower case
x='''This is python.
it is very powerful'''
print(x.lower())

#to check palindrome or not
string=input(("Enter a letter:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome")

#replce operation
x="hello world"
print(x.replace("hello", "hola"))

#string reverse
string1=x[::-1]
print(string1)

#serching in string
x="this is python and its very awesome"
print(x.find("very"))

#split operation
x="hello,world"
print(x.split(","))

#string fromating
quantity=3
item_no=54
price=67
print(f"i want {quantity} pieces and item number is {item_no},its price is {price}")
my_order="i want {2} pieces and item number is {1}, its price is{0}"
print(my_order.format(quantity,item_no,price))