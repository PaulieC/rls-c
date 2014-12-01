__author__ = "Joe Kvedaras and Collin Day"
#Set up a tournament with a game and register players
from AllPlayAll import *

class TournamentService:

    def __init__(self):
        #Is tournament service the one to create a new tournament?
        self.tournament = AllPlayAll()
        self.game = None

    def register_player(self, player):
        """register a player in the current tournament"""
        if self.tournament is None:
            print("Can not add player. Tournament is null")
        else:
            self.tournament.register_player(player)

    def set_game(self, game):
        """set the game of the current tournament"""
        #Tournament initializes with a game and you can not change
        #game type afterwards
        self.game = game

    def set_tournament(self, tournament):
        """Allow client to set the tournament type. Defaults to
        AllPlayAll tournament type"""
        self.tournament = tournament

    def set_display(self, display):
        if self.tournament is None:
            print("Tournament is null")
        else:
            self.tournament.attach_display(display)

    def run(self):
        """Set the game and run the tournament"""
        if self.tournament is None:
            print("Can not run tournament. Tournament is null")
        else:
            self.tournament.set_game(self.game)
            self.tournament.run()


