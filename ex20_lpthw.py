# imports argument module from sys package
from sys import argv

# unpacks arguments
script, input_file = argv

# creates function, which is a reading of a file passed in the function
def print_all(f): 
	print f.read()

# creates function which points to the start of the file (passes 0 bytes)
def rewind(f):
	f.seek(0)

# creates function that takes in a line count integer plus filename 
# and prints the line number integer and that line of the file
def print_a_line(line_count, f): 
	print line_count, f.readline(),

# opens input file (test txt file)
current_file = open(input_file)

# prints string plus newline
print "First let's print the whole file:\n"

# prints text file as is
print_all(current_file)

# prints string
print "Now let's rewind, kind of like a tape."

# seek to 0 bytes (beginning)
rewind(current_file)

# prints string
print "Let's print three lines:"

# sets current line var, prints current line integer and line from file
current_line = 1
print_a_line(current_line, current_file),

# sets current line var, prints current line integer and line from file
current_line += 1
print_a_line(current_line, current_file),

# sets current line var, prints current line integer and line from file
current_line += 1
print_a_line(current_line, current_file),