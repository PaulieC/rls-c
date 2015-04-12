"""
An advanced client class to allow the GameController to handle the server in ways that a
regular client cannot.
"""
__author__ = 'paulie'

from ClientPackage.PlayerClient import *
import os


class GameMasterClient(PlayerClient):
    def __init__(self, player):
        PlayerClient.__init__(self, player)

    def set_number_of_players(self, max_players):
        """
        Calls the function server side with the parameter to set as the maximum number of players that
        can register in the tournament.
        :param max_players: The highest amount of players
        :type: int
        """
        req_set_num_players = self.player_connect.method.set_num_players(max_players)
        print "set_number_of_players::> " + req_set_num_players()

    def get_dir(self, final_dir):
        """
        Used to find the directory of the games or the tournament. This could be used to find
        any directory in the same directory as the ClientPackage...
        :param final_dir: the name of the folder to search for
        :type: str
        :return str: The full path of the directory
        """
        os.chdir("..")
        os.chdir(os.curdir + "/" + final_dir)
        result = os.path.abspath(os.curdir) + "/"
        return result

    def list_available_tournaments(self):
        """
        Lists the tournaments that are available in the AvailableTournaments directory.
        This is printed to the console
        """
        tournament_dir = self.get_dir("AvailableTournaments")
        tournament_list = self.list_files(tournament_dir)
        self.print_list(tournament_list)


    def list_available_games(self):
        """
        Lists the games that are available in the AvailableGames directory.
        This is printed to the console.
        :return:
        """
        game_dir = self.get_dir("AvailableGames")
        game_list = self.list_files(game_dir)
        self.print_list(game_list)

    def open_tournament_registration(self):
        """
        Opens the player's ability to register to the tournament
        """
        req_open_registration = self.player_connect.method.open_tournament_registration()
        req_open_registration()

    def close_tournament_registration(self):
        """
        Closes the player's ability to register to the tournament
        """
        req_close_registration = self.player_connect.method.close_tournament_registration()
        req_close_registration()

    def list_registered_players(self):
        """
        Prints the players that have registered to the tournament
        """
        req_registered_players = self.player_connect.method.get_registered_players()
        players = req_registered_players()
        self.print_list(players)

    def set_tournament(self):
        # TODO finish implementation
        # first, list all available tournaments
        self.list_available_tournaments()
        # now select the tournament to import
        tournament_list = self.list_files(self.get_dir("AvailableTournaments"))
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

    def set_game(self):
        # TODO implement similarly to set_tournament
        pass

    def start_game(self):
        pass

    def end_game(self):
        pass

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

    def print_list(self, printable_list):
        num = 0
        for name in printable_list:
            print str(num) + ".   " + name
            num += 1


# obj = GameMasterClient(BEPCPlayer())
# obj.set_tournament()