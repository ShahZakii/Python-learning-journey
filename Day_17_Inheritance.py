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


# 1.Single Inheritance
# A child class inherits from one parent class.
# This is the most basic and common type of inheritance.

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

obj = Child()
obj.show()
obj.display()


# 2.Multiple Inheritance
# A child class inherits from more than one parent class.
# Python supports this directly.

class Father:
    def father_method(self):
        print("Father's method")

class Mother:
    def mother_method(self):
        print("Mother's method")

class Child(Father, Mother):
    def child_method(self):
        print("Child's method")

obj = Child()
obj.father_method()
obj.mother_method()
obj.child_method()


# 3.Multilevel Inheritance
# A class is derived from another derived class.
# Inheritance flows in levels (grandparent → parent → child).

class Grandparent:
    def gp_method(self):
        print("Grandparent method")

class Parent(Grandparent):
    def parent_method(self):
        print("Parent method")

class Child(Parent):
    def child_method(self):
        print("Child method")

obj = Child()
obj.gp_method()
obj.parent_method()
obj.child_method()


# 4.Hierarchical Inheritance
# Multiple child classes inherit from a single parent class.

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()


# 4.Hybrid Inheritance
# A combination of two or more types of inheritance
# (e.g., multiple + multilevel).

class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C(A):
    def method_c(self):
        print("Class C")

class D(B, C):
    def method_d(self):
        print("Class D")

obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()
