__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["jeffrey creighton"]


class ScorekeeperListItem:
    """
    Purpose: data structure for tracking tournament leaders
    """

    def __init__(self):
        self.wins = 0
        self.losses = 0

    def win(self):
        """ Adds a win to the record """
        self.wins += 1

    def lose(self):
        """ Adds a loss to the record"""
        self.losses += 1

    # Getters

    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def get_scores(self):
        return self.wins, self.losses