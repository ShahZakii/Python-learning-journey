# Python

# Day 3: Loops and Statments.
# Topics covered: for loop, while loop, break statement, continue statement, range.

# 1. for loop

# Printing character of a name using for loop.

name = "zaki"

for n in name:
    print(n)


# 2. while loop 
# Printing numbers from 1 to 5.

a = 1
while(a <= 5):
    print(a)
    a += 1

# Multiplication table using while loop.

table = int(input("Enter a number to print table: "))

n = 1

while(n <= 10):
    print(table,"X",n,"=",table*n)
    n += 1


# 3. break statement

# Program to stop the loop at 8 number.

for i in range(1,11):
    if(i == 8):
        print("Loop will stop here because of break statement.")
        break
    print(i)


# 4. continue statement.

# Program to skip the iteration.

for i in range(1,11):
    if(i == 5):
        print("Skipping the 5 iteration because of continue statement.")
        continue


# 5. Range.

# Printing numbers from 1 to 10.

for i in range(1,11):    # starting range and ending range (it goes till n-1).
    print(i)


# Printing numbers with three arguments (start,stop,step)

for i in range(2,21,2):

    print(i)                         # This will print all even numbers to 21.
