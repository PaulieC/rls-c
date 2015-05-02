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
        except Exception:
            response = "verify_connection::> " + txt + " couldn't connect..."
        return response

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
                return msg
            elif self.tournament_data.tournament.get_num_players() == \
                    self.tournament_data.tournament.get_max_num_players():
                msg = "Can not add player. Tournament room is full"
                return msg
            else:
                if self.tournament_data.register_player(player_id):
                    return player_id
                else:
                    return player_id + " has already been registered."
        else:
            msg = "The tournament registration hasn't been opened yet. Please wait for the game controller to request" \
                  " your registration. Thanks!"
            return msg

    def request_id(self):
        """
        The player calls this to get a unique number for player_id creation client side
        :return int: A new integer
        """
        return self.tournament_data.generate_id_counter()

    def set_max_rounds(self, max_num):
        """
        Sets the tournament's maximum amount of rounds
        :param max_num: int
        """
        self.tournament_data.tournament.set_max_rounds(max_num)
        print "Total rounds have been set to " + str(max_num) + "."

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
                return result
        result = player_id + " isn't in the registered list. Current registered player ids: "
        result += "[" + ", ".join(player_list) + "]"
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
            print "Tournament registration is now open!"
            return True
        except Exception:
            return False

    def close_tournament_registration(self):
        """
        Sets the registration status of the tournament from True to False
        """
        try:
            self.tournament_data.set_registration_status(False)
            print "Tournament registration is now closed!"
            return True
        except Exception:
            return False

    def get_registration_status(self):
        """
        Returns the current registration status
        :return Boolean: The current state of the registration status
        """
        return self.tournament_data.get_registration_status()

    def set_tournament(self, tournament_type):
        """
        Allows the game controller to set the current tournament type
        :param tournament_type: str
        :return: Boolean
        """
        # TODO finish this import issue
        success = False
        try:
            tournament_type = str(tournament_type)
            self.tournament_data.set_tournament(tournament_type)
            success = True
        except Exception:
            pass
        return success

    def set_game(self, new_game):
        # TODO finish this import issue
        pass

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
            return result

    def create_next_match(self):
        """
        Finds the next match and adds this information in the form of a MatchData
        object to the list of matches in TournamentData.
        """
        match = self.tournament_data.create_next_match()
        result = None
        if match:
            result = match
        return result

    def create_all_available_matches(self):
        """ Creates matches until there aren't any to generate """
        temp_list = []
        while True:
            match = self.create_next_match()
            if match is None:
                break
            temp_list.append(match)
        return_list = self.unique_match_sort(temp_list)
        self.tournament_data.matches = return_list
        # printable = [y.to_string() for y in return_list]

    def unique_match_sort(self, match_list):
        temp_list = match_list
        return_list = []
        while temp_list:
            return_list.append(temp_list.pop(0))
            if len(temp_list) != 0:
                return_list.append(temp_list.pop(len(temp_list) - 1))
        return return_list

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
        msg = " There wasn't a match for this move"
        for match in self.tournament_data.matches:
            if match.submit_move(player_id, move):
                result = True
                if match.check_for_ready():
                    self.run_ready(match)
                break
        if result:
            msg = str(result)
        return result

    def run_ready(self, ready_match):
        """
        Runs the current match that is set to ready. Switches
        the match's status to not ready upon running
        :param ready_match: MatchData
        """
        round_result = self.tournament_data.play_round(ready_match)
        ready_match.switch_ready()

    def create_match_pairs(self):
        """
        Looks through the list and tries to find ready pairs. These
        pairs are added to a list in TournamentData
        """
        # TODO deprecated?
        temp_list = []
        if self.tournament_data.matches:
            for index, match in enumerate(self.tournament_data.matches):
                if match.check_for_ready():
                    self.tournament_data.ready_pairs.append(self.tournament_data.matches[index])
                    temp_list.append((match.player1_id, match.player2_id))
        if self.tournament_data.ready_pairs:
            return temp_list
        else:
            return False

    def run_available_matches(self):
        """
        Runs the matches that have ready players. Returns the number of matches completed.
        :return: int
        """
        rounds = -1
        if self.tournament_data.get_game_open():
            for match in self.tournament_data.ready_pairs:
                if match.check_for_ready:
                    round_result = self.tournament_data.play_round(match)
                    match.switch_ready()
                    self.tournament_data.ready_pairs.remove(match)
                    rounds = match.get_curr_round()
        return rounds

    def get_all_available_matches(self):
        """
        Returns all matches that are currently set to ready in the form of a list of tuples
        :return: list
        """
        avail_match = []
        if self.tournament_data.get_game_open():
            for match in self.tournament_data.ready_pairs:
                avail_match.append(match.to_tuple())
        return avail_match

    def get_round_results(self, player_id):
        """
        Allows the client to find the most recent round information
        round_result:
            0 = A match couldn't be located for this player
            1 = Waiting for round to complete
            tuple = Round has completed with the following information:
                ((player_id, move, round_num, win/lost), (player_id, move, round_num, win/lost), True/False next round)
        :param player_id: str
        :return:
        """
        round_result = 0
        player_id = str(player_id)
        for match in self.tournament_data.matches:
            if match.is_round_complete():
                my_player_num = match.is_my_match(player_id)
                if my_player_num > 0:
                    round_result = match.get_result(my_player_num)
                    if match.did_players_retrieve() and (not round_result[2]):
                        # Removes the match if both player's retrieve results AND
                        # there isn't another round for this match
                        self.update_score_keeper(match)     # updates the scorekeeper for each player win/lose
                        self.tournament_data.matches.remove(match)
                    self.create_next_match()    # server tries to generate a new match here
                    break
            else:
                round_result = 1
                break

        if round_result == 0:
            msg = player_id + " doesn't have a round waiting."
        elif round_result == 1:
            msg = player_id + " is waiting for the opponent to submit their move and/or the round to run."
        else:
            msg = player_id + " :: " + str(round_result)
        return round_result

    def is_end_of_tournament(self):
        """ Functions used for testing """
        if self.tournament_data.matches:
            pass
        else:
            print "is_end_of_tournament::> " + str(self.tournament_data.sort_scoreboard())

    def get_tournament_results(self):
        """
        Returns the scores of the tournament IF all matches have been run
        :return: list
        """
        if self.tournament_data.matches:
            return False
        else:
            return self.tournament_data.sort_scoreboard()

    def update_score_keeper(self, match_item):
        """
        Adds a win/loss the the correct player in the match parameter.
        :param match_item: MatchData
        """
        if match_item.get_plr1_score() > match_item.get_plr2_score():
            self.tournament_data.score_keeper[match_item.get_plr1()].win()
            self.tournament_data.score_keeper[match_item.get_plr2()].lose()
        else:
            self.tournament_data.score_keeper[match_item.get_plr2()].win()
            self.tournament_data.score_keeper[match_item.get_plr1()].lose()

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

    def set_tournament_status(self, status):
        """
        Allows the game controller to dictate when the game can run.
        Tournament commands can't execute unless the game status is
        set to True.
        :param status: Boolean
        """
        result = self.tournament_data.set_game_open(status)
        return result

    def get_tournament_status(self):
        """
        Retrieves the current status of the game for the game controller
        :return: Boolean
        """
        result = self.tournament_data.get_game_open()
        return result

    def get_num_registered(self):
        result = len(self.tournament_data.tournament.playerList)
        return result