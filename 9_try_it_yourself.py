# Title: Writing and Reading Files
# Author: Dr. Mary Lebens
# Last updated 2/26/2022
# Description: Write a list of 
# ice cream flavors to a file and 
# then reads the file to display the flavors.

#Writing Starts:
with open("icecreamflavors.txt", "w") as f:
	pass
	f.write("Rocky Road\n")
	f.write("Mint Chocolate\n")
	f.write("Strawberry\n")
	f.write("Vanilla\n")
	f.write("Fudgy Brickle\n")

	
#Reading Files:
with open("icecreamflavors.txt", "r") as f:
	pass
	f_contents = f.read()
	print(f_contents)
	
    #output:
# Rocky Road
# Mint Chocolate
# Strawberry
# Vanilla
# Fudgy Brickle

# Now practice writing and reading a file.
# Write code that writes a list of pizza toppings
# to a file and then reads the file and displays
# the list of toppings.

#Writing Starts:
with open("pizzaToppings.txt", "w") as f:
	pass
	f.write("Pepperoni\n")
	f.write("Extra Cheese\n")
	f.write("Mushrooms\n")
	f.write("Red Pepper\n")
	f.write("Sausage\n")

	
#Reading Files:
with open("pizzaToppings.txt", "r") as f:
	pass
	f_contents = f.read()
	print(f_contents)