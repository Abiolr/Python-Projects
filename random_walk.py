import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("circle")
tim.color("blue")
tim.width("15")
tim.speed(0)
turtle.colormode(255)

def random_colours():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

while 1==1:
    tim.pencolor(random_colours())
    #tim.pencolor(random.choice(["red", "orange", "green", "blue", "purple", "brown", "teal", "midnight blue", "maroon", "gold"]))
    tim.fd(random.choice([50,-50]))
    tim.right(random.choice([-90,0,90]))

screen = Screen()
screen.exitonclick()