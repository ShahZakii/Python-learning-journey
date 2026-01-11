# Python 

# Day 6: Sets
# Topics covered: Sets, Sets type coonversion, Empty sets, Sets Function(Union and intersection)


# Sets are the collection of data items. They store multiple data items in a single variable.
# Sets are seperated by commas and are enclosed with curly brackets.
# Sets are immutable meaning you cannot change items of the set once created. 


# 1. Sets

info = {"zaki", 5.11, 66, True}

for i in info:                    # we can access the elements of sets with the help of for loop.
    print(i)

# 2. Sets converting

lst = list(info)                  # if we want to access the sets with index number then first we have convert it to list.

print(lst[2])


# 3. Empty set 

zaki = ()                         # Empty set is made with the help of paranthesis().
print(type(zaki))



# 3. Sets Functions

# Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and 
# intersection on the sets just like in mathematics.

# 1. union
# Union contains all the items of both of the sets but only contain one item if two items are same. 

cities = {"Meerut", "Delhi", "Mumbai"} 
states = {"Gujarat", "Haryana", "Uttarakhand"}

both = cities.union(states)
print(both)


# 2. intersection
# intersection contains which items that are similar in both of the sets.

name = {"Pooja", "Jivi", "Ayesha"}
name2 = {"Jivi", "zaki", "karan"}

bothname = name.intersection(name2)
print(bothname)