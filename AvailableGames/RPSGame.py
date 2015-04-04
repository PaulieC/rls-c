__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Greg Richards"]

# imports
from ServerPackage import Game


class RPSGame(Game.Game):
    """ this class simulates two players playing a game of rock, paper, scissors """

    def __init__(self):
        super(RPSGame, self).__init__()

    def get_result(self, moves):
        """
        unpack the tuple that was passed as a parameter
        :param moves: the tuple of moves that were played between the two players
        :type moves: tuple
        :return result: the tuple of moves that were played if they were legal
        :rtype: tuple
        """
        move1, move2 = moves
        x = self.is_legal(move1)
        y = self.is_legal(move2)

        if x and y:
            if move1 == move2:
                result = (0, 0)
            elif (move1 == 0 and move2 != 1) \
                    or (move1 == 1 and move2 != 2) \
                    or (move1 == 2 and move2 != 0):
                # result is tuple with points each player has earned respectively
                result = (1, 0)
            else:
                result = (0, 1)
        elif x and not y:
            result = (1, 0)
        elif not x and y:
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
