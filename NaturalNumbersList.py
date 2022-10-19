"""
Challenge: Natural Numbers List
Easy
Problem Description: Create a program to create a list of first n natural numbers using list comprehension.

Take an integer input from the user and assign it to n.
Use list comprehension to create a list with items from 1 to n.
Print the list.
Assumption: We will assume that the user will always enter a positive integer.

Example
Test Input
4
Expected Output
[1, 2, 3, 4]
"""

## long more readable
# get integer input for variable n
n = int(input())
# create the list using list comprehension
numbers = []
for i in range(1, 1+n):
    numbers.append(i)
# print the list
print(numbers)


## short and compact
print(*range(1, 1+ n))
