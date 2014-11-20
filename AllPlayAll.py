__author__ = "Paul Council & William Ezekiel"
__date__ = "November 19 2014"
__version__ = "1.0"

from Game import *
from Registration import *
""" AllPlayAll Tournament Type, every player plays every other player in
    1 match"""
class AllPlayAll(Tournament):
    def __init__(self,game,registration,rounds=1000):
        """ Initialize AllPlayAll class. Requires Game, Registration
            and Rounds. Rounds is optional and will be 1000 by default.
        """
        if(rounds>0):
            self.rounds = rounds
        else:
            self.rounds = 1000
        self.game = game
        self.registration = registration


    def set_players(self):
        """ Place all active players into tournament bracket."""
        self.bracket = self.registration.get_players()

    def create_next_match(self,i,j):
        """Create a match consisting of two players. Players
            are determined by positions i and j in bracket"""
        #i == j will never happen
        return [bracket[i],bracket[j]]

    def play_match(self,match):
        """ play match: play a game a certain number of rounds"""
        self.game.connect()
        for i in range(0,rounds):
            self.game.play(match[0],match[1])
            # assuming games updates scoreboard on winner. 
        
        
    
    def run(self):
        """ Run the All-Play-All Tournament.
            Each player plays all other players in one match.
        """
        for i in range(0,len(self.bracket)): 
            for j in range(i+1,len(self.bracket)):
                match = create_next_match(i,j)
                play_match(match)
                
