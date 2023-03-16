import turtle as tt
import random


class Food(tt.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed(0)
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-180, 180))

    def go_to_random(self):
        self.goto(random.randint(-280, 280), random.randint(-180, 180))
