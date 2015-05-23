# imports argv module from sys package
from sys import argv
# imports exists module from os.path package
from os.path import exists

# unpacks scripts for argument
script, from_file, to_file = argv

# prints string, inserts 2 strings (variables assigned in argument)
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# here's how, but i'm not sure why in_file.close() errors out
# opens and reads source file and assigns to variable in_file
in_file = open(from_file).read()
# this used to read separately from the line above
# indata = in_file.read()

# prints string and inserts integer (the length of the file)
print "The input file is %d bytes long" % len(in_file)

# prints string and confirmts whether output file exists (if yes, prints True)
print "Does the output file exist? %r" % exists(to_file)
# prints string with user instructions
print "Ready, hit RETURN to continue, CTRL-C to abort."
# prompts user to either kill program or hit return
raw_input()

# sets variable out_file; opens to_file in write mode
out_file = open(to_file, 'w')
# writes source file into to new file variable
out_file.write(in_file)

# prints string
print "Alright, all done."

# closes relevant files
out_file.close()
in_file.close()