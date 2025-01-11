import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic updates

# Create a player object
player = Player()
screen.listen()
screen.onkeypress(player.go_up,"w")

#create car objects
car_manager = CarManager()


# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False

screen.exitonclick()

