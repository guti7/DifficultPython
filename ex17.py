# Exercise 17: More files
# Copy one file to another.

from sys import argv
# exists returns true if a file exists, based on its name in a string
from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)
#
# # We could do these on one line
# # in_file = open(from_file)
# # indata = in_file.read()
# indata = open(from_file).read()
#
# #print "The input file is %d bytes long" % len(indata)
#
# #print "Does the output file exist? %r" % exists(to_file)
# #print "Ready, hit RETURN to continue, CTRL-C to abort."
# # raw_input()
#
# out_file = open(to_file, "w")
# out_file.write(indata)
#
# print "Alright, all done."
#
# out_file.close()
# #in_file.close()

# one line long
open(to_file, 'w').write(open(from_file).read())
# When you reach the end of script. It should alaready be closed by Python
# no need to call .close() on a file
