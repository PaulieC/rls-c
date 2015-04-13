__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
import bjsonrpc
from ServerPackage.TournamentService import *
from ServerPackage.server_ipsearch import *


class TournamentServer():
    """
    TODO
    """
    # TODO needs details

    def __init__(self):
        """
        :return:
        """
        self.host = None
        self.port = None
        self.tournament_server = None
        self.toolbox = NetworkToolbox()

    def create_server(self):
        if self.host is None or self.port is None:
            print "HOST AND/OR PORT HASN'T BEEN SET YET!"
        else:
            self.tournament_server = bjsonrpc.createserver(host=self.host,
                                                           port=self.port,
                                                           handler_factory=TournamentService)

    def generate_ip(self):
        self.host = self.toolbox.get_host()
        print self.host

    def get_ip(self):
        if self.host is None:
            result = "No ip set at this time"
            return result
        else:
            return self.host

    def set_ip(self, new_ip):
        self.host = new_ip

    def set_port(self, new_port):
        self.port = new_port

    def get_port(self):
        if self.port is None:
            result = "No port set at this time"
            return result
        else:
            return self.port

    def open_connection(self):
        """
        :return:
        """
        self.tournament_server.debug_socket(True)
        self.tournament_server.serve()
        msg = "The Server has started running..."
        return msg

    def close_connection(self):
        self.tournament_server.stop()
        msg = "The Server has stopped running..."
        return msg