from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLOR = "black"
SHAPE = "turtle"


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape(SHAPE)
        self.setheading(90) #Faces the turtle northwards.

    def move_up(self):
        """Moves the turtle forward."""
        self.forward(MOVE_DISTANCE)
    def move_down(self):
        """Moves the turtle downward."""
        self.backward(MOVE_DISTANCE)
