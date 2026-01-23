from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] #Constants encourage maintainability.
MOVEMENT_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


def add_segment():
    new_segment = Turtle("square")


class Snake:
    def __init__(self):
        self.segments = [] #The segments of the snake are an attribute.
        self.create_snake() #Methods can be used in classes themselves.
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:  # Range functions loop through numbers. The second input is not inclusive.Can write desired number of object values.
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")  # Creating turtle objects which are square
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """ Add a new segment to the snake from the last position"""
        self.add_segment(self.segments[-1].position()) #-1 Is the last position. The other movement code has been taken care of.

    def move(self):
        """Snake moves forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):# Goes from the last segment to the first. Start,stop and step format on the range inputs.
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(new_pos)
        self.head.forward(MOVEMENT_DISTANCE) #Moves the snake forward 20 paces.constantly


    def up(self):
        """ Moves the snake up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves the snake left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moves the snake right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

