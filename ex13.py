# Exerecise 13: Parameters, Unpacking, Variables

# Write a script that also accepts commnand line arguments.
from sys import argv  # import sys

script, first, second, third = argv  # unpacking
# take what is in argv, unpack it, and assign it to these variables.
variable = raw_input("Give me an input:")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your input was:", variable
