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
        success = False
        if self.host is None or self.port is None:
            pass
        else:
            try:
                self.tournament_server = bjsonrpc.createserver(host=self.host,
                                                               port=self.port,
                                                               handler_factory=TournamentService)
                success = True
            except Exception:
                success = None
        return success

    def generate_ip(self):
        success = False
        try:
            self.host = self.toolbox.get_host()
            success = self.host
        except Exception:
            pass
        return success

    def get_ip(self):
        if self.host is None:
            result = "No ip set at this time"
            return result
        else:
            return self.host

    def set_ip(self, new_ip):
        self.host = new_ip
        return self.host

    def set_port(self, new_port):
        self.port = new_port
        return self.port

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
        success = False
        try:
            self.tournament_server.debug_socket(True)
            try:
                self.tournament_server.serve()
            except Exception:
                raise Exception("The connection has unwillingly stopped.")
            success = True
        except Exception:
            pass
        return success

    def close_connection(self):
        success = False
        try:
            self.tournament_server.stop()
            success = True
        except Exception:
            pass
        return success