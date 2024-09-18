""" score class """

from turtle import Turtle


class Score(Turtle):
    """
    Score class
    - Initialize the score
    - Update the score
    - Print the winner
    """
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        """
        Update the score.
        :return:
        """
        self.clear()
        self.goto(-100, 250)
        self.write(f"P1: {self.left_score}", align='center', font=('Courier', 20, 'normal'))
        self.goto(100, 250)
        self.write(f"P2: {self.right_score}", align='center', font=('Courier', 20, 'normal'))


    def left_point(self):
        """
        Update the score for the left player.
        :return:
        """
        self.left_score += 1
        self.update_score()

    def right_point(self):
        """
        Update the score for the right player.
        :return:
        """
        self.right_score += 1
        self.update_score()

    def reset_score(self):
        """
        Reset the score.
        :return:
        """
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def print_winner(self):
        """
        Print the winner.
        :return:
        """
        self.clear()
        self.goto(0, 0)
        if self.left_score > self.right_score:
            self.write("Player 1 wins!", align="center", font=("Courier", 36, "normal"))
        elif self.right_score > self.left_score:
            self.write("Player 2 wins!", align="center", font=("Courier", 36, "normal"))
        else:
            self.write("It's a tie!", align="center", font=("Courier", 36, "normal"))
