__author__ = "Joe Kvedaras and Collin Day"
#Set up a tournament with a game and register players
from Tournament.py import *


class TournamentService:

    def __init__(self, tournament):
        #Is tournament service the one to create a new tournament?
        self.tournament = tournament


    def register_player(self, player):
        """register a player in the current tournament"""
        self.tournament.register_player(player)


    def set_game(self,game):
        """set the game of the current tournament"""
        #Do not know if I have to create a new tournament with the game
        #type or add the game to an existing tournament
        pass
