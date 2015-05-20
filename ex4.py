<<<<<<< HEAD
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
=======
# There are 100 cars. 
cars = 100
# There is space for 4 people in each car. 
space_in_a_car = 4.0
# There are 30 drivers
drivers = 30
# There are 90 passengers
passengers = 90
# The number of cars not being driven is number of cars less number of drivers
cars_not_driven = cars - drivers
# The number of cars being driven is equal to number of drivers
cars_driven = drivers
# The space available for carpoolers is cars being driven times space in each car
carpool_capacity = cars_driven * space_in_a_car
# The average number of passengers per car is total passengers div by cars driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
>>>>>>> 5e39aee329f96af716a2e0fba84872881cd73540
print "We need to put about", average_passengers_per_car, "in each car."