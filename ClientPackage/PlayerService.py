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

    def get_player(self, remote_object):
        return remote_object.get_id()