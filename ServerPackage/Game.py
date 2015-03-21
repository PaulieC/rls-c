__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Matt Martorana, Justin Read"]

# imports
from ServerPackage import Observer


class Game(Observer.Observer):

    @staticmethod
    def num_players_per_game():
        """
        Number of players in a game. Default setting is two-player games
        :return: the number of players this game will support
        :rtype: int
        """
        return 2

    def get_result(self, moves):
        """
        Computes the result for the given moves.
        child of this class will have to figure out how win/loss/tie
        is determined moves
        Don't forget an elimination process if move is illegal
        :param moves: A list containing the moves made by the players
        :type moves: list
        :return: a list containing the result for the players
        """
        pass

    def is_legal(self, move):
        """
        Checks if a given move is legal
        :param move: given move
        :type move: int
        :return: True if the move is legal, false otherwise
        :rtype: bool
        """
        pass

