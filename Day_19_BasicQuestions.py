# Python 

# Day 19: Basic Questions.

# Question 1: Program to find the factorial of a number.

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Enter a number to find the factorial: "))
fac = factorial(num)
print(fac)