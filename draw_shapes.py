import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
# counter = 0
# while counter < 4:
#    tim.fd(100)
#    tim.right(90)
#    counter += 1
tom.speed(0)
tom.pu()
tom.left(90)
tom.fd(200)
tom.right(90)
tom.pd()

""""
tom.pencolor('yellow')
for i in range(3):
    tom.fd(100)
    tom.right(120)
tom.pencolor('orange')
for i in range(4):
    tom.fd(100)
    tom.right(90)
tom.pencolor('pink')
for i in range(5):
    tom.fd(100)
    tom.right(72)
tom.pencolor('black')
for i in range(6):
    tom.fd(100)
    tom.right(60)
tom.pencolor('blue')
for i in range(7):
    tom.fd(100)
    tom.right(360/7)
tom.pencolor('red')
for i in range(8):
    tom.fd(100)
    tom.right(45)
tom.pencolor('green')
for i in range(9):
    tom.fd(100)
    tom.right(40)
tom.pencolor('purple')
for i in range(10):
    tom.fd(100)
    tom.right(36)
"""
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

x = 3
while x < 100:
    tom.pencolor(random_color())
    for i in range(x):
        tom.fd(100)
        tom.right(360/x)
    x += 1



screen = Screen()
screen.exitonclick()