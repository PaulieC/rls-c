"""
This file will be used to hold instances of the current tournament and player information.
This is a companion to the TournamnetService as data doesn't stay persistent without an instance
for the variable
"""
__author__ = 'system1'
# imports
from AvailableTournaments.AllPlayAll import *
from AvailableGames.RockPaperScissors import *


class TournamentData:
    def __init__(self):
        self.tournament = AllPlayAll()
        self.game = RockPaperScissors()
        self.id_counter = 0
        self.connected_players = []
        self.player_move_info = ()
        self.tournament_round_info = [()]
        self.registration_open = False
        self.registered_players = [()]

# Adders
    def add_connected_players(self, player):
        self.connected_players.append(player)

    def add_tournament_round_info(self, player1_move_info, player2_move_info):
        info = (player1_move_info, player2_move_info)
        self.tournament_round_info.append(info)

    def add_registered_players(self, player_id):
        reg_info = (player_id, self.tournament.get_name())
        self.registered_players.append(reg_info)

# Removers
    def rem_connected_players(self, player):
        self.connected_players.remove(player)

    def rem_tournament_round_info(self, player1_id, player2_id):
        for index, item in enumerate(self.tournament_round_info):
            if player1_id in item and player2_id in item:
                self.tournament_round_info.remove(item)
                break

    def rem_registered_players(self, player_id):
        for item in self.registered_players:
            if player_id in item:
                self.registered_players.remove(item)
                break

# Setters
    def set_tournament(self, tour_name):
        # TODO initialize this function
        pass

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
        self.registration_open = status

    def set_registered_players(self, player_list):
        self.registered_players = player_list

# Getters
    def get_tournament(self):
        return self.tournament

    def get_game(self):
        return self.game

    def get_id_counter(self):
        return self.id_counter

    def get_connected_players(self):
        return self.connected_players

    def get_player_move_info(self):
        return self.player_move_info

    def get_tournament_rount_info(self):
        return self.tournament_round_info

    def get_registration_status(self):
        return self.registration_open

    def get_registered_players(self):
        return self.registered_players