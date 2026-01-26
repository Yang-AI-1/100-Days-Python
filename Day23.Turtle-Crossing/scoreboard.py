from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.write(f"score: {self.score}", False, "left", FONT)

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", False, "left", FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER. SCORE: {self.score}", False, "center", FONT)


