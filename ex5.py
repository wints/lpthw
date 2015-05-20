	name = 'Mike Winters'
age = 29 # true
height = 71 #inches
weight = 185 # lbs
weight_kilos = weight * 0.453
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

print weight_kilos
print "In Germany, he weighs %r kilos." % (weight * 0.453)
