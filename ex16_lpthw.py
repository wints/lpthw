# imports argv module from sys package
from sys import argv

# unpacks variables for argument
script, filename = argv

# prints string with insertion
print "We're going to erase %r." % filename

# prints string
print "If you don't want that, hit CTRL-C (^C)."

# prints string
print "If you do want that, hit RETURN." 

# prints ? prompt for user
raw_input("?")

# prints string
print "Opening the file..."
# opens filename, 'w'
target = open(filename, 'w')

# prints string
print "Truncating the file. Goodbye!"
# removes starter text from file
target.truncate()

# prints string
print "Now I'm going to ask you for three lines."

# assigns variable line 1, prompts user for input
line1 = raw_input("line 1: ")
# assigns variable line 2, prompts user for input
line2 = raw_input("line 2: ")
# assigns variable line 3, prompts user for input
line3 = raw_input("line 3: ")

#prints string
print "I'm going to write these to the file."

# # writes line 1 to open file
# target.write(line1)
# # newline
# target.write("\n")
# # writes line 2 to open file
# target.write(line2)
# # newline
# target.write("\n")
# # writes line 3 to open file
# target.write(line3)
# # newline
# target.write("\n")

# attempt to combine to one target.write()
target.write( "%s\n%s\n%s" % (line1, line2, line3))

# prints string
print "And finally, we close it."
#closes open file
target.close()