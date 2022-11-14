"""
Challenge: Compute Perimeter
Easy
Problem Description
Create a program to compute the perimeter of a triangle using OOP.

Create a Class

Create a class named Triangle that will have three attributes x, y, z.
Use the __init__() method to initialize attributes.
Create a method named get_perimeter() to compute the perimeter and return it.
Outside of the class

Take three integer inputs and assign them to a, b and c respectively. These are the sides of a triangle.
Create an object of the Triangle class with these values.
Call the get_perimeter() method using the object which returns the perimeter.
Print the perimeter.
Example
Test Input

1
2
3
Expected Output

6
"""

# create the Triangle class
class Triangle:
    # define the __init__() method
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # define the get_perimeter() method
    def get_perimeter(self):
        return (self.x + self.y + self.z)
# take three integer inputs
a = int(input())
b = int(input())
c = int(input())

# create an object of the Triangle class
obj1 = Triangle(a ,b ,c)

# call the get_perimeter() method
perimeter = obj1.get_perimeter()
# print the perimeter
print(perimeter)
