# assigns variables people, cars, trucks
people = 30 
cars = 40
trucks = 15

# determines which code block to run based on number of cars vs people
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

# determines which code block to run based on number of cars vs trucks
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

# determines which code block to run based on number of people vs trucks
if people > trucks: 
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."