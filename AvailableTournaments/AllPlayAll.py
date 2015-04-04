__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["William Ezekiel"]

# imports
from ServerPackage import Tournament


class AllPlayAll(Tournament.Tournament):
    """ AllPlayAll Tournament Type, every player is in a match with every other player """

    def __init__(self, rounds=5):
        """
        Initialize AllPlayAll
        :param rounds: the number of rounds per match, 5 by default
        :type rounds: list
        """
        Tournament.Tournament.__init__(self)
        # variables to help us pick players 1 and 2.
        self.p = 0     # player 1 index
        self.q = 1     # player 2 index
        self.rounds = rounds

    def create_next_match(self):
        """
        Create the next match
        :return match: The new match
        :rtype: tuple
        """
        self.playerList = self.get_players()
        if self.q >= len(self.playerList):   # Go through all possible matches.
            return None
        match = ((self.playerList[self.p], self.playerList[self.q]), self.rounds)
        self.q += 1
        if self.q >= len(self.playerList):    # if index out of bounds
            self.p += 1
            self.q = self.p+1
        return match