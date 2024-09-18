""" Paddle class """
from turtle import Turtle, Screen

SCREEN = Screen()

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed('fastest')

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def setup_controls(self, screen, up_key, down_key):
        screen.onkey(self.go_up, up_key)
        screen.onkey(self.go_down, down_key)
