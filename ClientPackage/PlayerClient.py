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
        self.player_connect = bjsonrpc.connect(host="hello.com", port=00001, handler_factory=ClientService)

    def verify_connection(self):
        """
        :return:
        """
        self.client_connect()
        print "verify_connection::>", self.player_connect.call.welcome_player(self.player_name), "\n"

    def close_connection(self):
        """
        :return:
        """
        # TODO
        # self.player_connect.stop()
        self.player_connect.close()

    def register_player(self, player):
        """
        :param player:
        :return:
        """
        # print "register_player::>",
        self.client_connect()
        x = self.player_connect.call.register_player(player)
        print "hello"

    def verify_registration(self, player):
        """
        :param player:
        :return:
        """
        print "verify_registration::>", self.player_connect.call.verify_registration(player), "\n"