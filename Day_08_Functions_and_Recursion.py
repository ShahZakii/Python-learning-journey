# Python 

# Day 8: Functions.

# 1.Function Definition: A function is a block of code that performs a specific task when it is called. Functions
# help us to use the existing code again. It ensures code reusability.
# Syntax: 
# def function_name():
#          block of code 

# function_name()  calling the funtion

# 2.There are two types of functions.

# a. Built-in functions.
# These functions are defined and pre-coded in python. some examples of built-in functions are as follows:
# min(),max(),len(),sum(),type(),range(),dict(),list(),tuple(),set(),print(),etc.

# b. User-defined functions.
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

def geometrymean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def isgreater(a,b):
    if (a > b):
        print("First number is greater:")
    else:
        print("Second number is greater:")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

geometrymean(a,b)
isgreater(a,b)

# 3. Parameters and Arguments.
# Parameters are the variable names listed in a function’s definition.
# Arguments are the actual values you pass to a function when you call it.

def sum(a,b):            # a and b are parameters
    return a+b          


# 4. Recursion 
# Recursion is a technique where a function calls itself to solve a problem by breaking 
# it into smaller versions of the same problem.

# Example   

def fac(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fac(n-1)

print(fac(5))