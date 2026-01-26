import time
from turtle import Screen
from player import Player,STARTING_POSITION,FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up,"Up") #Functions passed in as arguments are not bracketed.
screen.onkeypress(player.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #Creating many cars and moving them
    car_manager.create_car()
    car_manager.move_cars() #Loops through the all cars list and moves them all by the movement pace.

    #Car collision detection.
    for car in car_manager.all_cars: #Basically loops over every car object in the all cars list and detects if the distance between the player and the car is less than 20.
        if car.distance(player) < 20: #The computer will already have looped and caught up to the player. Don't worry about long object list loops.
            game_is_on = False
            scoreboard.game_over()

    #Finishline detection and score updating.
    if player.ycor() > FINISH_LINE_Y:
        player.goto(STARTING_POSITION)
        scoreboard.update_scoreboard()
        car_manager.level_up()

screen.exitonclick()
