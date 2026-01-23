# Python 

# Day 17: Inheritance in Python.
# Topics covered: Inheritance, Types of inheritance 

# When a class derives from another class. The child class will inherit all the public and protected properties and methods 
# from the parent class. In addition, it can have its own properties and methods, this is called as Inheritance.


# class Baseclass:
#     body of the base class
# class Derivedclass(Baseclass):
#     body of the derived class

# Derived class inherits features from the base class where new feature can be added to it. 
# This results in re-usability of code.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}.")

class Programmer(Employee):
    def showlanguage(self):
        print("The programming language is Python.")

e1 = Employee("Zia", 8756538)
e1.showDetails()

e2 = Programmer("zaki", 987455648)
e2.showDetails()
e2.showlanguage()

# Types of Inheritance:
# 1- Single Inheritance.
# 2- Multiple Inheritance.
# 3- Multilevel Inheritance.
# 4- Hierarchical Inheritance.
# 5- Hybrid Inheritance.