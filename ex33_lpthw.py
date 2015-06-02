i = 0
numbers = []
end = 15

# updated so that while loop is now a function
def counter(start):
	while start < end:
		print "At the top i is %d" % start
		numbers.append(start)

		add = 2
		start = start + add
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % start

# messing around with a function from scratch / using for loops
# def counter(start):
# 	print "At the top i is %d" % start
# 	for num in range(start, 7):
# 		print "Adding %d to the list." % num
# 		numbers.append(num)
# 		print "Numbers now: ", numbers
# 		print "At the top i is %d" % num
# 		print "At the bottom i is %d" % num

counter(0)

print "The numbers: "

for num in numbers:
	print num