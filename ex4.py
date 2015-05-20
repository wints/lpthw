# assigns cars variable
cars = 100

# assigns space_in_a_car variable
space_in_a_car = 4.0

# assigns drivers variable
drivers = 30

# assigns passengers variable
passengers = 90

# assigns cars_not_driven variable
cars_not_driven = cars - drivers

# assigns cars_driven variable
cars_driven = drivers

# assigns carpool_capacity variable
carpool_capacity = cars_driven * space_in_a_car

# assigns average_passengers_per_car variable
average_passengers_per_car = passengers / cars_driven

# prints string w/ car variable
print "There are", cars, "cars available."

# prints string w/ drivers variable
print "There will only be", drivers, "drivers available."

# prints string w/ cars_not_driven variable
print "There will be", cars_not_driven, "empty cars today."

# prints string w/ carpool_capacity variable
print "We can transport", carpool_capacity, "people today."

# prints string w/ passengers variable
print "We have", passengers, "to carpool today."

# prints string w/ average_passengers_per_car variable
print "We need to put about", average_passengers_per_car, "in each car."