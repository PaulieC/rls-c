__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
import bjsonrpc


class ClientObject():
    """
    blah
    """

    player_connect = object

    def __init__(self):
        """
        :return:
        """
        self.player_connect = bjsonrpc.connect()