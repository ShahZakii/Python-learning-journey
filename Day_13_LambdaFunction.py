# Python 

# Day 13: Lambda Function 

# lambda funtion in python.
# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the 
# following syntax:

# lambda arguments: expression.

# lambda functions are often used in situations where a small function is required for a short period of time. They are commonly 
# used as arguments to higher-order functions, such as map,filter,and reduce.
# Here is an example of how to use a lambda function:

# function to double the input.
def double(x):
    return x * 2

print(double(4))

# lambda function to double the input.
d = lambda x: x * 2
print(d(5))

# The above lambda function has the same functionality as the same function defined earlier. However, the lambda function is 
# anonyous,as it does not have a name.

# Lambda functions can have multiple arguments, just like regular functions. 
# Here is an example of a lambda function with multiple arguments:

# lambda function to calculate the product of two numbers.
product = lambda x,y: x * y
print(product(5,7))

# Lambda functions can also include multiple statements, but they are limited to a single expression. For example:

# lambda function to calculate the product of two numbers.
product_print = lambda x,y: print(f'{x} X {y} = {x*y}')
product_print(4,8)

# In the above example, the lambda function includes a print statement, but it is still limited to a single expression.

# Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce which we will look 
# into later.