import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.penup()




class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            color = random.choice(COLORS)
            new_car_head = car()
            new_car_tail = car()
            new_car_head.color(color)
            new_car_tail.color(color)
            random_y = random.randint(-250,250)
            new_car_head.goto(300, random_y)
            new_car_tail.goto(320, random_y)
            self.all_cars.append(new_car_head)
            self.all_cars.append(new_car_tail)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        """increases speed cars move at"""
        self.car_speed += MOVE_INCREMENT