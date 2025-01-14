from turtle import Turtle

FONT = ("Courier", 24, "normal")
header_left = (-280,250)
header_center = (0,0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_value = 0
        self.penup()
        self.hideturtle()
        self.goto(header_left)
        self.write(f'Score:{self.score_value}',move=False, align='left', font=FONT)
    
    def update_score(self):
        self.clear()
        self.score_value +=1
        self.write(f'Score:{self.score_value}',move=False, align='left', font=FONT)

class Centerline(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(header_center)

    def display(self, text):
        self.write(text,move=False, align='center', font=FONT)


