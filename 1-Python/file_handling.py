with open('pi_digits.txt')as file_object:
    #the open() function needs
    #one  argument: the name of the file you want to open.
    contents = file_object.read()
print(contents)

with open('pi_digits.txt')as file_object:
    #the open() function needs
    #one  argument: the name of the file you want to open.
    contents = file_object.read()
print(contents.rstrip())
#tstrip()method removes,or strips,any whitespaces

file_path = 'c:/10-python/pi_digits.txt'
with open('pi_digits.txt')as file_object:
    contents = file_object.read()
print(contents.rstrip())

#reading line by line
filename='pi_digits.txt'
#we assign the name of the file we're reading from to the variable
with open(filename) as file_object:
    #we agian use the with syntax to let python open and close the flle properly
    for line in file_object:
        print(line)
        
#to remove white space use=rstrip       
filename='pi_digits.txt'
#we assign the name of the file we're reading from to the variable
with open(filename) as file_object:
    #we agian use the with syntax to let python open and close the flle properly
    for line in file_object:
        print(line.rstrip())
        
     
filename = 'pi_digits.txt'
with open(filename) as file_object:
     lines = file_object.readlines()
     pi_string = ''#not necessary
     for line in lines:
         pi_string = line.rstrip()
         print(pi_string)
         print((len(pi_string)))       


filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("i love programming.")

        
#write multiple lines
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("i love programming.\n")
    file_object.write("i love games.\n")
    

filename = 'programming.txt'
with open(filename, 'a') as file_object:
    #we use 'a' argument to open the file for appending rather then writing 
    #over  the existing file.
    file_object.write("i love programming more than watching movies.\n")
    file_object.write("i love creating apps that can run in a browser.\n")     


#json file operations
import json
numbers = [2,3,5,6,11,13]
filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers, f)


#
import json
username = input("what is your name?")
filename = "username,json"
with open(filename,"w") as f:
    json.dump(username,f)
print(f"we'll you when you came back,{username}!")


#
import json
filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
print(f'welcome back,{username}!')