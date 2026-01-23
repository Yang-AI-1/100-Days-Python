print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("What exit are you taking? left or right?\n").lower()
if direction == "right":
    print("Oh no you got stuck in traffic, game over!!")
elif direction == "left":
    drown = input("What do you wanna do next, swim to the island or wait for a boat?\n").lower()
    if drown == "swim":
        print("Game over man.You got bitten by a shark!!")
    elif drown == "wait":
        door = input("Which door do you wanna enter. Red, Blue or Green?\n").lower()
        if door == "red":
            print("Red doors are an obvious red flag. You loose!")
        elif door == "blue":
            print("Blue is basically diving back into the water. You loose!")
        elif door == "green":
            print("Green means go boys lets gooo! You won mehn")
        else:
            print("That's kinda cringe bro.Stop sitting on the fence.")
    else:
        print("That's not even an option man. Die! Game over!")


else:
    print("Thats not even eligible. Game over man!")

#  A backslash is used to escape useful symbols.


