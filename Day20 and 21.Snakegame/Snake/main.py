from turtle import Screen

from Snake.scoreboard import Scoreboard
from snake import Snake
import time
from food import Food

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake() #The snake has been created. The created snake is an initialised attribute
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()#This makes the screen update after all the 3 segments have been moved.
    time.sleep(0.1) #Adds a certain amount of delay to the movement of the snake
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]: #Slices the segments list from the first one to ignore the head.
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()




screen.exitonclick()