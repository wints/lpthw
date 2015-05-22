# prints string
print "How old are you?",

#requests raw input from user, sets variable age
age = raw_input()

#requests raw input from user, sets variable height
print "How tall are you?",

#requests raw input from user, sets variable height
height = raw_input()

#requests raw input from user, sets variable height
print "How much do you weigh?",

#requests raw input from user, sets variable weight
weight = raw_input()

# prints string; uses string insertion to 
print "So, you're %r old, %r tall, and %r heavy." % (
	age, height, weight)

# print type(age)