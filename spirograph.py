import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

tim.speed(0)
turtle.colormode(255)
def random_colours():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r, g, b)
    return random_colour

for i in range(103):
    tim.pencolor(random_colours())
    tim.circle(100)
    tim.right(7)






screen = Screen()

screen.exitonclick()