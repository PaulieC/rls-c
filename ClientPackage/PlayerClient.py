__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
import bjsonrpc
from ClientPackage.PlayerService import *


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
        self.player_connect = bjsonrpc.connect(host="150.250.191.238",
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

    def check_if_registration_is_open(self):
        """
        Prints to this player the current status of the tournament's registration
        """
        req_registration_status = self.player_connect.method.get_registration_status()
        if req_registration_status():
            print "check_if_registration_is_open::> " + "registration is open!"
        else:
            print "check_if_registration_is_open::> " + "registration is closed."

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