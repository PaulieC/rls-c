__author__ = 'Joe Kvedaras and Collin Day'
#purpose of this file is to register a player in a tournament


class Registration:

    def __init__(self,tournament):
        """Initialize Registration with a Tournament"""
        self.tournament = tournament


    def register(self, player):
        """Register a player in the tournament"""
        self.tournament.add(player)
