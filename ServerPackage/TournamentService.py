__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Joe Kvedaras, Collin Day"]

# imports
from bjsonrpc.handlers import BaseHandler
from ServerPackage.TournamentData import *


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
            if self.tournament_data.tournament is None:
                msg = "Can not add player. Tournament is null"
                print "SERVER_SIDE::> " + msg
                return msg
            elif self.tournament_data.tournament.get_num_players() == \
                    self.tournament_data.tournament.get_max_num_players():
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

    def verify_registration(self, player_id):
        """
        Allows the client to confirm that their unique id is registered to the tournament.
        :param player_id: str
        :return: str
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
        result = self.tournament_data.tournament.get_players()
        return result

    def open_tournament_registration(self):
        """
        Sets the registration status of the tournament from False to True
        """
        try:
            self.tournament_data.set_registration_status(True)
            print "SERVER_SIDE::> Registration is open!"
            return True
        except Exception:
            return False

    def close_tournament_registration(self):
        """
        Sets the registration status of the tournament from True to False
        """
        try:
            self.tournament_data.set_registration_status(False)
            print "SERVER_SIDE::> Registration is closed!"
            return True
        except Exception:
            return False

    def get_registration_status(self):
        """
        Returns the current registration status
        :return Boolean: The current state of the registration status
        """
        return self.tournament_data.get_registration_status()

    def set_tournament(self, game_type):
        game_type = str(game_type)
        self.tournament_data.set_tournament(game_type)

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
            self.tournament_data.tournament.set_number_of_players(max_players)
            result = "Number of players set to " + max_players
            print "SERVER_SIDE::> " + result
            return result

    def run(self):
        """Set the game and run the tournament"""
        if self.tournament_data.tournament is None:
            print "Can not run tournament. Tournament is null"
        else:
            # TODO hold move with player_id
            # TODO submit moves to the tournament
            # TODO determine the winner of the round
            # TODO set a message tuple that has the winner of the previous round
            # TODO allow players of the round to collect these tuples
            self.find_next_match()

    def find_next_match(self):
        """
        Finds the next match and adds this information in the form of a MatchData
        object to the list of matches in TournamentData.
        """
        match = self.tournament_data.tournament.create_next_match()
        result = False
        if match:
            if self.tournament_data.add_match(match[0][0], match[0][1], match[1]):
                result = match
        print "SERVER_SIDE::> " + str(result)
        return result

    def set_player_move(self, player_id, move):
        """
        Attempts to set the player move to the correct match item in
        the matches list.
        :param player_id: str
        :param move: int
        :return: Boolean
        """
        result = False
        player_id = str(player_id)
        for match in self.tournament_data.matches:
            if match.submit_move(player_id, move):
                result = True
                break
        return result

    def check_for_ready_pairs(self):
        """
        Looks through the list and tries to find ready pairs. These
        pairs are added to a list in TournamentData
        """
        if self.tournament_data.matches:
            for index, match in enumerate(self.tournament_data.matches):
                if match.check_for_ready():
                    self.tournament_data.ready_pairs.append(self.tournament_data.matches[index])
        if self.tournament_data.ready_pairs:
            print "SERVER_SIDE::> " + self.tournament_data.ready_pairs
            return self.tournament_data.ready_pairs
        else:
            print "SERVER_SIDE::> No ready pairs could be found at this time"
            return False

    def run_ready_pair(self):
        """
        Runs the matches that have ready players. Returns the number of matches completed.
        :return: int
        """
        rounds = 0
        for match in self.tournament_data.ready_pairs:
            if match.check_for_ready:
                self.tournament_data.tournament.play_round(match)
                rounds += 1
        return rounds

    def get_round_results(self, player_id):
        """
        Allows the client to find out if they won/lost the last round. Returns 1 for win, 0 for lose, and
        None if they didn't have a round
        :param player_id: str
        :return:
        """
        result = None
        for match in self.tournament_data.matches:
            my_player_num = match.is_my_match(player_id)
            if my_player_num > 0:
                round_result = match.get_result(my_player_num)
                if round_result:
                    result = round_result[2]
        return result

    def get_game(self):
        """
        Gets the name of the current game
        :return: str
        """
        result = ""
        if self.tournament_data.tournament.game is not None:
            result = self.tournament_data.tournament.game.get_name()
        else:
            pass
        return result

    def get_tournament(self):
        """
        Gets the name of the current tournament
        :return: str
        """
        result = ""
        if self.tournament_data.tournament is not None:
            result = self.tournament_data.tournament.get_name()
        else:
            pass
        return result