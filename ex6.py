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
print w + e