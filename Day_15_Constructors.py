# Python

# Day 15: Constructors.
# Topics covered: Constructor definition, Types of constructor, Practice question 

# A constructors is a special method in aclass used to create and initialize an object of a class. There are different 
# types of constructors.
# Constructors is invocked automatically when an object of a class is created. 

# A constructor is a unique function that gets called automatically when an object is created of a class. The main 
# purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any 
# value other than None. 

# Syntax of Python Constructor:
# def __init__(self):

# init is one of the reserved function in Python. In Object Oriented Programming, it is known as a constructor by 
# defining the function name with same class name. 

# Types of Conctructors in Python. 
# 1- Parameterized Constructor
# 2- Default Constructor

# Parameterized Constructor in Python. 
# When the constructor accepts arguments along with self, it is known as parameterized constructor. 

# These arguments can be used inside the class to assign the values to the data member. 
# Example. 

class details:
    def __init__(self, animal, group):
        self.animal = animal 
        self.group = group
    
    def info(self):
        print(f"{self.animal} belongs to the {self.group} group.")

a = details("Lion", "Wild")
a.info()

b = details("Goat", "Pet")
b.info()


# Default Constructor in Python. 
# When the constructor doesn't accept any arguments from the object and has only one argument, self, in the constructor, it 
# is known as a Default constructor. 
# Example:

class details:
    def __init__(self):
        print("This is Default Constructor in Python.")

obj = details()


# Practice Questions 
# Create student class that takes name & marks of 3 subjects as arguments in constructor. 
# Then create a method to print the average.

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for i in self.marks:
            sum += i
        avg = sum/len(self.marks)
        print(f"The avg marks of {self.name} is {avg}.")
        

s1 = student("Tony Stark", [87,99,98])
s1.avg_marks()
