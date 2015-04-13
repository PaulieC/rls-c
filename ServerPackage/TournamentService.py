__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Joe Kvedaras, Collin Day"]

# imports
from bjsonrpc.handlers import BaseHandler
from ServerPackage.TournamentData import *
from AvailableTournaments.AllPlayAll import *
from AvailableGames.RockPaperScissors import *
import importlib


class TournamentService(BaseHandler):
    """
    Supports the connection of players to the tournament.get_tournament().
    This class holds the functions required for the tournament
    to start, run, and end successfully.
    """

    # Initializes the tournament data file that is used for persistent data
    tournament_data = TournamentData()

    def verify_connection(self, txt):
        """
        Returns a message to the player to confirm that they have established a solid connection
        with the server.
        :param txt: The player's name
        :return str: the message including the player's name to confirm a connection
        """
        txt = str(txt)
        response = "Hello %s! " \
                   "\nYou have connected to the registration queue." \
                   "\nPlease standby for registration confirmation..." % txt
        try:
            self.tournament_data.add_connected_players(txt)
            print "SERVER_SIDE::> " + response     # prints information server side
            return response     # sends information to the client to handle
        except Exception:
            print "SERVER_SIDE::> " + txt + " couldn't connect..."

    def register_player(self, player_id):
        """
        Allows a player to register their name with the tournament's list of registered players.
        For any issues registering, a message will be returned explaining the reason
        :param player_id: The calling player's id
        :type: str
        :return str: A message corresponding to the result of this function
        """
        player_id = str(player_id)
        if self.tournament_data.get_registration_status():
            if self.tournament_data.get_tournament() is None:
                msg = "Can not add player. Tournament is null"
                print "SERVER_SIDE::> " + msg
                return msg
            elif self.tournament_data.get_tournament().get_num_players() == \
                    self.tournament_data.get_tournament().get_max_num_players():
                msg = "Can not add player. Tournament room is full"
                print "SERVER_SIDE::> " + msg
                return msg
            else:
                if self.tournament_data.register_player(player_id):
                    print "SERVER_SIDE::> " + player_id
                    return player_id
                else:
                    print "SERVER_SIDE::> " + player_id + " has already been registered"
                    return player_id + " has already been registered."
        else:
            print "SERVER_SIDE::> " + player_id + " tried to connect while registration is closed"
            msg = "The tournament registration hasn't been opened yet. Please wait for the game controller to request" \
                  " your registration. Thanks!"
            return msg

    def request_id(self):
        """
        The player calls this to get a unique number for player_id creation client side
        :return int: A new integer
        """
        return self.tournament_data.generate_id_counter()

    def register_players(self, player_list):
        """
        Registers the Player objects that exist in the player_list
        :param player_list: the collected list of players to register
        :type player_list: list
        """
        # TODO remove?
        for plr in player_list:
            self.register_player(plr)

    def verify_registration(self, player_id):
        """
        :param player:
        :type player: Player.Player
        :return:
        """
        player_id = str(player_id)
        player_list = self.tournament_data.get_registered_players()
        for player_pack in player_list:
            if player_id in player_pack:
                result = "Player \'" + player_id + "\' has been registered"
                print "SERVER_SIDE::> " + result
                return result
        result = player_id + " isn't in the registered list. Current registered player ids: "
        result += "[" + ", ".join(player_list) + "]"
        print "SERVER_SIDE::> " + result
        return result

    def get_registered_players(self):
        """
        Gets the players registered to the tournament in the form of a list
        :return result: The list of players registered
        """
        result = self.tournament.get_players()
        return result

    def open_tournament_registration(self):
        """
        Sets the registration status of the tournament from False to True
        """
        try:
            self.tournament_data.set_registration_status(True)
            return True
        except Exception:
            return False

    def close_tournament_registration(self):
        """
        Sets the registration status of the tournament from True to False
        """
        try:
            self.tournament_data.set_registration_status(False)
            return True
        except Exception:
            return False

    def get_registration_status(self):
        """
        Returns the current registration status
        :return Boolean: The current state of the registration status
        """
        return self.tournament_data.get_registration_status()

    def new_id(self):
        """
        :return:
        """
        self.id_counter += 1
        return self.id_counter

    def set_tournament(self, new_tournament_package, new_tournament_module):
        """
        Allow client to set the tournament type. Defaults to
        AllPlayAll tournament type
        """
        # TODO finish this import issue
        if new_tournament_package is not None:
            print "The current tournament is " + str(self.tournament)
            tour = importlib.import_module("AvailableTournaments.AllPlayAll.AllPlayAll")
            self.tournament = tour()
            return "The current tournament is " + str(self.tournament)

    def set_game(self, new_game):
        # TODO finish this import issue
        if new_game is not None:
            print "The current tournament is " + str(self.game)
            tour = importlib.import_module(new_game, "*")
            self.game = tour.AllPlayAll()
            return "The current tournament is " + str(self.game)

    def set_num_players(self, max_players):
        """
        Allows the game controller to set the maximum number of players for this tournament
        :param max_players: The highest amount of players allowed to register to the tournament
        :type: int
        :return str: The message that the value has been changed if the parameter was greater than 0
        """
        if max_players > 0:
            self.tournament.set_number_of_players(max_players)
            result = "Number of players set to " + max_players
            print "SERVER_SIDE::> " + result
            return result

    def set_display(self, display):
        """
        Assigns the display solution for this service
        :param display: display to project information
        :type display: Display.Display
        """
        if self.tournament is None:
            print "Tournament is null"
        else:
            self.tournament.attach_display(display)

    def run(self):
        """Set the game and run the tournament"""
        if self.tournament is None:
            print "Can not run tournament. Tournament is null"
        else:
            # TODO hold move with player_id
            # TODO submit moves to the tournament
            # TODO determine the winner of the round
            # TODO set a message tuple that has the winner of the previous round
            # TODO allow players of the round to collect these tuples
            self.find_next_match()
            # self.tournament.run()

    def find_next_match(self):
        match = self.tournament.create_next_match()
        self.tournament_match_info.append(match)

    def set_player_move(self, player_id, move):
        # TODO hold move with player_id
        move_pack = (player_id, move)
        self.player_move_info.append(move_pack)

    def check_for_ready_pairs(self):
        result = None
        for matches in self.tournament_match_info:
            if result is not None:
                break
            player1 = matches[0][0]
            player2 = matches[0][1]
            for players1 in self.player_move_info:
                if result is not None:
                    break
                if player1 in players1[0]:
                    for players2 in self.player_move_info:
                        if player2 in players2[0]:
                            result = (players1, players2)
        return result

    def run_ready_pair(self, player1_and_move, player2_and_move):
        match = ((player1_and_move, player2_and_move), 5)
        result = self.tournament.play_rounds(match)
        return result   # ((player1, win/lose), (player2, win/lose))

    def get_round_results(self, player_id):
        result = None
        for player in self.tournament_round_info:
            if player_id in player[0]:
                result = player[0][1]
                self.tournament_round_info.remove(player)   # remove this item as it isn't useful anymore
                break
            elif player_id in player[1]:
                result = player[1][1]
                self.tournament_round_info.remove(player)   # remove this item as it isn't useful anymore
                break
        return result

    def get_game(self):
        result = ""
        if self.tournament.game is not None:
            result = self.tournament.game.get_name()
        else:
            pass
        return result

    def get_tournament(self):
        result = ""
        if self.tournament is not None:
            result = self.tournament.get_name()
        else:
            pass
        return result