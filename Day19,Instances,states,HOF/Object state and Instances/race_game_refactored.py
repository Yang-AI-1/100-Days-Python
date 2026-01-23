from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=800)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# 1. Input Validation Logic
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a color:")

# Loop until the user enters a valid color or cancels
while user_bet is None or user_bet.lower() not in colors:
    if user_bet is None:
        screen.bye()
        exit()
    user_bet = screen.textinput(title="Invalid Color", prompt=f"Choose from: {', '.join(colors)}")

user_bet = user_bet.lower()

turtle_list = []
y_positions = [150, 100, 50, 0, -50, -100]

# 2. Refactored Turtle Creation (DRY Principle)
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index]) #Cleverly uses the indexed number to assign a color.

    # Start at -380 so the turtle is visible (at -400 it is half off-screen)
    new_turtle.goto(x=-380, y=y_positions[turtle_index])
    turtle_list.append(new_turtle)

def forward_speed():
    """ This function returns a random value for forward movement of the turtle."""
    return random.randint(0, 15)

is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        # 3. Check for finish line (380 accounts for turtle width)
        if turtle.xcor() > 380:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle} turtle is the winner!")
            break # Stop the loop so we don't get multiple winners
        
        turtle.forward(forward_speed())

screen.exitonclick()