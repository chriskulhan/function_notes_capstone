#Program Name: Dr. Mary's Taco Truck
#Author: Chris Kulhanek, following Dr. Mary's lecture
#Last updated 2.3.25

def displayMenu():
    #special style of comment: tells other developers what the function does: (using 3" on each side)
    """This function displays the menu to the customer."""
    print('Welcome to Chris\'s Taco Truck!')
    print('What would you like to eat?')
    print('Enter 1 for vegan burrito, 2 for pork nachos, or 3 for fish tacos.')

#TODO: get the order from the customer:
def getOrder():
    """This function gets the customer's food order"""
    #Use int to make sure the number is recorded as a number:
    orderNumber = int(input());
    #make a decision, did the user input a valid order number?
    if orderNumber == 1 or orderNumber ==2 or orderNumber ==3:
        print("Good choice! Your order will be right up.")
    #If user didn't order a valid number, prompt user to enter a new number    
    else: 
        print("You did not enter a valid choice. Enter 1, 2, or 3.")
        #get a correct order from the user
        orderNumber = input()
    #need to return the number to the function orderNumber
    return orderNumber   

def calculateTotal(orderNumber):
    """This function will determine the customer's total price."""
    if orderNumber == 1:
        price = 8.99
    elif orderNumber == 2:
        price = 5.99
    elif orderNumber == 3:
        price = 10.99
    #show total to the user:
    print("Your total is: " + str(price))    

#Call the menu function to display the menu to the customer
displayMenu()  

#output:
# Welcome to Chris's Taco Truck!
#What would you like to eat?
#Enter 1 for vegan burrito, 2 for pork nachos, or 3 for fish tacos.

#Call the order function to get the user's order:
orderNumber = getOrder()
#change the order number into a string so you can use concatenation to connect the two statements below:
print("Your order number is: " + str(orderNumber))

#Output:
#Welcome to Chris's Taco Truck!
#What would you like to eat?
#Enter 1 for vegan burrito, 2 for pork nachos, or 3 for fish tacos.

#input: 2

#Output
#Good choice! Your order will be right up.
#Your order number is: 2

#What if the user inputs the wrong thing? This only allows 1 wrong entry before it gets out:
#TODO rework this^^^ so you must enter 1, 2, or 3 before anything prints:

#Welcome to Chris's Taco Truck!
#What would you like to eat?
#Enter 1 for vegan burrito, 2 for pork nachos, or 3 for fish tacos.
#input: 4
#You did not enter a valid choice. Enter 1, 2, or 3.
#input: 5

#TODO this shouldn't print:
#Your order number is: 5

#Calculate the total and show it to your user:
calculateTotal(orderNumber)

#WOrks, but doesn't address the issue of 5 working
#Welcome to Chris's Taco Truck!
#What would you like to eat?
#Enter 1 for vegan burrito, 2 for pork nachos, or 3 for fish tacos.
#3
#Good choice! Your order will be right up.
#Your order number is: 3
#Your total is: 10.99