from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score}", True, 'center', ('Courier', 24, 'normal'))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", True, 'center', ('Courier', 24, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(0, 260)
        self.write(f"Score: {self.score}", True, 'center', ('Courier', 24, 'normal'))