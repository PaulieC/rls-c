__author__ = "Joe Kvedaras and Collin Day"
#Set up a tournament with a game and register players
from Tournament.py import *
from AllPlayAll.py import *

class TournamentService:

    def __init__(self):
        #Is tournament service the one to create a new tournament?
        self.tournament
        self.game


    def register_player(self, player):
        """register a player in the current tournament"""
        self.tournament.register_player(player)


    def set_game(self, game):
        """set the game of the current tournament"""
        #Tournament initializes with a game and you can not change
        #game type afterwards
        self.game = game

    def set_tournament(self, tournament_type = None):
        """Allow client to set the tournament type. Defaults to
        AllPlayAll tournament type"""
        if tournament_type is None:
            #AllPlayAll takes registration as a parameter. I don't think they
            #need that there
            self.tournament = AllPlayAll(self.game, None, 1000)
        else:
            self.tournament = tournament_type(self.game, None, 1000)

    def run(self):
        """Set the game and run the tournament"""
        if self.tournament is None:
            print ("Can not run tournament. Tournament is null")
        else:
            self.tournament.run()
