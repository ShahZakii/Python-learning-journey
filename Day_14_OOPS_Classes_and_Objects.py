# Python 

# Day 14: OOPS and Classes and Objects
# Topics covered: Introduction to OOPs, Classes and objects

# Introduction to Object-Oriented Programming in Python: In programming languages, mainly there are two approaches that are used 
# to write program or code.

# 1- Procedural Programming.
# 2- Object-Oriented Programming.

# Python Classes and Objects.

# A class is a blueprint or a template for creating objects, providing initial values for  state (member variables or attributes),
# and implementations of behaviour (member functions or methhods). The user-defined objects are created using the class keyword.

# Creating a Class.
# Let us now create a class using the class keyword.

class details:
    name = "zaki"
    age = 20

# Creating an Object:
# Object is the instance of the class used to access the properties of the class. Now lets create an object of the class. 

obj1 = details()

# Example.

class person:
    name = "Zaki"
    occupation = "Student"
    course = "BCA"

a = person()

print(a.name)
print(a.occupation)
print(a.course)

# self parameter 
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. 

# It must be provided as the extra parameter inside the method definition.

class person:
    name = "Zaki"
    occupation = "Student"
    course = "BCA"

    def info(self):
        print(f"My name is {self.name} and I'm a {self.occupation} of {self.course}.")

a = person()
a.info()


# If i want to change the information. Simply do this

b = person()
b.name = "Shah"
b.occupation = "Good Student"
b.info()