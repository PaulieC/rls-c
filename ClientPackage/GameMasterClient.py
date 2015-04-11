"""
An advanced client class to allow the GameController to handle the server in ways that a
regular client cannot.
"""
__author__ = 'paulie'

from ClientPackage.PlayerClient import *
from AvailableGames import *
from AvailableTournaments import *
from ClientPackage.BEPCPlayer import *
import importlib
import os


class GameMasterClient(PlayerClient):
    def __init__(self, player):
        PlayerClient.__init__(self, player)

    def set_number_of_players(self, max_players):
        req_set_num_players = self.player_connect.method.set_num_players(max_players)
        print "set_number_of_players::> " + req_set_num_players()

    def get_tournament_dir(self):
        os.chdir("..")
        os.chdir(os.curdir + "/AvailableTournaments")
        result = os.path.abspath(os.curdir) + "/"
        return result

    def get_game_dir(self):
        os.chdir("..")
        os.chdir(os.curdir + "/AvailableGames")
        result = os.path.abspath(os.curdir) + "/"
        return result

    def list_available_tournaments(self):

        tournament_dir = self.get_tournament_dir()
        list = self.list_files(tournament_dir)
        self.print_list(list)


    def list_available_games(self):
        game_dir = self.get_game_dir()
        list = self.list_files(game_dir)
        self.print_list(list)

    def list_registered_players(self):
        req_registered_players = self.player_connect.method.get_registered_players()
        players = req_registered_players()
        self.print_list(players)

    def set_tournament(self):
        # first, list all available tournaments
        self.list_available_tournaments()
        # now select the tournament to import
        tournament_list = self.list_files(self.get_tournament_dir())
        print tournament_list
        print len(tournament_list)
        while True:
            index = raw_input("tournament to select (-1 to cancel) --> ")
            if index == "-1":
                print "...nevermind then >_>"
                break
            elif index >= str(len(tournament_list)) or index < str(len(tournament_list) - 1):
                print "This value doesn't reference a possible tournament"
            else:
                tournament_package = "AvailableTournaments." + str(tournament_list[int(index)]).replace(".py", "")
                tournament_module = str(tournament_list[int(index)]).replace(".py", "")
                req_change_tournament = self.player_connect.method.set_tournament(tournament_package, tournament_module)
                print "set_tournament::>" + req_change_tournament()
                break


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

    def print_list(self, list):
        num = 0
        for name in list:
            print str(num) + ".   " + name
            num += 1


# obj = GameMasterClient(BEPCPlayer())
# obj.set_tournament()