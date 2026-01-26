import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car) #Adds all the car objects in a car list.

    def move_cars(self):
        for car in self.all_cars: #For the number of car objects inside the list the car will move.
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

#Things I learnt:
# Inheritance makes the created class a single object in contexts like these.
# Objects have their individual serial that can be stored in a list and accessed in order.
# The computer processes the tasks super-fast. Program while conscious of this.