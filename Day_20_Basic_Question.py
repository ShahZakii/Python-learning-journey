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


# Question 4:
# Given the participants' score sheet for your University Sports Day, you are required to find the 
# runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    rem_dup = set(arr)
    new_arr = list(rem_dup)
    new_arr.sort(reverse=True)
    print(new_arr[1])


# Question 5:
# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

# Let's try to understand this with an example.

# You are given an immutable string, and you want to make changes to it.

def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position + 1:]
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Question 6:
# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

# Hello firstname lastname! You just delved into python.

# Function Description

# Complete the print_full_name function in the editor below.

# print_full_name has the following parameters:

# string first: the first name
# string last: the last name

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Question 7:
#  You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase 
# letters and vice versa. 

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# Question 8:
# Consider a list (list = []). You can perform the following commands:

# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for i in range(N):
        user_input = input().split()
        
        if user_input[0] == "insert":
            lst.insert(int(user_input[1]), int(user_input[2]))
        elif user_input[0] == "print":
            print(lst)
        elif user_input[0] == "remove":
            lst.remove(int(user_input[1]))
        elif user_input[0] == "append":
            lst.append(int(user_input[1]))
        elif user_input[0] == "sort":
            lst.sort()
        elif user_input[0] == "pop":
            lst.pop()
        elif user_input[0] == "reverse":
            lst.reverse()


# Question 9:
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. 
# It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year 
# contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
# while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is 
# only necessary to complete the is_leap function.


def is_leap(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False
year = int(input())
print(is_leap(year))


# Question 10:
# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print 
# the result of hash(t).

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

n = int(input())

integer_list = map(int,input().split())
integer_tuple = tuple(integer_list)

print(hash(integer_tuple))


# Question 11:
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    split_line = line.split(" ")
    join_line = "-".join(split_line)
    return join_line

# Question 12:
# Create a stack using a list and perform operations:

# 1.push x → push element
# 2.pop → remove top element
# 3.top → print top element
# 4.size → print size of stack

n = int(input())
lst = []
for _ in range(n):
    command = input().split()
    if(command[0] == "push"):
        lst.append(int(command[1]))
    elif(command[0] == "pop"):
        if lst:
            lst.pop()
    elif(command[0] == "top"):
        if lst:
            print(lst[-1])
    elif(command[0] == "size"):
        print(len(lst))


# question 13:  You are given a list. Perform operations:
# 1. add x → add element
# 2. even → print all even numbers
# 3. odd → print all odd numbers
# 4. sum → print sum of list

lst = []
n = int(input())
for _ in range(n):
    command = input().split()
    if(command[0] == "add"):
        lst.append(int(command[1]))
    elif(command[0] == "even"):
        for i in lst:
            if(i % 2 == 0):
                print(i)
    elif(command[0] == "odd"):
        for i in lst:
            if(i % 2 != 0):
                print(i)
    elif(command[0] == "sum"):
       print(sum(lst))

# question 14: Given an integer n and n space-separated integers, create a tuple t.
#              Print the sum of elements and the hash of the tuple.

n = int(input())
create_lst = map(int,input().split())
t = tuple(create_lst)
print(sum(t))
print(hash(t))

# question 15: Given n integers, store them in a tuple t.
#              Print the number of unique elements in the tuple.

n = int(input())
t = tuple(map(int,input().split()))
unique_count = len(set(t))
print(unique_count)

# question 15: Create a tuple t from input.
               # Print how many times a given number x appears in the tuple.

n = int(input())
t = tuple(map(int,input().split()))
x = int(input())
count = 0
for i in t:
    if(i == x):
        count += 1
print(count)

# question 16: Create a tuple t and print the difference between the maximum and minimum elements.

n = int(input())
t = tuple(map(int,input().split()))
max_num = max(t)
min_num = min(t)
print(max_num - min_num)


# question 17: write a function: 
            # Given a string, reverse each word individually while maintaining the original word order.

def reverse_words(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
        
    return " ".join(reversed_words)

s = input()
print(reverse_words(s))

# question 18: Given a string, count how many uppercase and lowercase letters are present.

str = input()
uppercase_count = 0
lowercase_count = 0
for ch in str:
    if ch.isupper():
        uppercase_count += 1
    else:
        lowercase_count += 1
print(uppercase_count)
print(lowercase_count)

# question 19: Replace all spaces in the string with hyphens (-).

str = input()
print(str.replace(" ","-"))

# question 20: Given a string, remove duplicate characters while preserving the order of first occurrence.

str = input()
result = " "
for ch in str:
    if ch not in result:
        result += ch
print(result
