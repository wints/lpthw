from sys import exit

def google():
	print "You're doing well and cranking along at Google."
	print "They've offered you a promotion, or you can leave for a new role at a startup."
	print "Do you want the promotion or the startup?"
	google_promo = False

	while True:
		google_job = raw_input("promo or startup? ")

		if google_job == "promo" and not google_job:
			google_promo = True
			print "Congrats. You're rising through the ranks, grasshopper."
		elif google_job == "promo" and google_job:
			stagnate("You're in a rut and no longer ambitious. You enter a cycle of stagnation.")
		elif google_job == "startup":
			startup_2()
		else:
			print "I know it's tough and your emotions are important, but make a damn decision!"


def stagnate(why):
	print why, "Now bounce back!"
	exit(0)


def startup_1():
	print "Startup life is hard. Things aren't looking good right now."
	print "You can leave for another startup role. Do you want to jump ship, or do you want to stay loyal?"

	startup_choice = raw_input("leave or loyal? ")
	if startup_choice == "leave":
		print "Sometimes, you gotta do you. Good choice. You landed somewhere solid."
		startup_2()
	elif startup_choice == "loyal":
		print "Unfortunately, in the Valley, loyalty can drag you down."
		bankrupt("Your employer ran out of money. You're out of a job with a couple months of severance.")
	else:
		print "Quit yer waffling."
		stagnate("You're thoughtful and therefore not passionate enough. And out of a job.")

def bankrupt(why):
	print why, "Don't worry, it happens to a lot of startups."
	exit(0)

def startup_2():
    print "Well, you did it. You picked a red-hot Valley startup."
    print "But--wait--after a year, things are flatlining. Is...is the company spiraling?"
    print "You need to decide if you're going to see this through."	
    
    while True:
	    startup_choice_2 = raw_input("stay or go? ")
	    
	    if startup_choice_2 == "stay":
		    print "The company recovers and is acquired for a huge sum!"
		    print "You're going to be handsomely rewarded."
		    rich("Your new net worth is $3M.")
	    elif startup_choice_2 == "go":
		    print "It takes you years to find another exciting gig."
		    stagnate("You slog through boredom and burnout. Sh*t happens.")
	    else:
		    print "OK, you're lucky to have some time to think about this. What's the plan, Stan?"


def rich(why):
	print why, "Now take a vacation and live life!"
	exit(0)

def grad():
	print "Congrats, you've graduated from a great school and get to choose a Silicon Valley job!"
	print "Do you want to work for Google or a startup?"

	job = raw_input("google or startup? ")
	if job == "google":
		google()
	elif job == "startup":
		startup_1()
	else:
		print "Yes, I'm sure you'll enjoy taking that year off to find yourself."


grad()