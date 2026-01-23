from turtle import Turtle
from food import Food
FONT = ("Times New Roman",16,"normal")  #These are global constants to prevent hardcoding.
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"score: {self.score}", False, ALIGNMENT, FONT)


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER. SCORE: {self.score}", False, ALIGNMENT, FONT)



