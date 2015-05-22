# imports argv module
from sys import argv

# unpacks variables for argument
script, filename = argv

# assigns variable txt to the opened txt file specified in argument
txt = open(filename)

# prints string plus insertion 
print "Here's your file %r:" % filename

# prints contents inside txt variable, which is file specified in argument
print txt.read()

# prints string
print "Type the filename again:"

# assigns variable file_again and prompts filename from user
file_again = raw_input("> ")

# assigns variable txt_again and opens filename requested from user on line 20
txt_again = open(file_again)

# prints text inside the file, though from a different variable (with the same contents)
print txt_again.read()

txt.close()
txt_again.close()