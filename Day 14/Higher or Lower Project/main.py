# TODO.Import the game_data file and create a function that randomly selects and returns a dictionary nested in the list.
import random
from game_data import data    #The game data has 50 nested dictionaries.
from art import vs,logo
#The four dictionary keys 'name' 'follower_count' 'description' 'country'.

def subject_selector():
    """Selects and returns a random dictionary from the data list."""
    return random.choice(data)

def format_account(account):
    """Takes an account dictionary and returns a printable string."""
    return f'{account["name"]}, a {account["description"]}, from {account["country"]}'

def check_answer(user_guess, a_followers, b_followers):
    """Takes the user's guess and follower counts, and returns True if correct, False otherwise."""
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

def game_loop():
    """Main function to run the Higher or Lower game."""
    print(logo)
    score = 0
    game_should_continue = True
    
    # Start with two random accounts
    account_a = subject_selector()
    account_b = subject_selector()

    while game_should_continue:
        # Ensure accounts are not the same
        while account_a == account_b:
            account_b = subject_selector()

        # Display the choices
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        # Get user input
        user_guess = input("Who has more followers? 'A' or 'B'? ").lower()

        # Check the answer
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

        # Clear screen for next round
        print("\n" * 30)
        print(logo)

        # Provide feedback and update score
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            # The winner moves to the 'A' position for the next round
            account_a = account_b
            account_b = subject_selector()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Start the game
game_loop()