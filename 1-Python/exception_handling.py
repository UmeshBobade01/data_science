#exception handling
#using try except block
a=5
b=6
c=a+b
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't division by zero!")
print(c)

'''need of unicode- Today's programs need to be able to handle a wide variety
of characters. Applications are often internationalized to display messages
and output in a variety of user-selectable languages; the same program might
need to output an error message in English, French, Japanese, Hebrew, or
Russian. Web content can be written in any of these languages and can also 
include a variety of emoji symbols. Python's string type uses the unicode 
standard for representing characters, which lets Python programs work with all
these different possible characters.'''

#1- utf[unicode transformation program]
filename = 'alice.txt'
try:
    with open(filename, encoding = 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"sorry,the file {filename} does not exist.")       
