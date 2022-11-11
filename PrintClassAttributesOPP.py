Example #10
"""
Challenge: Object Attributes
Medium
Problem Description
Write a program to create a class and print attributes using a method of the class.

Create a class

Create a class named Bicycle.
Inside this class, create two methods named: __init__() and print_attributes().
The class will have two attributes: gear and speed which should be initialized inside __init__().
Inside the print_attributes() method, print the gear attribute followed by the speed attribute in two separate lines.
Outside of the class

Create an object named bicycle1 of the Bicycle class. The gear and speed attributes of this object should be 4 and 80 respectively.
Call the print_attributes() method using the bicycle1 object.
For hints, see the code outline.

Example
Expected Output

4
80
"""

# create the class
class Bycycle:
    def __init__(self, gear, speed):
        # initialize attributes
        self.gear = gear
        self.speed = speed
    
    # create the print_atributes() method 
    def print_attributes(self):
        print(self.gear)
        print(self.speed)

# create the object with 4 and 80 as arguments
bicycle1 = Bycycle(4 , 80)

# call print_atributes() using bicycle1
bicycle1.print_attributes()
