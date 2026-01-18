# Python 

# Day 12: File Input/Output.
# Topics covered: Open a file, Modes of file, With statement.

# Open a File 

# Before we can performs any operations in a file, we must first open it. Python provides the open function() to open a file. 
# It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for  reading, 
# 'w' for writing, or 'a' for appending.

# Here's an example of how to open a file for reading.
# f = open("myfile.txt","r")  you can write it in single quote or double qoute.

# By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode.


# Modes of file.
# There are various mode in which we can open file.

# 1. read(r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode 
# if no mode passed as a parameter.

# 2. write(w): This mode opens the file for writing only and creates a new file if the file does not exist.

# 3. append(a): This mode opens the file for appending only and creates a new file if the file does not exist.
    
# 4. create(x): This mode creates a file and gives an error if the file already exists.

# 5. text(t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t
# refers to the text mode. 

# There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading 
# text, synonym of 'rt').

# 6. binary(b): used to handle binary file (images, pdfs,etc).

# Reading from a file.
# Once we have a file object, we can use various methods to read from a file.

# The read() method reads the entire contents of the file and returns it as a string.

f = open("myfile.txt","r")
# print(f)   # if we open it like this, then it will give error.
text = f.read()
print(text)
f.close()

# Writing to a File.
# To write to a file, we first need to open it in write mode.
# We can use the write() method to write to the file. 

f = open('myfile.txt','w')
f.write('Hello, World!')
f.close()
 


# The 'With' statement.
# Alternatively, you can use the with statement to automatically close the file after you are done with it.

with open('myfile.txt','a') as f:
    f.write('\nHello World!')