# Exercise 14: Prompting and Passing

# Use argv and raw_input together to ask the user for input

from sys import argv

script, user_name, role = argv  # unpacking
prompt = '> '

print "Hi %s, the %s, I'm the %s script." % (user_name, role, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
