"""
An advanced client class to allow the GameController to handle the server in ways that a
regular client cannot.
"""
__author__ = 'paulie'

from ClientPackage.PlayerClient import *
from ClientPackage.BEPCPlayer import *
import os


class GameMasterClient(PlayerClient):
    def __init__(self, player):
        PlayerClient.__init__(self, player)

    def set_number_of_players(self, max_players):
        req_set_num_players = self.player_connect.method.set_num_players(max_players)
        print "set_number_of_players::> " + req_set_num_players()

    def list_available_tournaments(self):
        os.chdir("..")
        os.chdir(os.curdir + "/AvailableTournaments")
        tournament_dir = os.path.abspath(os.curdir) + "/"
        list = self.list_files(tournament_dir)
        self.print_list(list)


    def list_available_games(self):
        os.chdir("..")
        os.chdir(os.curdir + "/AvailableGames")
        game_dir = os.path.abspath(os.curdir) + "/"
        list = self.list_files(game_dir)
        self.print_list(list)

    def print_list(self, list):
        for name in list:
            print name

    def list_files(self, path):
        """
        Web: http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
        Username: Apogentus
        :param path:
        :return:
        """
        # returns a list of names (with extension, without full path) of all files
        # in folder path
        files = []
        for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)):
                if name != "__init__.py" and name.endswith(".py"):
                    files.append(name)
        return files

obj = GameMasterClient(BEPCPlayer())
obj.list_available_tournaments()
obj.list_available_games()