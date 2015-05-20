# defines variable x and inserts int 10 in string
x = "There are %d types of people." % 10

# defines variable binary
binary = "binary"

# defines variable do_not
do_not = "don't"

# defines variable y, inserts strings 'binary' and 'do_not' into string
y = "Those who know %s and those who %s." % (binary, do_not)

# prints x
print x

# prints y
print y

# prints string and inserts variable x (also a string)
print "I said: %r." % x

# prints string and inserts variable y (also a string)
print "I also said: '%s'." % y

# defines variable hilarous
hilarious = False

# defiens variable joke_evaluation, which includes an insertion
joke_evaluation  = "Isn't that joke so funny?! %r"

# prints joke_evaluation, which includes variable hilarious in string
print joke_evaluation % hilarious

# defines variable w (string)
w = "This is the left side of..."

# defines variable e (string)
e = "a string with a right side."

# prints strings w and e
print w + e