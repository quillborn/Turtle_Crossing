import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, Centerline

#setup objects and screen values
screen = Screen()
player = Player()
scoreboard = Scoreboard()
center = Centerline()
car_manager = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic updates

#setting up pause funtionality
unpaused = True
def toggle_pause():
    global unpaused
    unpaused = not unpaused
    if unpaused == False:
            player.player_pause()
            center.display("Pause")
    else:
        center.clear()
        player.player_unpause()

#set up controls
screen.listen()
screen.onkeypress(key="w",fun=player.go_up)
screen.onkeypress(key="space", fun=toggle_pause)

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #spawning in cars & applying movement
    if unpaused:
        car_manager.create_cars()
        car_manager.move_cars()

    #detecting a collision between car object and player.
    #game over
    for car in car_manager.all_cars:
        if car.distance(player) <= 20:
            game_is_on = False
            center.display("Game Over.")

    #detecting if player has reached the other side
    if player.is_at_finish_line():
        scoreboard.update_score()
        car_manager.level_up()
        player.return_to_start()
        

   

screen.exitonclick()

