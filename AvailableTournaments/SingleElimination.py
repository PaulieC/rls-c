__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["William Ezekiel"]

# imports
from ServerPackage.Tournament import *
import random


class SingleElimination(Tournament):
    """
    SingleElimination Tournament Type:
    Every player plays an initial match, but only winners move on.
    In this game mode the number of rounds per match is defaulted to 3
    """

    #TODO: Implement a losers bracket.
    #TODO: Update to work with more than just 2^n players.

    def __init__(self):
        """
        Initialize SingleElimination
        :param rounds: the number of rounds per match, 3 by default
        :type rounds: list
        """
        Tournament.__init__(self)
        # variables to help us pick players 1 and 2.
        self.player_one = 0     # player 1 index
        self.player_two = 1     # player 2 index
        self.rounds = 3
        #self.playerList = random.shuffle(self.get_players())
        #self.nextSet = [] * len(self.playerList)
        self.name = "Single Elimination"

    def create_next_match(self):
        """
        Create the next match
        :return match: The new match
        :rtype: tuple
        """
        if self.player_two >= len(self.playerList):     # adds odd player to the nextset and begins
            self.nextSet.append(self.player_one)  # might need to be self.playerList[len(self.playerList)-1]
            self.start_next_set()
        match = ((self.playerList[self.player_one], self.playerList[self.player_two]), self.rounds)
        self.player_two += 2
        self.player_one += 2
        return match

    def run(self):
        """
        Run the tournament
        """
        self.begin_tournament()
        while True:
            match = self.create_next_match()
            if match is None: #TODO this is where the final player in self.nextSet is declared the winner.
                break
            self.play_match(match)
        self.end_tournament()

    def start_next_set(self):
        """
        Updates all the fields to start the next "layer" of the tournament
        :return:
        """
        self.player_one = 0     # player 1 index
        self.player_two = 1     # player 2 index
        self.playerList = random.shuffle(self.nextSet)
        self.nextSet = [0] * len(self.playerList)

    def play_match(self, match):
        """
        Play the next match and return the results
        :param match: the information for the current match
        :type match: tuple
        """
        players = match[0]
        self.start_match(players)
        result = self.play_rounds(match)    # play_rounds should return a value, but doesn't... TODO??
        
        #THIS IS ASSUMING THAT RESULT IS A PLAYER, OTHERWISE THIS WON'T WORK TODO??
        
        self.nextSet.append(self, result)
        self.end_match(players, result)