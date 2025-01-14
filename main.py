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
print(player.xcor)

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #spawnin in cars & applying movement
    car_manager.create_cars()
    car_manager.move_cars()

    #detecting a collision between car object and player.
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False

    #detecting if player has reached the other side
    if player.is_at_finish_line():
        player.return_to_start()
        car_manager.level_up()

   

screen.exitonclick()

