# Exercise 20: Functions and Files
# Using functions and files together.

from sys import argv

script, input_file = argv  # unpacking

# print the contents of the file
def print_all(file):
    print file.read()

# put cursor back at the start of the file
def rewind(file):
    file.seek(0)

# print a line from the current cursor position
def print_a_line(line_count, file):
    print line_count, file.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines from start of file:"

current_line = 1
print_a_line(current_line, current_file)

# increase the current line count to be in sync with file position.
current_line += 1
print_a_line(current_line, current_file)

current_line += 1  # current_line + 1
print_a_line(current_line, current_file)
