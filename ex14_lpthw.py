# imports argv module
from sys import argv

# unpacks varaibles
script, user_name, city = argv
# assigns variable prompt
prompt = '-->'

# prints and inserts strings
print "Hi %s, I'm the %s script. I live in %s." % (user_name, script, city)

# prints string
print "I'd like to ask you a few questions."

# prints and inserts string
print "Do you like me %s?" % user_name

# assigns variable from raw input
likes = raw_input(prompt)

# prints and inserts string
print "Where do you live %s?" % user_name

# assigns variable from raw input
lives = raw_input(prompt)

# prints and inserts string
print "What kind of computer do you have?"

# assigns variable from raw input
computer = raw_input(prompt)

# prints and inserts string
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)