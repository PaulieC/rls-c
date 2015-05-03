__author__ = "Paul Council, Anand Patel"
__version__ = "sprint5"

# imports
import time
import os
import importlib
import bjsonrpc
from ClientPackage.PlayerService import *


class PlayerClient():
    """
    Handles all the request creation
    """
    def __init__(self, player):
        """
        :param player: The player associated with this client object
        :type player: Player.Player
        :return:
        """
        self.player = player
        self.player_name = self.player.get_name()
        self.player_connect = None

    def change_player(self, player_type):
        try:
            mod = importlib.import_module("AvailablePlayers." + player_type)
            my_class = getattr(mod, player_type)
            self.player = my_class()
            print "Player type is now: ", self.player.get_name()
        except Exception:
            raise Exception("The selected tournament doesn't exist in the AvailableTournaments directory.")

    def client_connect(self, host, port=12345, handler=PlayerService):
        """
        Connects to a bjsonrpc server using the given ip, and port.
        :param host: the ip address of the target server
        :param port: the port you are trying to connect with
        :param handler: the class that contains all the handler methods
        :return:
        """
        try:
            self.player_connect = bjsonrpc.connect(host=host, port=port, handler_factory=handler)
            result = 1
            return result
        except Exception:
            raise Exception('client_connect::> Unable to connect to the server.')

    def verify_connection(self):
        """
        Verifies the player connection based on whether there was a "Hello" in the req_welcome_player() response.
        :return:
        """
        try:
            msg = "Couldn't verify connection"
            req_welcome_player = self.player_connect.method.verify_connection(self.player_name)
            welcome_player = req_welcome_player()
            welcome_player = str(welcome_player)
            if "Hello" in welcome_player:
                msg = "Connection verified"
            return msg
        except Exception:
            raise Exception('verify_connection::> Unable to verify connection at this time.')

    @staticmethod
    def get_dir(final_dir):
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

    @staticmethod
    def list_files(path):
        """
        Returns a list of names (with extension, without full path) of all files in the specified folder path
        Web: http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
        Username: Apogentus
        :param path:
        :return:
        """
        files = []
        for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)):
                if name != "__init__.py" and name.endswith(".py"):
                    files.append(name)
        return files

    @staticmethod
    def print_list(printable_list):
        num = 0
        for name in printable_list:
            print str(num) + ".   " + name
            num += 1

    def list_available_players(self):
        """
        Lists the games that are available in the AvailableGames directory.
        :return player_list: the list of files in the AvailablePlayers directory
        """
        player_dir = self.get_dir("AvailablePlayers")
        player_list = self.list_files(player_dir)
        return player_list

    def close_connection(self):
        """
        Attempts to close the player's connection to the server.
        :return:
        """
        try:
            self.player_connect.close()
        except Exception:
            raise Exception("close_connection::> Couldn't close connection...")

    def check_if_registration_is_open(self):
        """
        Prints to this player the current status of the tournament's registration
        :return msg: returns open/closed based on the registration status
        """
        try:
            req_registration_status = self.player_connect.method.get_registration_status()
            if req_registration_status():
                msg = "Open"
                print "check_if_registration_is_open::> " + msg
                return msg
            else:
                msg = "Closed"
                print "check_if_registration_is_open::> " + msg
                return msg
        except Exception:
            raise Exception('check_if_registration_is_open::> unable to check if the registation is open')

    def register_player(self):
        """
        Registers the current player after checking to see if that player isn't already registered.
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
                    raise Exception("register_player::> Couldn't successfully register the player...")
        except Exception:
            raise Exception("register_player::> Couldn't successfully obtain a player number...")
        return result

    def verify_registration(self):
        """
        Attempts to verify that this player is already registered in the tournament
        :return:
        """
        try:
            req_verify_reg = self.player_connect.method.verify_registration(self.player.get_player_id())
            return req_verify_reg()
        except Exception:
            raise Exception("verify_registration::> unable to verify")

    def get_current_game(self):
        """
        Gets the current game the tournament is set to from the server.
        :return:
        """
        try:
            req_curr_game = self.player_connect.method.get_game()
            game_name = req_curr_game()
            if game_name is not "":
                return game_name
            else:
                return "No game to return to you."
        except Exception:
            raise Exception('get_current_game::> unable to get current game')

    def get_current_tournament(self):
        """
        Allows the player to get the name of the current set tournament type (All-Play-All, SingleElimination, etc.)
        :return:
        """
        try:
            req_curr_tour = self.player_connect.method.get_tournament()
            tour_name = req_curr_tour()
            if tour_name is not "":
                return tour_name
            else:
                return "Unknown"
        except Exception:
            raise Exception('get_current_tournament::> unable to get the current tournament')

    def set_name(self, new_name):
        """
        Allows a player to change their name (not their unique player ID), but only if they haven't been registered.
        :param new_name:
        :return:
        """
        try:
            if self.player.get_player_id() is None:
                self.player.set_name(new_name)
                self.player_name = new_name
            return self.player.get_name()
        except Exception:
            raise Exception('set_name::> Unable to change the name of a player that is already registered.')

    def submit_move(self):
        """
        Allows the player object to generate the next move and send this server side for
        the current round.
        """
        try:
            move = self.player.play()
            req_set_move = self.player_connect.method.set_player_move(self.player.get_player_id(), move)
            set_move = req_set_move()
            if set_move:
                self.player.set_ready()
                print self.player.get_name() + " submit_move::> Move has been set!"
            time.sleep(2)
            if set_move:
                self.get_round_results()
        except Exception:
            raise Exception('submit_move::> unable to submit a move at this time')

    def get_round_results(self):
        """
        Gets a tuple of: (((Player1_id, move, roundnumber) win/loss),((Player2_id,move,roundnumber) win/loss)))
        Can be useful in predicting future moves
        :return:
        """
        req_get_round_results = self.player_connect.method.get_round_results(self.player.get_player_id())
        round_results = req_get_round_results()
        if round_results == 0:
            print "There isn't a match for you to get results from."
            pass
        if round_results == 1:  # The opposite player hasn't submitted a move, wait a few second and try again
            time.sleep(3)
            return self.get_round_results()
        if round_results:  # If we are handed back a tuple, print them
            print "round_results::> " + str((round_results[0], round_results[1]))
            if round_results[2]:  # Checks last spot in the tuple for another round or not
                time.sleep(5)
                self.submit_move()  # Submits a move
            return round_results
        else:
            print "round_results::> none"

    def get_tournament_results(self):
        """
        Gets the results of a completed tournament, if the tournament isn't completed/still in progress return "Unknown"
        """
        try:
            req_get_tournament_results = self.player_connect.method.get_tournament_results()
            print str(req_get_tournament_results())
        except Exception:
            raise Exception('get_tournament_results::> unable to grab tournament results')