# Python 

# Day 10: Enumerate function in python.

# The enumerate function is a built-in function in python that allows you to loop over a sequence (Such as a list,tuple,or string) 
# and get the index and value of each element in the sequence at the same time. Here's basic example of how it works.

marks = [44,77,2,4,6,99,6]

for mark in marks:
    print(mark)

print()


for index, mark in enumerate(marks):
    print(f"The index is {index} and the marks is:{mark}")

# Changing the start index.

# By default, the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an 
# argument to the enumerate function.

for index, mark in enumerate(marks , start = 1):
    print(index , mark) 