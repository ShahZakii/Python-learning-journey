# Python 

# Docstrings in python.

# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**3)

square(3)
print(square.__doc__)