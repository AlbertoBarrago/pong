""" Paddle class """
from turtle import Turtle, Screen

SCREEN = Screen()

class Paddle(Turtle):
    """
    Paddle class
    - Initialize the paddle
    - Move the paddle
    - Set up the controls
    """
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed('fastest')

    def go_up(self):
        """
        Move the paddle up.
        :return:
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Move the paddle down.
        :return:
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def setup_controls(self, screen, up_key, down_key):
        """
        Set up the controls for the paddle.
        :param screen:
        :param up_key:
        :param down_key:
        :return:
        """
        screen.onkey(self.go_up, up_key)
        screen.onkey(self.go_down, down_key)
