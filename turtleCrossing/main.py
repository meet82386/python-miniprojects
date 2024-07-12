import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

tim = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.onkeypress(tim.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collisions with cars
    for car in car_manager.all_cars:
        if tim.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect level up
    if tim.is_lvl_completed():
        scoreboard.increment_level()
        car_manager.increment_speed()
        tim.reset_tim()

screen.exitonclick()
