"""
Challenge: Sum of List Items
Medium
Problem Description
Write a program to create a class that will have a method that returns the sum of a student's scores stored in a list.

Create a class

Create a class named Student that will have an attribute named scores (which will take a list).
Create the __init__() method to initialize the scores attribute.
Create a method named get_scores_sum() that adds individual items of a list and returns it. Use the built-in sum() function for it.
Outside of the Class

Create a scores variable and assign the [55, 75, 80, 62, 77] list to it.
Create an object s1 of Student with the list as an argument.
Call the get_scores_sum() method and store the return value in the total variable.
Print the total variable.
Example
Expected Output

349
"""

# create the Student class
class Student:
    def __init__(self,scores):
        
    # use the __init__() method to initialize the scores attribute  
        self.scores = scores
  
    # create the get_scores_sum() method that returns the sum of scores items
    def get_scores_sum(self):
        return sum(self.scores)
  
  
# create the scores variable
scores = [55, 75, 80, 62, 77]

# create an object of Student by passing scores as an argument
s1 = Student(scores)

# call the get_scores_sum() method using the s1 object
total = s1.get_scores_sum()

# print total
print(total)
