""" Pong game """

from turtle import Screen

from ball import Ball
from paddle import Paddle
import time

SCREEN = Screen()
SCREEN.bgcolor('black')
SCREEN.setup(width=800, height=600)
SCREEN.title('Pong')
SCREEN.tracer(0)
GAME_IS_ON = True

# Create paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# Set up controls
SCREEN.listen()
right_paddle.setup_controls(SCREEN, "Up", "Down")
left_paddle.setup_controls(SCREEN, "w", "s")

# Create ball
ball = Ball()

while GAME_IS_ON:
    time.sleep(ball.move_speed)
    SCREEN.update()
    ball.move()

    # Check for collisions with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check for collisions with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Check if ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        GAME_IS_ON = False
    if ball.xcor() < -380:
        ball.reset_position()
        GAME_IS_ON = False

SCREEN.exitonclick()

