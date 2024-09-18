""" Pong Game """
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score


class PongGame:
    """
    Pong Game class
    - Initialize the game
    - Set up the game
    - Run the game
    - Check for collisions
    - Check for game over
    - Reset the game
    """
    def __init__(self, game_is_on):
        self.screen = Screen()
        self.screen.bgcolor('black')
        self.screen.setup(width=800, height=600)
        self.screen.title('Pong')
        self.screen.tracer(0)
        self.game_is_on = game_is_on
        self.right_paddle = Paddle((350, 0))
        self.left_paddle = Paddle((-350, 0))
        self.ball = Ball()
        self.score = Score()

    def setup_game(self):
        """
        Set up the game by setting up the screen, paddles, and ball.
        :return:
        """
        # Set up controls
        self.screen.listen()
        self.right_paddle.setup_controls(self.screen, "Up", "Down")
        self.left_paddle.setup_controls(self.screen, "w", "s")

    def game_loop(self):
        """
        Run the game loop.
        :return:
        """
        # Main game loop
        while self.game_is_on:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()
            self.handle_collisions()

    def handle_collisions(self):
        """
        Handle collisions between the ball and the paddles.
        Also check for collisions with the top and bottom walls.
        :return:
        """
        # Check for collisions with top and bottom walls
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.ball.bounce_y()

        if (self.ball.distance(self.right_paddle) < 50 and
                320 < self.ball.xcor() < 350):
            self.ball.bounce_x()
            self.score.right_point()
            self.ball.move_speed += self.ball.move_speed_increase
            #print(f"Hit right paddle: ball position ({self.ball.xcor()}, {self.ball.ycor()})")


        elif (self.ball.distance(self.left_paddle) < 50 and
              -320 > self.ball.xcor() > -350):
            self.ball.bounce_x()
            self.score.left_point()
            self.ball.move_speed += self.ball.move_speed_increase
            #print(f"Hit left paddle: ball position ({self.ball.xcor()}, {self.ball.ycor()})")

        # Check for collisions with left and right walls
        if self.ball.xcor() > 380:
            self.ball.reset_position()
            self.score.left_point()
        elif self.ball.xcor() < -380:
            self.ball.reset_position()
            self.score.right_point()

        # Check if a player has reached the winning score
        if self.score.left_score >= 10 or self.score.right_score >= 10:
            self.score.print_winner()
            self.game_is_on = False

    def end_game(self):
        """
        End the game and print the winner.
        :return:
        """
        self.score.print_winner()
        self.screen.exitonclick()

    def check_game_over(self):
        """
        Check if the game is over.
        :return:
        """
        return not self.game_is_on

    def run(self):
        """
        Run the game.
        :return:
        """
        # Run the game
        self.setup_game()
        while not self.check_game_over():
            self.game_loop()
        self.end_game()
