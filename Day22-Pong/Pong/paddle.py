#TODO.Create a class that created paddles on the screen.
from turtle import Turtle,Screen
MOVEMENT_PACE = 20
XCOR_RIGHT = 350
XCOR_LEFT = -350
YCOR = 0

class Paddle(Turtle):
    def __init__(self,direction):
        super().__init__()
        self.create_paddle(direction)

    def create_paddle(self,direction):
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        if direction == "right":
            self.goto(x=XCOR_RIGHT, y=YCOR)
        elif direction == "left":
            self.goto(x=XCOR_LEFT,y=YCOR)
        else:
            screen = Screen()
            new_xcor = int(screen.textinput("Co-ordinate", "Write your desired x-co-ordinate"))
            new_ycor = int(screen.textinput("Co-ordinate", "Write your desired y-co-ordinate"))
            self.goto(new_xcor,new_ycor)


    def move_up(self):
        """Moves the paddle upwards."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        """Moves the paddle downwards."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)