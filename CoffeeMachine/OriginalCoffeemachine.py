MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


#TODO.Construct variables for how much resource the machine currently has.


#TODO.At any point in time the off prompt should turn off the coffee machine.
# Define a function to break the coffee making loop.

#TODO.When you type report the remaining resources should show.
# Define a report function.
def report(resources, money):
    """Gives information after every customer about how much resource is left in the machine"""
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: {money}")


#TODO.Check if resources are sufficient. If not print sorry there is not enough {Missing resource}

def give_resource_required(drink_name, menu):
    """Returns the required resource."""
    water_requirement = menu[drink_name]["ingredients"]["water"]
    coffee_requirement = menu[drink_name]["ingredients"]["coffee"]
    try:
        milk_requirement = menu[drink_name]["ingredients"]["milk"]
    except KeyError:
        milk_requirement = 0
    return water_requirement, coffee_requirement, milk_requirement
#The try block makes it perfect because the espresso doesn't have a milk requirement so it will set it to 0.




def evaluate_resource(available_water, available_milk, available_coffee, water, milk, coffee):
    """Determines if the coffee machine has enough resource to make the desired drink."""
    if water > available_water:
        print("Sorry there is not enough water.")
        return False
    elif milk > available_milk:
        print("Sorry there is not enough milk.")
        return False
    elif coffee > available_coffee:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True



#TODO. Coin processing. quarter = 0.25, dime = 0.10, nickel = 0.05, penny = 0.01. Calculate the total value.
# Define a function to calculate the amount of money given.

def payment_value():
    """Calculates the total value of coins that you input."""
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters?: ")) #Takes the value of quarters.
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return 0
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total

#TODO.Check if the transaction is successful.If not enough money say sorry, not enough money and refund.
# If it is actually successful report is triggered and change is given in two decimal places.
def transaction(cost_of_drink,payed_price):
    """This function determines if the transaction was successful.It also calculates and prints change given by the user."""
    if payed_price >= cost_of_drink:
        print("Transaction successful.")
        change = payed_price - cost_of_drink
        if payed_price == cost_of_drink:
            print("No change.")
            return True
        else:
            print(f"Here is ${change.__round__(2)} in change.")
            return True
    else:
        print(f"Transaction Failed. Insufficient funds.\n${payed_price} Refunded. ")
        return False




#TODO.Deduct the used resources and make the coffee. Update the report. Give the coffee and prompt again.


#TODO. Execute the coffee making in a main function.Money will be accumulated most likely in a global variable


def coffee_making(menu, resources):
    """Accommodates for a round of while the machine is on buying coffee."""
    money = 0
    coffee_round = True
    while coffee_round:
        user_command =  input("What would you like to order?(espresso/latte/cappuccino): ").lower()

       #Check If the user of the machine wants to turn off the machine.
        if user_command == "off":
            return False
       #Gives the report of available resource
        elif user_command == "report":
            report(resources, money)     #NOTE. When using an if elif else structure it naturally skips the block when one path is followed.
        elif user_command in menu:  #We add an elif statement in order to check if the command is inside the menu

           #Selection and delivery process.
            cost_of_drink = menu[user_command]["cost"]  #This is how much the selected drink costs
           #Find the requirements for the drinks
            water_requirement, coffee_requirement, milk_requirement = give_resource_required(user_command,menu)

            #Available resources
            water_available = resources["water"]
            milk_available = resources["milk"]
            coffee_available = resources["coffee"]

            enough_resource = evaluate_resource(water_available,milk_available,coffee_available,water_requirement,milk_requirement,coffee_requirement)

            if not enough_resource:
                # If not enough resources, we just loop back to the start.
                # We do NOT return False here, because that would turn off the machine!
                pass 
            else:  #Prompt the payment if the resources are sufficient.
                payment = payment_value()
                transacted = transaction(cost_of_drink,payment)
                
                #The clock of code that follows up after the transaction was successful or flawed is nested in the else statement.
                if not transacted: 
                    # If transaction failed (not enough money), we loop back.
                    # Again, do NOT return False, or the machine turns off.
                    pass
                else:
                    money += cost_of_drink  #This is a source of error.
                    resources["water"] -= water_requirement
                    resources["milk"] -= milk_requirement
                    resources["coffee"] -= coffee_requirement
                    print(f"Here is your {user_command}. Enjoy!")
        else:
            print("Invalid choice. Please select (or spell) the correct drink.")

making_coffee = True

while making_coffee:
    making_coffee = coffee_making(MENU,resources)
