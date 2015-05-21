<<<<<<< HEAD
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
=======
# defining variable x with formatted variable %d
x = "There are %d types of people." % 10

# defining variable  binary
binary = "binary"

# defining variable do_not
do_not = "don't"

# defining variable y with formatted variable %s and set of 2 variables to input
y = "Those who know %s and those who %s." % (binary, do_not)

# print x
print x

# print y
print y

# print string and input variable x
print "I said: %r." % x

# print string and input variable y
print "I also said: '%s'." % y

# define variable hilarious
hilarious = False

#define variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# print variable joke_evaluation and input variable hilarious
print joke_evaluation % hilarious

# define variable w
w = "This is the left side of..."

# define variable e
e = "a string with a right side."

# print variable w and variable e concatenated
>>>>>>> 5e39aee329f96af716a2e0fba84872881cd73540
print w + e