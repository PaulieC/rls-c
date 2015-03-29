__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Joe Kvedaras, Collin Day"]

# imports
from bjsonrpc.handlers import BaseHandler
from ServerPackage.AllPlayAll import *
from ServerPackage.RPSGame import *
import time


class TournamentService(BaseHandler):
    """
    Supports the connection of players to the tournament.
    This class holds the functions required for the tournament
    to start, run, and end successfully.

    Attributes:
        game: the game corresponding to this tournament
        tournament: the tournament associated with this class
    """
    tournament = AllPlayAll()
    game = RPSGame
    id_counter = -1

    def welcome_player(self, txt):
        """
        :param txt:
        :return:
        """
        response = "Hello %s! " \
                   "\nYou have connected to the registration queue." \
                   "\nPlease standby for registration confirmation..." % txt
        print "SERVER_SIDE::>" + response     # prints information server side
        return response     # sends information to the client to handle

    def register_player(self, player):
        """
        register a player in the current tournament
        :param player: the player object to register to this tournament
        :type player: Player.Player
        """
        # convert from unicode to string
        player_name = str(player.connection.call.get_name())
        if self.tournament is None:
            msg = "Can not add player. Tournament is null"
            print "SERVER_SIDE::> " + msg
            return msg
        else:
            player.connection.call.set_player_id(self.new_id())
            # convert from unicode to string
            player_id = str(player.connection.call.get_player_id())
            print "SERVER_SIDE::> " + player_id
            self.tournament.register_player(player_id)
            result = "Attempted to register " + player_name + "..."
            print "SERVER_SIDE::> " + result
            return result

    def register_players(self, player_list):
        """
        Registers the Player objects that exist in the player_list
        :param player_list: the collected list of players to register
        :type player_list: list
        """
        for plr in player_list:
            self.register_player(plr)

    def verify_registration(self, player):
        """
        :param player:
        :type player: Player.Player
        :return:
        """
        # convert from unicode to string
        player_id = str(player.connection.call.get_player_id())
        # convert from unicode to string
        player_name = str(player.connection.call.get_name())
        registered_players = self.tournament.get_players()
        if player_id in registered_players:
            result = "Player \'" + player_name + "\' has been registered"
            print "SERVER_SIDE::>" + result
            return result
        else:
            result = player_name + " isn't in the registered list. Current registered player ids: "
            result += "[" + ", ".join(self.tournament.get_players()) + "]"
            print "SERVER_SIDE::>" + result
            return result

    def new_id(self):
        """
        :return:
        """
        self.id_counter += 1
        return self.id_counter

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