"""
Challenge: Compute Area and Perimeter
Medium
Problem Description
Create a program to compute the area and perimeter of a square using class. If you don't know, a square is a rectangle with equal sides.

Create a class

Create a class named Square that has an attribute named length.
Use __init__() to initialize the length attribute.
Create the compute_area() method to compute the area of a square and return it.
Create the compute_perimter() method to compute the perimeter of a square and return it.
Outside the class

Take integer input from the user and store it in the length variable.
Create an object of the Square class by passing length as an argument.
Call the compute_area() method and print the area.
Call the compute_perimeter() method and print the perimeter.
By the way, the area of a square is equal to length * length, and the perimeter of a square is equal to 4 * length.

Example
Test Input

2
Expected Output

4
8

"""

# create the class
class Square:
    def __init__(self, length):
    # define the __init__() method
        self.length = length
  
    # define the compute_area() method
    def compute_area(self):
        print(length * length)
    # define the compute_perimeter() method
    def compute_perimeter(self):
        print(4 * length)
# get integer input
length = int(input())
# create an object of Square    
obj_sq = Square(length)
# call compute_area() and print the area
obj_sq.compute_area()
# call compute_perimeter() and print the perimeter
obj_sq.compute_perimeter()

