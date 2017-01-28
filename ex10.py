# # Exercise 10: What was that?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

slim_cat = '''
I'll do a slim list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat
print slim_cat
print "%s%r" % ("\t", "\t")

# while True:
#     for i in ["/", "-", "|", "\\", "|"]:
#         print "%s\r" % i,
