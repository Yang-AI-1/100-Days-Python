import random
from art import logo

# Constants for difficulty levels (makes them easy to change later!)
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def compare_guess(guess, target):
    """
    Compares the user's guess to the target number.

    Returns:
        str: Feedback message ('correct', 'too_high', or 'too_low')
    """
    if guess == target:
        return 'correct'
    elif guess > target:
        return 'too_high'
    else:
        return 'too_low'


def get_difficulty():
    """
    Prompts user to select difficulty and returns number of attempts.

    Returns:
        int: Number of attempts based on difficulty
    """
    while True: # You want it to loop infinitely.
        choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if choice == 'easy':
            return EASY_ATTEMPTS
        elif choice == 'hard':
            return HARD_ATTEMPTS
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")


def play_game():
    """
    Main game logic - handles one complete round of the guessing game.
    """
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a fresh random number for THIS game
    target_number = random.randint(1, 100)
    attempts_remaining = get_difficulty()

    # Game loop - continues until win or out of attempts
    while attempts_remaining > 0:
        print(f"\nYou have {attempts_remaining} attempts remaining to guess the number.")

        # Get and validate user input
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        # Compare and provide feedback
        result = compare_guess(guess, target_number)

        if result == 'correct':
            print(f"🎉 You got it! The answer was {target_number}!")
            print(f"You solved it in {get_difficulty() - attempts_remaining + 1} attempts!")
            return True  # Return True to indicate a win
        elif result == 'too_high':
            print("Too high.")
        else:  # too_low
            print("Too low.")

        attempts_remaining -= 1

        if attempts_remaining > 0:
            print("Guess again.")

    # If we exit the loop, user ran out of attempts
    print(f"\n💀 You've run out of guesses. The number was {target_number}.")
    return False  # Return False to indicate a loss


def main():
    """
    Main entry point - handles game replay loop.
    """
    keep_playing = True

    while keep_playing:
        play_game()

        # Ask if they want to play again
        replay = input("\nDo you want to play again? Type 'y' for yes, 'n' for no: ").lower()

        if replay == 'y':
            print("\n" * 3)  # Clear some space (not 100 lines though! 😄)
        elif replay == 'n':
            print("Thanks for playing! Goodbye! 👋")
            keep_playing = False
        else:
            print("I'll take that as a no. Goodbye! 👋")
            keep_playing = False


# Only run the game if this file is executed directly
if __name__ == "__main__":
    main()