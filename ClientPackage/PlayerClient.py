__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
import bjsonrpc
from ClientPackage.PlayerService import *
import os


class PlayerClient():
    """
    TODO
    """
    # TODO needs details

    def __init__(self, player):
        """
        :param player: The player associated with this client object
        :type player: Player.Player
        :return:
        """
        self.player = player
        self.player_name = self.player.get_name()
        self.player_connect = None

    def client_connect(self, host, port=12345, handler=PlayerService):
        """
        :param host:
        :param port:
        :param handler:
        :return:
        """
        try:
            self.player_connect = bjsonrpc.connect(host=host, port=port, handler_factory=handler)
            result = 1
            return result
        except Exception:
            result = 0
            return result

    def verify_connection(self):
        """
        :return:
        """
        result = 0
        req_welcome_player = self.player_connect.method.verify_connection(self.player_name)
        if "Hello" in req_welcome_player():
            result = 1
        return result

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

    def list_available_players(self):
        """
        Lists the games that are available in the AvailableGames directory.
        This is printed to the console.
        :return:
        """
        player_dir = self.get_dir("AvailablePlayers")
        player_list = self.list_files(player_dir)
        return player_list

    def close_connection(self):
        """
        :return:
        """
        self.player_connect.close()

    def check_if_registration_is_open(self):
        """
        Prints to this player the current status of the tournament's registration
        """
        req_registration_status = self.player_connect.method.get_registration_status()
        if req_registration_status():
            msg = "Open"
            print "check_if_registration_is_open::> " + msg
            return msg
        else:
            msg = "Closed"
            print "check_if_registration_is_open::> " + msg
            return msg

    def register_player(self):
        """
        :param player:
        :return:
        """
        result = 0
        try:
            req_request_id = self.player_connect.method.request_id()
            id_num = req_request_id()
            self.player.set_id(id_num)
            if self.player.get_id_num() == id_num:
                try:
                    req_register_player_id = self.player_connect.method.register_player(self.player.get_player_id())
                    my_id = req_register_player_id()
                    print "register_player::> " + my_id
                    result = 1
                except Exception:
                    pass
        except Exception:
            pass
        return result

    def verify_registration(self):
        """
        :param player:
        :return:
        """
        result = 0
        try:
            req_verify_reg = self.player_connect.method.verify_registration(self.player.get_player_id())
            print "verify_registration::> " + req_verify_reg()
            return result
        except Exception:
            return result

    def get_current_game(self):
        try:
            req_curr_game = self.player_connect.method.get_game()
            game_name = req_curr_game()
            if game_name is not "":
                return game_name
            else:
                return "Unknown"
        except Exception:
            pass

    def get_current_tournament(self):
        try:
            req_curr_tour = self.player_connect.method.get_tournament()
            tour_name = req_curr_tour()
            if tour_name is not "":
                return tour_name
            else:
                return "Unknown"
        except Exception:
            pass

    def set_name(self, new_name):
        # This should stop the name from being changed if the player has been registered
        if self.player.get_player_id() is None:
            self.player.set_name(new_name)
        return self.player.get_name()

    def set_player_ready(self):
        result = "Not registered in a tournament!"
        if self.player.get_player_id() is not None:
            self.player.set_ready()
            result = "Ready!"
        else:
            pass
        return result