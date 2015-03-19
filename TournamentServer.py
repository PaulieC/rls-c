__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
import bjsonrpc
from bjsonrpc.handlers import BaseHandler
from TournamentService import *


class ServerObject(BaseHandler):
    """
    TODO
    """
    server = object
    service = object

    def __init__(self):
        """
        :return:
        """
        self.server = bjsonrpc.createserver()
        self.service = TournamentService()

    def run(self):
        """
        :return:
        """
        self.server.debug_socket(True)
        self.server.serve()

    def hello(self, txt):
        """
        :param txt:
        :return:
        """
        response = "hello, %s!." % txt
        print "*", response
        return response