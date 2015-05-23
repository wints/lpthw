# defines function with cheese_count and boxes_of_crackers arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# prints cheese_count in string
	print "You have %d cheeses!" % cheese_count
	# prints boxes_of_crackers in string
	print "You have %d boxes of crackers!" % boxes_of_crackers
	# prints string
	print "Man that's enough for a party!"
	# prints string plus newline
	print "Get a blanket.\n"

# prints string
print "We can just give the function numbers directly:"
# calls function with args of 20 and 30
cheese_and_crackers(20, 30)

# prints string
print "OR, we can use variables from our script:"
# assigns variable amount_of_cheese
amount_of_cheese = 10
# assigns variable amount_of_crackers
amount_of_crackers = 50

# calls function with newly assigned vars as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints string
print "OR, we can use variables from our script:"
# assigns variable amount_of_cheese
amount_of_cheese = 100
# assigns variable amount_of_crackers
amount_of_crackers = 37

# calls function with newly assigned vars as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints string
print "We can even do math inside too:"
# calls function with simple arithmetic as arguments
cheese_and_crackers(10 + 20, 5 + 6)

# prints string
print "And we can combine the two, variables and math:"
# calls function with sums of variables and integers  for arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)