# Python 

# Day 7: Dictionaries
# Topics covered: Definition, Different ways to print dictionary, dictionary.items(), Dictionaries Function.

# Dictionary definition :- Dictionaries are ordered collection of data items. They stored multiple data 
# items in a single variable. Dictionaries items are key-value pairs that are enclosed with curly brackets.
# Syntax: 
#     dictionary_name = {
#     key1: value1,
#     key2: value2,
#     key3: value3
# }



dic = {
    "name": "zaki",
    "height": 5.11,
    "eligible": True
}

# We are printing the dic keys and will give us the value pair of the key 

print(dic["name"])
print(dic["height"])
print(dic["eligible"])


# If we print the dic like this 
print(dic)
# Then it'll print the entire dictionary

print(dic.keys())                                      # it will print all the keys
print(dic.values())                                    # it will print all the values

# Dictionaries are the iterable object 

for i in dic:                                          # it will only print the key of the dictionary
    print(i)        


for i,j in dic.items():                                # this loop will print both key and value 
    print(f"The value corresponding to the key {i} is {j}")


# Dictionaries Functions

# 1.update()
# The update()method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new 
# key-value pair.

print("update method\m")
ep1 = {101: 34, 102: 56, 103: 98}
ep2 = {201: 43, 202: 85, 203: 77}
ep1.update(ep2)
print(ep1)

print()

# 2- clear()
# There are a few methods that we can use to remove items from dictionary.
print("clear()method")
ep1.clear()
print(ep1)

print()

# 3- pop()
# The pop() method removes the key-value pair whose key is passed as a parameter.
print("pop() method")
ep1 = {101: 34, 102: 56, 103: 98}
ep1.pop(101)
print(ep1)

print()

# 4- popitem()
# The popitem() method removes the last key-value pair from the dictionary.
print("popitem() method")
ep1 = {101: 34, 102: 56, 103: 98}
ep1.popitem()
print(ep1)

print()

# 5- del
# we can also use the del keyword to remove a dictionary item.
print("del method")
ep1 = {101: 34, 102: 56, 103: 98}
del ep1
# print(ep1)