from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

print(user_bet)

for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.pu()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(-230, y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)

'''''

tim = Turtle("turtle")
tim.color(color[0])
tim.pu()
tim.goto(-230, -125)

tom = Turtle("turtle")
tom.color(color[1])
tom.pu()
tom.goto(-230, -75)

tam = Turtle("turtle")
tam.color(color[2])
tam.pu()
tam.goto(-230, -25)

bill = Turtle("turtle")
bill.color(color[3])
bill.pu()
bill.goto(-230, 25)

bob = Turtle("turtle")
bob.color(color[4])
bob.pu()
bob.goto(-230, 75)

joe = Turtle("turtle")
joe.color(color[5])
joe.pu()
joe.goto(-230, 125)

'''''


screen.exitonclick()