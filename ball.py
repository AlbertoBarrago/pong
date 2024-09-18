""" ball class """
from turtle import Turtle


class Ball(Turtle):
    """
    Ball class
    - Initialize the ball
    - Move the ball
    - Bounce the ball off the top or bottom wall
    - Bounce the ball off the paddles
    """
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.goto(0, 0)
        self.speed('fastest')
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.1
        self.move_speed_increase = 0.0001
        self.move_speed_decrease = 0.0001

    def move(self):
        """
        Move the ball.
        :return:
        """
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Bounce the ball off the top or bottom wall.
        :return:
        """
        self.dy *= -1
        self.move_speed += self.move_speed_increase

    def bounce_x(self):
        """
        Bounce the ball off the left or right wall.
        :return:
        """
        self.dx *= -1
        self.move_speed += self.move_speed_increase

    def reset_position(self):
        """
        Reset the ball's position and speed.
        :return:
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.move_speed_increase = 0.5
        self.move_speed_decrease = 0.1
        self.bounce_x()
