"""
Challenge: Division With Exception Handling
Medium
Problem Description
Create a program to divide numerator by denominator. However, if the denominator is 0, print Denominator cannot be 0. Try again..

Take two integer inputs and store them in numerator and denominator respectively.
Divide numerator by denominator and print the result.
However, if denominator is 0, print Denominator cannot be 0. Try again.
Note: Use exception handling to solve this problem.

Example
Test Input

4
0
Expected Output

Denominator cannot be 0. Try again.	
"""
# create a try block
try:
    # take input for numerator
    numerator = int(input())
    # take input for denominator
    denominator = int(input())

    # Divide numerator by denominator and print the result
    print(numerator / denominator)

# create the except block
except:
    print('Denominator cannot be 0. Try again.')
