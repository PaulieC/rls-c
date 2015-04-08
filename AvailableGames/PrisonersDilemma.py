#TODO Deal with pass/illegal moves.

__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"

# imports
from ServerPackage import Game


class PrisonersDilemma(Game.Game):
    """
     This game simulates Prisoner's Dilema. Result will return the number of years in jail for each player respectively
    """

    def __init__(self):
        super(PrisonersDilemma, self).__init__()

    def get_result(self, moves):
        """
        unpack the tuple that was passed as a parameter
        :param moves: the tuple of moves that were played between the two players
        :type moves: tuple
        :return result: the tuple of moves that were played if they were legal
        :rtype: tuple
        """
        player_one_move, player_two_move = moves
        move_one_legal = self.is_legal(player_one_move)
        move_two_legal = self.is_legal(player_two_move)
        player_two_move = player_two_move.lower()
        player_one_move = player_one_move.lower()

        if move_one_legal and move_two_legal:
            if player_one_move == "confess" and player_two_move == "confess":
                result = (5, 5)
            elif player_one_move == "confess" and player_two_move == "silent":
                result = (0, 20)
            elif player_one_move == "silent" and player_two_move == "confess":
                result = (20, 0)
            else:
                result = (1, 1)
        elif move_one_legal and not move_two_legal:
            pass
        elif not move_one_legal and move_two_legal:
            pass
        else:
            pass
        return result

    def is_legal(self, move):
        """
        Checks if the move provided is within the legal list
        :param move: the tuple of moves that were played
        :type move: tuple
        :return: the result of checking if the moves are legal
        :rtype: bool
        """
        return isinstance(move, str) and (move.lower() in ("confess", "silent"))

#TODO replace strings with 0-4??