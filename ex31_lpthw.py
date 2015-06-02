print "You enter a dark room with three doors. Do you go through door #1, door #2, or door #3?"

door = raw_input(">")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input(">")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input(">")


	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
	print "You happen to have found a beach with a bar. What would you like to drink?"
	print "1. Island beer."
	print "2. Margarita."
	print "3. Mojito."

	drink = raw_input(">")


	if drink == "1":
		print "Can't go wrong with an island beer. Enjoy!"
	elif drink == "2":
		print "Coming right up, strong and with salt on the rim."
	elif drink == "3":
		print "Plenty more mint where that came from. I bet you feel refreshed."
	else:
	    print "We have what we have. Want to try again?"


else: 
	print "You stumble around and fall on a knife and die. Good job!"

