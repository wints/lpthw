print "It's been a long week, but luckily, you have a three-day weekend coming up." 
print "How would you like to spend it?"
print "1. By the beach."
print "2. Off in nature."
print "3. In a charming city."

destination = raw_input("Enter 1, 2, or 3: ")

if destination == "1":
	print "OK, let's get you to a beach."
	print "Would you rather see Spain or Croatia?"

	beach = raw_input("Spain or Croatia: ")

	if beach == "Spain":
		print "OK, just booked you a flight and hotel for San Sebastian!"
	elif beach == "Croatia":
		print "Great, you're going to Susak! Get to the airport!"
	else:
		print "OK, someone else will need to help you get to %s." % beach

elif destination == "2":
	print "Ah, good choice. I love nature."
	print "Would you rather visit Cinque Terre or Mont Blanc?"

	nature = raw_input("Cinque Terre or Mont Blanc: ")

	if nature == "Cinque Terre":
		print "I love that hike from Monterosso to Riomaggiore."
	elif nature == "Mont Blanc":
		print "Some of the grandest vistas this side of the Thames. Yodel-ay-hee-hoooo!"
	else:
		print "OK, someone else will need to help you get to %s." % nature


elif destination == "3":
	print "A hefty dose of old-world charm, coming right up!"
	print "Would you rather visit Prague or Amsterdam?"

	city = raw_input("Prague or Amsterdam:")

	if city == "Prague":
		print "Be sure to try the beer at the Strahov Monatic Brewery!"
	elif city == "Amsterdam":
		print "Rent a boat, tour the canals, and hey-ey-ey-ey...eat ribs every day."
	else:
		print "OK, someone else will need to help you get to %s." % city

else:
	print "Well, it sure would be nice to relax in Berlin too, wouldn't it?"
