#TODO: Implement

__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["William Ezekiel"]

# imports
from ServerPackage import Tournament
import random


class DoubleElimination(Tournament.Tournament):
    """
    DoubleElimination Tournament Type:
    Every player plays in matches until they have accumulated two losses.
    In this game mode the number of rounds per match is defaulted to 3

    TODO: Implement a losers bracket.
    TODO: Update to work with more than just 2^n players.
    """