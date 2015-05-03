__author__ = "Paul Council, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Greg Richards"]

# imports
from ServerPackage import Game


class RockPaperScissors(Game.Game):
    """ this class simulates two players playing a game of rock, paper, scissors """

    def __init__(self):
        super(RockPaperScissors, self).__init__()
        self.name = "Rock-Paper-Scissors"

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

        if move_one_legal and move_two_legal:
            if player_one_move == player_two_move:
                result = (0, 0)
            elif (player_one_move == 0 and player_two_move != 1) \
                    or (player_one_move == 1 and player_two_move != 2) \
                    or (player_one_move == 2 and player_two_move != 0):
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
        return isinstance(move, int) and (move in (0, 1, 2))
