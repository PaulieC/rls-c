__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
from bjsonrpc.handlers import BaseHandler
from ClientPackage.BEPCPlayer import *


class PlayerService(BaseHandler):
    """
    TODO
    """
    # TODO fill information
    player = BEPCPlayer()

    def get_name(self):
        return self.player.get_name()

    def set_player_id(self, id_num):
        self.player.set_id(id_num)

    def get_player_id(self):
        return self.player.get_player_id()