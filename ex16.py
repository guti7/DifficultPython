# Exercise 16: Reading and Writing Files

# File commands:
# close -- Closes the file.
# read -- Reads the contents of the file. You can assign the result.
# readline -- Reads just one line of a text file.
# truncate -- Empties the file. The contents will be lost.
# write('stuf') -- Writes "stuff" to the file.

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# continue with execution
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')  # needs to be open for writing/editing

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
string = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(string)

print "And finally, we close it."
target.close()
