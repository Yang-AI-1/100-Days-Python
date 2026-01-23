from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=800 ,height= 800) #In cases like these where there are integers as arguments, to make the code more readable using keyword arguments is recommended.
user_bet = screen.textinput(title="Make your bet:",prompt="Which turtle will win the race? Enter a color:") #The input text gets stored in this variable.
colors = ["red","orange","yellow","green","blue","purple"]
user_bet.lower()


#The code executes in hierarchy, hence the penup function is to appear earlier than the goto function.

tim = Turtle("turtle")
tim.penup()
tim.goto(-400,150)
tim.color(colors[0])

tod = Turtle("turtle")
tod.penup()
tod.goto(-400,100)
tod.color(colors[1])

tom = Turtle("turtle")
tom.penup()
tom.goto(-400,50)
tom.color(colors[2])

terry = Turtle("turtle")
terry.penup()
terry.goto(-400,0)
terry.color(colors[3])

tendai = Turtle("turtle")
tendai.penup()
tendai.goto(-400,-50)
tendai.color(colors[4])

trossard = Turtle("turtle")
trossard.penup()
trossard.goto(-400,-100)
trossard.color(colors[5])


turtle_list = [tim,tod,tom,terry,tendai,trossard] #Turtle list is a game feature that's meant for the loop.

def forward_speed():
    """ This function returns a random value for forward movement of the turtle."""
    return random.randint(0,15)

Race_on = True
while Race_on:
    for turtle in turtle_list:
        turtle.forward(forward_speed())
        if turtle.xcor() >= 400:
            Race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! The {winning_turtle} won the race")
            else:
                print(f"You've lost! The {winning_turtle} won the race")


screen.exitonclick() #Screen exit on click should be placed at the very end of the code.

#Revisions:
#1. The code is repetitive.
#2. The assignment of y values is hardcoded hence cannot be altered in the future. A list of values would be better.
#3. The assignment of colours is also hard coded. Requires complex looping knowledge.
#4. The code does not have a system to check for input errors of the user.
#5. The set coordinates cut the turtle in half at the beginning and end of the screen. The turtle width is 20.

#Appreciations:
#It works.