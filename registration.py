__author__ = 'joe kvedaras'
#purpose of this file is to register a player in a tournament


class Registration:
    """Register a player in the tournament"""

    def __init__(self,Tournament):
        self.tournament = Tournament


    def register(self, Player):
        """Register a player in the tournament passed into constructor"""
        self.tournament.add(Player)
