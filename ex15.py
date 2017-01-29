# Exercise 15: Reading Files

# Reading from a file and writing to a file
# use argv and raw_input to ask the user for a file name

# Import argv from sys module
from sys import argv

# unpack arguments into variables
script, filename = argv

# create a file object witht the given argument filename
text = open(filename)

# confirm filename to user
print "Here's your file %r:" % filename

# print the contents of the file object with read
print text.read()

# prompt the user for a file name
print "Type the filename again:"
file_again = raw_input("> ")

# create a new file object with new file name
text_again = open(file_again)

# print the contents of the new file
print text_again.read()

text.close()
text_again.close()
