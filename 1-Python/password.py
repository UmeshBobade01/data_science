import string
import random
adjectives=["sleepy","slow","smelly","wet","fat","healthy","red","orange","yellow"]
nouns=["apple","dianosoar","ball","toaster","goat","dragon","homer"]
pass_list = []
for i in range(5):
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password=adjective+noun+str(number)+special_char
    pass_list.append(password)

print(pass_list)

# function to find length of each password in given list of passwords
def lengths(password):
    for i in password:
        yield len(i)

#function to convert the password into "********" format
def hide(password):
    for i in password:
        yield i*'*'
        
for i in hide(lengths(pass_list)):
    print(i)