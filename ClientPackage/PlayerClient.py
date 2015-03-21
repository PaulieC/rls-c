__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
import bjsonrpc

from ClientPackage import Player
from ServerPackage.TournamentService import *


class PlayerClient():
    """
    blah
    """

    player_connect = object
    player = object
    player_name = ""

    def __init__(self, player):
        """
        :param player: The player associated with this client object
        :type player: Player.Player
        :return:
        """
        self.player = player
        self.player_name = self.player.get_name()

    def client_connect(self):
        """
        :return:
        """
        self.player_connect = bjsonrpc.connect(handler_factory=TournamentService)

    def verify_connection(self):
        """
        :return:
        """
        print "::>", self.player_connect.call.welcome_player(self.player_name)

    def close_connection(self):
        """
        :return:
        """
        # TODO
        # self.player_connect.stop()
        pass

    def register_player(self, player):
        """
        :param player:
        :return:
        """
        print "::>", self.player_connect.method.register_player(player)

    def check_registration(self, player):
        """
        :param player:
        :return:
        """
        print "::>", self.player_connect.call.verify_registration(player)