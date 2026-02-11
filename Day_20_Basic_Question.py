# Day 20: Basic Questions.

# Question 1: Conditional Operator and If-elif-else.

# Given three integers a, b, and c, determine:
# If all three are equal, print "Equilateral"
# If any two are equal, print "Isosceles"
# If all three are different, print "Scalene"

# a = int(input("Enter First number: "))
# b = int(input("Enter Second number: "))
# c = int(input("Enter Third number: "))

# if ( a == b == c):
#     print("Equilateral")
# elif (a == b or b == c or c == a):
#     print("Isosceles")
# else:
#     print("Scalene")



# Question 2:   

num = list(map(int,input("Enter numgers seperated by space: ").split()))

num.sort(reverse=True)

print(num[1])

# Question 3:
# The included code stub will read an integer,n, from STDIN.
# Without using any string methods, try to print the following:
# 123...n
# Note that "..." represents the consecutive values in between.

n = int(input())
    
newstr = ""
for i in range(1,n+1):
    type = str(i)
    newstr += type
print(newstr)