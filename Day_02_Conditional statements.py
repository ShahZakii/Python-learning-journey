
# Python Basics
# Day 2: Conditions (Decision making)

# 1. if-else

a = int(input("Enter your age: "))

if(a >= 18):
    print("Yes, you can drive: ")
else:
    print("No, you cannot drive: ")


# 2. if-elif-else

b = int(input("Enter a number: "))

if(b >= 1 and b <= 10):
    print("Number is between 1 to 10.")
elif(b >= 11 and b <= 20):
    print("Number is between 11 to 20.")
elif(b >= 21):
    print("Number is greater than 20.")
else:
    print("Number is zero or negative.")


# 3. Short hand if-else 

num = int(input("Enter a number: "))
print("Even") if num % 2 == 0 else print("Odd")                


# Program to find the greatest number among three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a >= b and a >= c):
    print(a," is greatest.")
elif(b >= a and b >= c):
    print(b," is greatest.")
else:
    print(c," is greatest.") 