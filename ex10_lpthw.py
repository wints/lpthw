# defines variable tabby_cat, which includes a tab
tabby_cat = "\tI'm tabbed in."

# defines variable persian_cat, which includes a newline
persian_cat = "I'm split\non a line."

# defines variable backslash_cat, which includes an escape sequence
backslash_cat = "I'm \\ a \\ cat."

# defines variable fat_cat, which is a string with tab and newline formatting
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies 
\t* Catnip\n\t* Grass
"""

# my additional list, with string insertion
fat_cat_2 = """
And another list:
\t* %s
\t* %s 
\t* %s
""" % (tabby_cat, persian_cat, backslash_cat)

#prints various variables created in file
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print fat_cat_2

# me messing around with %r vs %s insertion with an escape sequence
quote_test = '"But I really \'like\' pizza!"'
print "And then he says to me, %r" % quote_test