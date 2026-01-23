import random
import art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# Check if the user has an ace plus a 10. Finding out if the list has both 10 and 11(BlackJack).
# Define a function called BlackJack that checks for blackjacks and replaces aces.
def Blackjack(user_score):
    """This function processes whether a blackjack is present in the game."""
    if user_score > 21:
        if 11 not in user_cards:
            print("Bust! You loose!")
            return 1
        elif 11 in user_cards:
            #TODO. Replace the 11 with 1 and calculate the score. If its above 21 it's a loss if it's not the game continues.
            user_cards[0] = 1  #TODO. Here we can instead do user_cards.remove(11) and .append(1).
            user_score = sum(user_cards)
            if user_score > 21:
                print("Bust!You loose!")
                return 1
            elif user_score < 21:
                return
    if 11 in user_cards and 10 in user_cards:
        print("BlackJack! You win!")
        return 1
    elif 11 in computer_cards and 10 in computer_cards:
        print("Dealer has Blackjack.You loose!")
        return 1


Playtime = True # Set up a while loop called play time.That loops the entire game when you loose
while Playtime:
    print(art.logo)
    # We have a user called the dealer. Were programming for the computer and the player.
    user_cards = []
    computer_cards = []
    # Problem: Random selection and appending of cards to the user's and computer's card list.
    user_cards.extend(random.sample(cards,2 ))
    computer_cards.extend(random.sample(cards,2))
    # TODO.Sort the lists in descending order to make indexing more simple.
    # TODO.This working is intended so that the 11 in the dec may be and the 0 index.It only works for simplified blackjack however.
    user_cards.sort(reverse=True)
    computer_cards.sort(reverse=True)
    Playtime2 = True
    while Playtime2:
        # Add up the users and computers scores
        #TODO.Angela's calculations had a different defined function for calculating the score
        user_score = sum(user_cards)
        computer_score = sum(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computers first card: {computer_cards[0]}")
        Black = Blackjack(user_score)
        if Black == 1:
            break
        choice = input("Type 'y' to get another card,type 'n' to stand:").lower()
        if choice == "y": #If they want another card. Append another card to the list and loop it for summing.
            user_cards.append(random.choice(cards))
        if choice == "n":
            Playtime2 = False #The 2nd loop will break.Allowing the computer to play.
            while computer_score < 17:
                computer_cards.append(random.choice(cards))
                computer_score = sum(computer_cards)
            print(f"Your final hand {user_cards}, final score,{user_score}")
            print(f"Computers final hand {computer_cards}, final score,{computer_score}")
            if computer_score > 21:
                print("Dealer went over! You win!")
            elif computer_score <= 21:
                if computer_score > user_score:
                    print("You went over. The dealer wins!!")
                elif computer_score < user_score:
                    print("You win!!")
                elif computer_score == user_score:
                    print("Push! That's a draw!!")
    continue_game = input("Do you wanna play a game of Blackjack? Type 'y' for yes and 'n' for no.").lower()
    if continue_game == "y":
            print("\n" * 100)
    if continue_game == "n":
            Playtime = False
            print("Well Goodbye!")



# TODO. This isnt really a todo, The difference between Angela's work and mine is that she created many different functions that execute different things.
# TODO. She has a deal card, calculate function>


