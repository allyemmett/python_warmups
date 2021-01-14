# Write a program that takes in a fruit list as
# txt and creates a dict that the:
# Key is the first letter &
# The value is a list of all that begin with that
# letter

import pprint

with open("fruit.txt", "r") as f:# known as "context manager" & benefit of using is do not have to close reading file (for reading fruit.txt). Closes file automatically
    fruit_data = f.read().split('\n') # '\n' will make sure "starfruit" stays as one word
print(fruit_data)

fruit_dict = {} # empty dictionary
for fruit in fruit_data:
    if fruit_dict.get(fruit[0]): # fruit[0] grabs first letter
        fruit_dict[fruit[0]].append(fruit)
    else: fruit_dict[fruit[0]] = [fruit]

pprint.pprint(fruit_dict) #pprint can be imported to format dictionaries

