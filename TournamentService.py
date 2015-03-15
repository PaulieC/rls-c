__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Joe Kvedaras, Collin Day"]

# imports
from AllPlayAll import *


class TournamentService:
    """
    Set up a tournament with a game and register players

        Attributes:
            game: the game corresponding to this tournament
            tournament: the tournament associated with this class
    """

    def __init__(self):
        # Is tournament service the one to create a new tournament?
        self.tournament = AllPlayAll()
        self.game = None

    def register_player(self, player):
        """
        register a player in the current tournament
        :param player: the player object to register to this tournament
        :type player: Player.Player
        """
        if self.tournament is None:
            print "Can not add player. Tournament is null"
        else:
            self.tournament.register_player(player)

    def set_game(self, game):
        """
        set the game of the current tournament
        :param game: the game to set to this tournament
        :type game: Game.Game
        """
        # Tournament initializes with a game and you can not change
        # game type afterwards
        self.game = game

    def set_tournament(self, tournament):
        """
        Allow client to set the tournament type. Defaults to
        AllPlayAll tournament type
        :param tournament: the tournament to assign to this service
        :type tournament: Tournament.Tournament
        """
        self.tournament = tournament

    def set_display(self, display):
        """
        Assigns the display solution for this service
        :param display: display to project information
        :type display: Display.Display
        """
        if self.tournament is None:
            print "Tournament is null"
        else:
            self.tournament.attach_display(display)

    def run(self):
        """Set the game and run the tournament"""
        if self.tournament is None:
            print "Can not run tournament. Tournament is null"
        else:
            self.tournament.set_game(self.game)
            self.tournament.run()