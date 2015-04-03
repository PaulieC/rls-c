__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
import bjsonrpc
from ServerPackage.TournamentService import *


class TournamentServer():
    """
    TODO
    """
    # TODO needs details

    tournament_server = object

    def __init__(self):
        """
        :return:
        """
        self.tournament_server = bjsonrpc.createserver(host="192.168.1.25",
                                                       port=12345,
                                                       handler_factory=TournamentService)

    def open_connection(self):
        """
        :return:
        """
        self.tournament_server.debug_socket(True)
        self.tournament_server.serve()