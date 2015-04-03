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
        self.player_connect = bjsonrpc.connect(host="192.168.1.26",
                                               port=12345,
                                               handler_factory=PlayerService)

    def verify_connection(self):
        """
        :return:
        """
        req_welcome_player = self.player_connect.method.verify_connection(self.player_name)
        print "verify_connection::> " + req_welcome_player()

    def close_connection(self):
        """
        :return:
        """
        self.player_connect.close()

    def register_player(self):
        """
        :param player:
        :return:
        """
        req_request_id = self.player_connect.method.request_id()
        self.player.set_id(req_request_id())
        req_register_player_id = self.player_connect.method.register_player(self.player.get_player_id())
        print "register_player::> " + req_register_player_id()

    def verify_registration(self):
        """
        :param player:
        :return:
        """
        req_verify_reg = self.player_connect.method.verify_registration(self.player.get_player_id())
        print "verify_registration::> " + req_verify_reg()