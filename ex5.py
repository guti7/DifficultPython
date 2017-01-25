# Exercise 5: More Variables and Printing

name = 'guti'
age = 999
height = 70
weight = 160
eyes = 'Cafe'
teeth = 'Blancos'
hair = 'Obscuro'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee." % teeth

inches_to_cm = 2.54 / 1.00

height_cm = height * inches_to_cm

# pay attention to this line
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)

print "height in cm = %d" % height_cm
print "height in cm(.00) = %.2f" %height_cm
