# Python

# Day 4: List and Tuples.
# Topics covered: List, List slicing, List jumping, List Functions, Tuple, Tuple slicing, Tuple Functions

# 1. list

list = ["zaki", 20, 5.11]

print(list)


# List slicing

list2 = [2,4,6,3,7]
print(list2[1:4])                       # it goes till n-1

# List jumping

list3 = [3,5,7,44,75,3,454,3]
print(list3[1:7:2])                     # [start:stop:step]


# List Functions

# 1- list.append() #adds elements in the list.
# 2- list.sort()  #sorting the list in ascending order.
# 3. list.sort(reverse=True) #sort the list in descending order.
# 4. list.reverse() #reverse the list.
# 5. list.count() #used to return the number of times a specified value appears in a list
# 6. list.copy() #Returns copy of the list.


# 2. Tuple 

tup = (2,4,6,23,78,44,35)
print(tup)

# Tuple slicing

print(tup[1:4])

# Tuple Functions

# 1- tup.count() #Returns the number of times a value appears in a tuple.
# 2- tup.index() #Returns the index of the first occurrence of a value.


# Practice questions:

# Program to take user input and print a list:

movies = []

m1 = input("Enter first movie: ")
m2 = input("Enter second movie: ")
m3 = input("Enter third movie: ")
movies.append(m1)
movies.append(m2)
movies.append(m3)

print(movies)


# Program to sort the list in ascending order

lst = [3,56,7,65,44,23,75,2]
lst.sort()
print(lst)