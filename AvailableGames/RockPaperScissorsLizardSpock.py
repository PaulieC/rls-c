#TODO Test!!!!


__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"

# imports
from ServerPackage import Game


class RockPaperScissorsLizardSpock(Game.Game):
    """ this class simulates two players playing a game of rock, paper, scissors, lizard, spock """

    def __init__(self):
        super(RockPaperScissorsLizardSpock, self).__init__()
        self.name = "Rock-Paper-Scissors-Lizard-Spock"

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
            if player_one_move == player_two_move:
                result = (0, 0)
            elif (player_one_move == "spock" and (player_two_move == "scissors" or player_two_move == "rock")) \
                    or (player_one_move == "scissors" and (player_two_move == "paper" or player_two_move == "lizard")) \
                    or (player_one_move == "paper" and (player_two_move == "rock" or player_two_move == "spock")) \
                    or (player_one_move == "rock" and (player_two_move == "scissors" or player_two_move == "lizard")) \
                    or (player_one_move == "lizard" and (player_two_move == "spock" or player_two_move == "paper")):
                # result is tuple with points each player has earned respectively
                result = (1, 0)
            else:
                result = (0, 1)
        elif move_one_legal and not move_two_legal:
            result = (1, 0)
        elif not move_one_legal and move_two_legal:
            result = (0, 1)
        else:
            result = (0, 0)
        return result

    def is_legal(self, move):
        """
        Checks if the move provided is within the legal list
        :param move: the tuple of moves that were played
        :type move: tuple
        :return: the result of checking if the moves are legal
        :rtype: bool
        """
        return isinstance(move, str) and (move.lower() in ("rock", "paper", "scissors", "lizard", "spock"))

#TODO replace strings with 0-4??