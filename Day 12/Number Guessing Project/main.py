# TODO. Create a list that contains numbers between 1 and 100 an crate a variable(global) assigned to the number chosen.
# TODO. Define functions for the easy mode and hard mode.
# TODO. Define a function to compare the outcomes that returns a value(string)
# TODO. Inside each function(hard and easy), Construct a loop that factors in attempts 10 for easy 5 for hard.
import random
from art import logo

# Upon revision creation of an entirely new list is useless. Just... from random import randint, <-- Imports random integers. and It can be assigned to a variable as randint(1, 100) for random integers of that range.
list_of_numbers = []
for _ in range(1,101):
    list_of_numbers.append(_)
# List of numbers is now global with numbers from range 1 to 100

my_actual_guess = -1


def compare(my_guess, actual_number):
    """This function compares my guess to the actual number"""
    if actual_number == my_guess:
        return "You've made the guess!"
    elif actual_number > my_guess:
        return "Too low."
    elif my_guess > actual_number:
        return "Too High."
    return None

def easy_mode(the_guess, the_number):
    """This function loops for 10 attempts."""
    attempts = 10
    for _ in range(10):
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1
        the_guess = int(input("Make a guess:"))
        result_of_guess = compare(my_guess=the_guess,actual_number=the_number)
        if result_of_guess == "You've made the guess!":
            return f"You've made the guess!! in { _ + 1} attempts!"
        if attempts == 0:
            return f"You've run out of attempts. The actual number was {the_number} "
        elif result_of_guess == "Too low.":
            print("Too low.")
            print("Guess again.")
        elif result_of_guess == "Too High.":
            print("Too High.")
            print("Guess again.")



def hard_mode(the_guess, the_number):
    """This function loops for 10 attempts."""
    attempts = 5
    for _ in range(5):
        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1
        the_guess = int(input("Make a guess:"))
        result_of_guess = compare(my_guess=the_guess,actual_number=the_number)
        if result_of_guess == "You've made the guess!":
            return f"You've made the guess!! in { _ + 1} attempts!"
        if attempts == 0:
            return f"You've run out of attempts. The actual number was {the_number} "
        elif result_of_guess == "Too low.":
            print("Too low.")
            print("Guess again.")
        elif result_of_guess == "Too High.":
            print("Too High.")
            print("Guess again.")


#The only thing separating Angela's code and mine, is the function that is used to get the number of turns.
# The play game function then encapsulates and makes decisions based on the number of turns obtained.

Play_game = True
while Play_game:
    the_random_number = random.choice(list_of_numbers) #Keep the random number module in the loop to avoid using the same random number everytime.
    print(logo)
    print("Welcome to the number guessing game!")
    print("Im thinking of a number between 1 and 100. Whats it gonna be?")
    select = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if select == "easy":
        print(easy_mode(my_actual_guess, the_random_number))
    elif select == "hard":
        print(hard_mode(my_actual_guess, the_random_number))
    continue_game = input("Do you wanna keep going? Type 'y' if so and type 'n' if no.").lower()
    if continue_game == "y":
        print("\n" * 100)
    elif continue_game == "n":
        Play_game = False
        print("Oki.Goodbye!!")

