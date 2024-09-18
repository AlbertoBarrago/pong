""" ball class """
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.goto(0, 0)
        self.speed('fastest')
        self.dx = 3
        self.dy = 3
        self.move_speed = 0.1
        self.move_speed_increase = 0.0001
        self.move_speed_decrease = 0.0001

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.dy *= -1
        self.move_speed += self.move_speed_increase

    def bounce_x(self):
        self.dx *= -1
        self.move_speed += self.move_speed_increase

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.move_speed_increase = 0.5
        self.move_speed_decrease = 0.1
        self.bounce_x()
