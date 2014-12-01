__author__ = "Paul Council & William Ezekiel"
__date__ = "November 24 2014"
__version__ = "1.0.1"

#imports
import Tournament

""" AllPlayAll Tournament Type, every player is in a match with every other player """
class AllPlayAll(Tournament.Tournament):
    
    def __init__(self,rounds = 5):
        """ Initialize AllPlayAll
        :param rounds the number of rounds per match, 100 by default
        """
        Tournament.Tournament.__init__(self)
        # variables to help us pick players 1 and 2.
        self.p = 0     # player 1 index
        self.q = 1     # player 2 index
        self.rounds = rounds

    def create_next_match(self):
        """ Create the next match """
        self.playerList = self.get_players()
        if self.q >= len(self.playerList):   # Gone through all possible matchups.
            return None
        match = ((self.playerList[self.p],self.playerList[self.q]), self.rounds)
        self.q = self.q+1
        if self.q >= len(self.playerList):    # if index out of bounds
            self.p = self.p+1
            self.q = self.p+1
        return match
