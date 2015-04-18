"""
This file will be used to hold instances of the current tournament and player information.
This is a companion to the TournamentService as data doesn't stay persistent without an instance
for the variable
"""
import importlib

__author__ = 'system1'
# imports
from AvailableTournaments.AllPlayAll import *
from AvailableGames.RockPaperScissors import *
from ServerPackage.MatchData import *


class TournamentData:
    """
    Class used to maintain data for the server
    """
    def __init__(self):
        self.tournament = AllPlayAll()
        self.game = RockPaperScissors()
        self.id_counter = 0
        self.connected_players = []
        self.registration_open = False
        self.registered_players = []
        self.ready_pairs = []
        self.matches = []
        # TODO The following line should be in a function in the future
        self.tournament.game = self.game

# General Functions
    def check_reg_stat(self):
        """
        Finds and returns the current registration status
        :return Boolean:
        """
        result = False
        if self.registration_open:
            result = True
        return result

    def register_player(self, player_id):
        """
        Allows the player to register to the tournament list.
        The player's unique id is used along with the name of the Tournament when adding to the
        registered_players list
        :param player_id: The player's unique id
        :type player_id: str
        :return Boolean:
        """
        index = player_id.rfind("_")
        player_num = player_id[index:]
        for item in self.tournament.playerList:
            if player_num in item:
                return False
        # player unique id isn't in the registered list, so register this player
        self.tournament.register_player(player_id)
        self.add_registered_players(player_id)
        return True

    def add_match(self, player1, player2, num_rounds):
        """
        Adds another match to the list of matches. This match will be used as a reference
        for the player to observe the results.
        :param player1: str
        :param player2: str
        :param num_rounds: int
        :return: Boolean
        """
        try:
            new_match = MatchData(player1, player2, num_rounds)
            self.matches.append(new_match)
            return True
        except Exception:
            return False

    def set_player_move(self, player_id, move):
        """
        Function used to allow the player to submit their move for the current round
        :param player_id: str
        :param move: itn
        :return: Boolean
        """
        result = False
        for match in self.matches:
            if match.submit_move(player_id=player_id, player_move=move):
                result = True
        return result

    def generate_id_counter(self):
        """
        Holds the current id value. Increases the id value by 1. Returns the held id value
        :return int:
        """
        result = self.id_counter
        self.increase_id_counter()
        return result

    def increase_id_counter(self):
        """ Increments the id counter by 1. """
        self.id_counter += 1

    def play_round(self, match_item):
        result = self.tournament.play_round(match_item)
        for matches in self.matches:
            if matches.submit_round_results(result):
                return result

    def run_match(self):
        # TODO implement
        pass

# Adders
    def add_connected_players(self, player_name):
        """
        Add the player id to the connected_players list
        :param player_name: str
        """
        if player_name not in self.connected_players:
            self.connected_players.append(player_name)

    def add_registered_players(self, player_id):
        """
        Add the player id to the list of registered players
        :param player_id: str
        """
        reg_info = (player_id, self.tournament.get_name())
        self.registered_players.append(reg_info)

# Removers
    def rem_connected_players(self, player):
        """
        Removes the player id from the list of connected players
        :param player: str
        """
        self.connected_players.remove(player)

    def rem_registered_players(self, player_id):
        """
        Removes the player id from the list of registered players
        :param player_id: str
        """
        for item in self.registered_players:
            if player_id in item:
                self.registered_players.remove(item)
                self.tournament.playerList.remove(player_id)
                break

# Setters
    def set_tournament(self, game_type):
        tour = importlib.import_module("AvailableTournaments." + game_type)
        self.tournament = getattr(tour, game_type)()
        print "Tournament type is now: ", self.tournament.get_name()

    def set_game(self, game_name):
        # TODO initialize this function
        pass

    def set_id_counter(self, num):
        self.id_counter = num

    def set_connected_players(self, player_list):
        # TODO initialize this function
        pass

    def set_player_move_info(self):
        # TODO initialize this function
        pass

    def set_tournament_round_info(self):
        # TODO initialize this function
        pass

    def set_registration_status(self, status):
        """
        Allows the caller to change the status of registration in the tournament
        :param status: Boolean
        """
        self.registration_open = status

    def set_registered_players(self, player_list):
        """
        Allows a list of players to be set to this local player list
        :param player_list: list
        """
        self.registered_players = player_list

# Getters
    def get_tournament(self):
        """
        Returns the current tournament object
        :return: Tournament
        """
        return self.tournament

    def get_game(self):
        """
        Returns the current game object
        :return: Game
        """
        return self.game

    def get_id_counter(self):
        """
        Returns the current id_counter
        :return: int
        """
        return self.id_counter

    def get_connected_players(self):
        """
        Returns the current list of connected players
        :return: list
        """
        return self.connected_players

    def get_registration_status(self):
        """
        Returns the current registration status
        :return: Boolean
        """
        return self.registration_open

    def get_registered_players(self):
        """
        Returns the list of registered players
        :return: list
        """
        return self.registered_players

    def get_matches(self):
        """
        Returns the list of matches
        :return: list
        """
        return self.matches