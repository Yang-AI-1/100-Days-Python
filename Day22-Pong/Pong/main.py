from turtle import Turtle,Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Arcade")
screen.tracer(0)

paddle_right = Paddle("right")
paddle_left = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_right.move_up,"Up") #When a function is used as a parameter don't use brackets.
screen.onkeypress(paddle_right.move_down,"Down")
screen.onkeypress(paddle_left.move_up,"w")
screen.onkeypress(paddle_left.move_down,"s")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.speed)
    ball.move()

    #Collision detection with upper and lower wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision detection with paddles.
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Collision detection with right wall. left wins
    if ball.xcor() > 380:
        ball.resetposition()
        scoreboard.increase_left_score()

    #Collision detection with left wall. Right wins.
    if ball.xcor() < -380:
        ball.resetposition()
        scoreboard.increase_right_score()


screen.exitonclick()