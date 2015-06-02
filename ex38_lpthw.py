# assigns variable ten_things
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things ni that list. Let's fix that."

# splits ten_things variable on spaces and creates list called stuff
stuff = ten_things.split(' ')
# creates second list called more_stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# initiates while loop with rule being 'number of items in list "stuff" is not equal to 10'
while len(stuff) != 10:
	# pops off last item from list next_one
	next_one = more_stuff.pop()
	# prints string + popped item from next_one
	print "Adding: ", next_one
	# appends next_one to stuff list
	stuff.append(next_one)
	# prints string, counts number of items in stuff after most recent append
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

# prints item from stuff in position 1
print stuff[1]
# prints last item in stuff
print stuff[-1] # whoa! fancy
# prints last item in stuff, again (and pops it)
print stuff.pop()
# prints items in stuff separated by spaces
print ' '.join(stuff) # what? cool!
# prints items from stuff in positions 3 and 4 and joins with a #
print '#'.join(stuff[3:5]) # super stellar!



