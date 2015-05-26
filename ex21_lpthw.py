# defines function that adds and returns a and b
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# defines function that subtracts and returns a and b
def subtract (a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

# defines function that multiplies and returns a and b
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

# defines function that divides and returns a and b
def divide(a, b): 
	print "DIVIDING %d / %d" % (a, b)
	return a / b

# prints string
print "Let's do some math with just functions!"

# assigns four variables using functions; specifies the arguments to use
age = add(30, 5)
height = subtract (78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# prints string; inserts integer variables returned from functions
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# yes.
# 35 + 74 - 180 * 50 / 2
# 35 + 74 - 180 * 25
# 35 + 74 - 4500
# 35 - 4426
# -4391