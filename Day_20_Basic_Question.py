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


# Question 3:
# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print 
# the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

n = int(input())

integer_list = map(int,input().split())
integer_tuple = tuple(integer_list)

print(hash(integer_tuple))


Question 4:
# Given the participants' score sheet for your University Sports Day, you are required to find the 
# runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    rem_dup = set(arr)
    new_arr = list(rem_dup)
    new_arr.sort(reverse=True)
    print(new_arr[1])