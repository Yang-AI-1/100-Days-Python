from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#TODO.Read the documentation for the other files and determine how to use them to refactor the coffee machine.
menu = Menu() #<--- Menu object, allows us to access attributes and methods of the menu class.
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    customer_order = input(f"What would you like?{menu.get_items()}?")

    if customer_order == "report":
        coffee_maker.report()
        money_machine.report()

    elif customer_order == "off":
        is_on = False

    elif menu.find_drink(customer_order) is None:  #Checks for relevant input.
        print("Please type the correct drink.(Check for correct spelling.)")

    else:  # This is the path taken when the customer had a correct input.
        drink = menu.find_drink(customer_order)
        enough_resource = coffee_maker.is_resource_sufficient(drink)
        if not enough_resource:
            pass    #We actually don't need this block of code. If its false it'll just pass.

        else:
            drink_cost = drink.cost
            transacted = money_machine.make_payment(drink_cost)

            #Checks if transaction was successful.
            if not transacted:
                pass  #If the payment is rejected it loops back to the top

            else:
                coffee_maker.make_coffee(drink)  #Also takes the menu item order that contains all the









