# Exercise 18: Names, Variables, Code, Functions

# Introduction to Functions
# 3 objectives:
# They name blocks of code
# They take arguments
# Let you make your own "mini-scripts"


# This one is like scripts with argv
def print_two(*args):  # *args very similar to argv but for functions.
    arg1, arg2 = args  # unpacking
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    # The asterik tells python to put all arguments given into a list


# That *args is actually pointless, we can just do This
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1, arg2)  # no unpacking needed

# This just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# This one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Guti", "Seven")
print_two_again("Guti", "7")
print_one("First!")
print_none()
