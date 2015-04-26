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

    def close_tournament_registration(self):
        """
        Closes the player's ability to register to the tournament
        """
        req_close_registration = self.player_connect.method.close_tournament_registration()
        tour_closed = req_close_registration()
        msg = "Tournament registration could not be closed"
        if tour_closed:
            msg = "Tournament registration is closed"
            self.create_all_available_matches()
        print "close_tournament_registration::> " + msg

    def list_registered_players(self):
        """
        Prints the players that have registered to the tournament
        """
        req_registered_players = self.player_connect.method.get_registered_players()
        players = req_registered_players()
        result = "list_registered_players::> There aren't any registered players at this time..."
        if players:
            print "list_registered_players::> "
            self.print_list(players)
            return
        print result

    def create_match_pairs(self):
        """
        Generates  ready pairs on the server side for a match if any are set to ready.
        """
        req_ready_pairs = self.player_connect.method.create_match_pairs()
        pairs = req_ready_pairs()
        if pairs:
            for pair in pairs:
                print "create_match_pairs::> "
                self.print_list(pair)
            return
        print "create_match_pairs::> There aren't any ready pairs at this time..."

    def create_next_match(self):
        """
        Submits a request to generate a new match for registered players that aren't currently in
        a match. If this isn't possible, a message will be printed stating this, otherwise, info
        on the newly created match will be printed.
        """
        req_next_match = self.player_connect.method.create_next_match()
        next_match = req_next_match()
        result = "Couldn't create a new match"
        if next_match:
            play1 = str(next_match[0][0])
            play2 = str(next_match[0][1])
            rounds = str(next_match[1])
            result = "A new match has been created between " + \
                     play1 + " and " + play2 + " for " + \
                     rounds + " rounds."
        print "create_next_match::> " + result

    def run_available_matches(self):
        """
        Requests that the server runs all the matches that have players
        set to the ready status. This will then print the round number
        that just completed.
        """
        while True:
            created_matches = self.player_connect.method.get_all_available_matches()
            matches = created_matches()
            #print "run_available_matches::>" + str(matches)
            if not matches == []:
                result = "No pairs are ready at this time..."
                req_run_ready = self.player_connect.method.run_available_matches()
                run_ready = req_run_ready()
                if run_ready > 0:
                    result = "Completed round number " + str(run_ready)
                print "run_available_matches::> " + result
            else:
                break

    def set_tournament(self, game_type):
        req_set_tournament = self.player_connect.method.set_tournament(game_type)
        req_set_tournament()

    def set_game(self):
        # TODO implement similarly to set_tournament
        pass

    def start_game(self):
        # TODO impelment this method to run at least one round
        pass

    def end_game(self):
        pass

    def get_game_status(self):
        #TODO put this in the GUI
        req_get_game_status = self.player_connect.method.get_tournament_status()
        status = req_get_game_status()
        print str(status)
        return status

    def set_game_status(self, status):
        req_set_game_status = self.player_connect.method.set_tournament_status(status)
        req_set_game_status()

    def create_all_available_matches(self):
        req_find_all_available_matches = self.player_connect.method.create_all_available_matches()
        req_find_all_available_matches()
        # available_matches = req_find_all_available_matches()
        # print "create_all_available_matches" + str(available_matches)
        # return available_matches

    def set_max_rounds(self, max_num):
        req_set_max_rounds = self.player_connect.method.set_max_rounds(max_num)
        req_set_max_rounds()



# obj = GameMasterClient(BEPCPlayer())
# obj.set_tournament()