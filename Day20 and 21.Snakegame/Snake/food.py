from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self): #This file gets called.
        super().__init__()  #This initializes all the attributes and methods of turtle class to this food class.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)