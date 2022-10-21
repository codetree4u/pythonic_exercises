"""
Example #4
Challenge: Cube of a Number Using Lambda
Easy
Problem Description
Create a program to find the cube of a number using a lambda function.

Create the lambda function and assign it to a variable named num_cube.
Take one integer input and assign it to number.
Call the lambda function with number as argument and print the result.
Example
Test Input

2
Expected Output

8
"""

# create the function
num_cube = lambda x: x * x * x

# take integer input
number = int(input())

# call the function and print the result
print(num_cube(number))
