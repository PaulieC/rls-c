__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
import bjsonrpc
from ClientPackage.Player import *
from ClientPackage.PlayerService import *
from ServerPackage.TournamentService import *


class PlayerClient():
    """
    TODO
    """
    # TODO needs details

    def __init__(self, player):
        """
        :param player: The player associated with this client object
        :type player: Player.Player
        :return:
        """
        self.player = player
        self.player_name = self.player.get_name()
        self.player_connect = None

    def client_connect(self):
        """
        :return:
        """
        self.player_connect = bjsonrpc.connect(host="192.168.1.25",
                                               port=12345,
                                               handler_factory=PlayerService)

    def verify_connection(self):
        """
        :return:
        """
        print "verify_connection::>", self.player_connect.call.welcome_player(self.player_name), "\n"

    def close_connection(self):
        """
        :return:
        """
        self.player_connect.close()

    def register_player(self, player):
        """
        :param player:
        :return:
        """
        print "register_player::>", self.player_connect.call.register_player(player)

    def verify_registration(self, player):
        """
        :param player:
        :return:
        """
        print "verify_registration::>", self.player_connect.call.verify_registration(player), "\n"