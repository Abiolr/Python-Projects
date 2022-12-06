from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color("lime")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-260, 260, 20)
        random_y = random.randrange(-260, 260, 20)
        self.goto(random_x, random_y)