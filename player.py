from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280


class Player(Turtle):
        def __init__(self):
            super().__init__()
            self.hideturtle()
            self.speed(0)
            self.shape("turtle")
            self.penup()
            self.goto(STARTING_POSITION)
            self.setheading(90)
            self.color("green")
            self.showturtle()
            self.move_distance = 10

        def go_up(self):
                self.forward(self.move_distance)

        def is_at_finish_line(self):
            if self.ycor() > FINISH_LINE_Y:
                return True
            else:
                return False
        
        def return_to_start(self):
             self.goto(STARTING_POSITION)

        def player_pause(self):
             self.move_distance = 0

        def player_unpause(self):
             self.move_distance = 10


 
      
