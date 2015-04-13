"""
An advanced client class to allow the GameController to handle the server in ways that a
regular client cannot.
"""
__author__ = 'paulie'

from ClientPackage.PlayerClient import *


class GameMasterClient(PlayerClient):
    def __init__(self, player):
        PlayerClient.__init__(self, player)

    def init_tour_data(self):
        result = "unable to init"
        req_init_tour_data = self.player_connect.method.init_tour_data()
        tour_status = req_init_tour_data()
        if tour_status:
            result = "tournament has been initialized"
        print "init_tour_data::> " + result
        return result

    def set_number_of_players(self, max_players):
        """
        Calls the function server side with the parameter to set as the maximum number of players that
        can register in the tournament.
        :param max_players: The highest amount of players
        :type: int
        """
        req_set_num_players = self.player_connect.method.set_num_players(max_players)
        print "set_number_of_players::> " + req_set_num_players()

    def list_available_tournaments(self):
        """
        Lists the tournaments that are available in the AvailableTournaments directory.
        This is printed to the console
        """
        tournament_dir = self.get_dir("AvailableTournaments")
        tournament_list = self.list_files(tournament_dir)
        return tournament_list

    def list_available_games(self):
        """
        Lists the games that are available in the AvailableGames directory.
        This is printed to the console.
        :return:
        """
        game_dir = self.get_dir("AvailableGames")
        game_list = self.list_files(game_dir)
        return game_list

    def open_tournament_registration(self):
        """
        Opens the player's ability to register to the tournament
        """
        req_open_registration = self.player_connect.method.open_tournament_registration()
        tour_open = req_open_registration()
        msg = "Tournament registration couldn't open"
        if tour_open:
            msg = "Tournament registration is open"
        print "open_tournament_registration::> " + msg
        return msg

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

# obj = GameMasterClient(BEPCPlayer())
# obj.set_tournament()