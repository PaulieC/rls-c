__author__ = "Paul Council, Anand Patel"
__version__ = "sprint2"

# imports
from bjsonrpc.handlers import BaseHandler


class PlayerService(BaseHandler):
    """
    This class is currently unused, but may be used in the future.
    """
    # TODO fill information

    def get_name(self, current_player):
        result = current_player.get_name()
        return result

    def set_player_id(self, current_player, id_num):
        current_player.set_id(id_num)

    def get_player_id(self, current_player):
        # result = current_player.get_player_id()
        # return result
        result = current_player.get_name()
        return result