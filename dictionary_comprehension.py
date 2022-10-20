"""
Example #3
Challenge: Create a Dictionary
Easy
Problem Description
Create a program to create a dictionary using dictionary comprehension.

Create a list with the following data items 1, 2, 3, 4, and assign it to the numbers variable.
Create a new dictionary using comprehension where the keys are items of the list, and their corresponding values are equal to key+1.
Print the dictionary.
Example
Expected Output

{1: 2, 2: 3, 3: 4, 4: 5}
"""

# The simplest way to accomplish this task is as follows. 
# Create a dictionary and a count variable, then run a nested loop for the key list to assign key-value pairs from the list and count to the dictionary. For each iteration, add one to the count.
numbers = [1, 2, 3, 4]
dict={}
count = 2
# create the dictionary using brute force.
for key in numbers:
    dict[key]=(count)
    count=count+1
# print the dictionary
print(dict)


## short and compact
# create the dictionary using comprehension
dict = {v:k +2 for k,v in enumerate(numbers)}
print(dict)
