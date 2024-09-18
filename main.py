"""
 Main entry point for the Pong game.
"""
from pong_game import PongGame


def main():
    """
    Main entry point for the Pong game.
    :return:
    """
    game = PongGame(game_is_on=True)
    game.run()


if __name__ == "__main__":
    main()
