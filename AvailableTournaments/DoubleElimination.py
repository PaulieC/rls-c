__author__ = "Paul Council, Anand Patel"
__version__ = "sprint5"
__credits__ = ["William Ezekiel"]

# imports
from ServerPackage.Tournament import *


class DoubleElimination(Tournament):
    """
    DoubleElimination Tournament Type:
    Every player plays in matches until they have accumulated two losses.
    In this game mode the number of rounds per match is defaulted to 3
    """
    # TODO: Implement a losers bracket.
    # TODO: Update to work with more than just 2^n players.

    def __init__(self, rounds=5):
        """
        Initialize AllPlayAll
        :param rounds: the number of rounds per match, 5 by default
        :type rounds: list
        """
        Tournament.__init__(self)
        # variables to help us pick players 1 and 2.
        self.p = 0     # player 1 index
        self.q = 1     # player 2 index
        self.rounds = rounds
        self.name = "DoubleElimination"