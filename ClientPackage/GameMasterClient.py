__author__ = "Paul Council, Anand Patel"
__version__ = "sprint5"

from ClientPackage.PlayerClient import *


class GameMasterClient(PlayerClient):
    """
    An advanced client class to allow the GameController to handle the server in ways that a
    regular client cannot. Used to changed tournament type, max players, open/close registration, etc.
    """

    def __init__(self, player):
        PlayerClient.__init__(self, player)

    def init_tour_data(self):
        """
        Sends a request to the server to initialize the tournament data object.
        :return:
        """
        try:
            result = "unable to init"
            req_init_tour_data = self.player_connect.method.init_tour_data()
            tour_status = req_init_tour_data()
            if tour_status:
                result = "tournament has been initialized"
            print "init_tour_data::> " + result
            return result
        except Exception:
            raise Exception('init_tour_data::> unable to initialize the tournament data at this timef')

    def set_number_of_players(self, max_players):
        """
        Calls the function server side with the parameter to set as the maximum number of players that
        can register in the tournament.
        :param max_players: The highest amount of players
        :type: int
        """
        try:
            req_set_num_players = self.player_connect.method.set_num_players(max_players)
            req_set_num_players()
        except Exception:
            raise Exception(
                'set_number_of_players::> unable to chance the number of players in the tournament at this time')

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
        try:
            req_open_registration = self.player_connect.method.open_tournament_registration()
            tour_open = req_open_registration()
            msg = "Tournament registration couldn't open"
            if tour_open:
                msg = "Tournament registration is open"
            return msg
        except Exception:
            raise Exception('open_tournament_registration::> unable to open the tournament registration at this time')

    def close_tournament_registration(self):
        """
        Closes the tournament registration so players can no longer register
        """
        try:
            req_close_registration = self.player_connect.method.close_tournament_registration()
            tour_closed = req_close_registration()
            msg = "Tournament registration couldn't close"
            if tour_closed:
                try:
                    self.create_all_available_matches()
                except Exception:
                    raise Exception("Unable to create matches at this time.\n"
                                    "Have players been registered?...")
                msg = "Tournament registration is closed"
            return msg
        except Exception:
            raise Exception("close_tournament_registration::> unable to close the tournament registration at this time")

    def list_registered_players(self):
        """
        Prints the players that have registered to the tournament
        """
        try:
            req_registered_players = self.player_connect.method.get_registered_players()
            players = req_registered_players()
            if players:
                print "list_registered_players::> "
                self.print_list(players)
                return
            print "list_registered_players::> There aren't any registered players at this time..."
        except Exception:
            raise Exception('list_registered_players::> unable to list registered players at this time.')

    def create_match_pairs(self):
        """
        Generates ready pairs on the server side for a match if any are set to ready.
        """
        try:
            req_ready_pairs = self.player_connect.method.create_match_pairs()
            pairs = req_ready_pairs()
            if pairs:
                for pair in pairs:
                    print "create_match_pairs::> "
                    self.print_list(pair)
                return
            print "create_match_pairs::> There aren't any ready pairs at this time..."
        except Exception:
            raise Exception('create_match_pairs::> unable to create match pairs at this time')

    def create_next_match(self):
        """
        Submits a request to generate a new match for registered players that aren't currently in
        a match. If this isn't possible, a message will be printed stating this, otherwise, info
        on the newly created match will be printed.
        """
        try:
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
        except Exception:
            raise Exception('create_next_match::> unable to create a next match')

    def run_available_matches(self):
        """
        Requests that the server runs all the matches that have players
        set to the ready status. This will then print the round number
        that just completed.
        """
        try:
            while True:
                created_matches = self.player_connect.method.get_all_available_matches()
                matches = created_matches()
                if not matches == []:
                    result = "No pairs are ready at this time..."
                    req_run_ready = self.player_connect.method.run_available_matches()
                    run_ready = req_run_ready()
                    if run_ready > 0:
                        result = "Completed round number " + str(run_ready)
                    print "run_available_matches::> " + result
                else:
                    break
        except Exception:
            raise Exception('run_available_matches::> unable to run available matches')

    def set_tournament(self, tour_type):
        """
        Sends a request to the server to set the specified tournament type
        :param game_type: the game_type that we want to set
        """
        try:
            req_set_tournament = self.player_connect.method.set_tournament(tour_type)
            req_set_tournament()
        except Exception:
            raise Exception('set_tournament::> unable to set the specified tournament')

    def set_game(self, game_type):
        try:
            req_set_game = self.player_connect.method.set_game(game_type)
            req_set_game()
        except Exception:
            raise Exception('set_game::> unable to set the specified tournament')

    def get_tournament_status(self):
        """
        Sends a request to the server to get the current tournament status
        :return status: the status of the tournament
        """
        try:
            req_get_tournament_status = self.player_connect.method.get_tournament_status()
            status = req_get_tournament_status()
            return status
        except Exception:
            raise Exception('get_tournament_status::> unable to get the correct tournament status')

    def set_tournament_status(self, status):
        """
        Sends a request to the server to set the tournament status to the specified type
        :param status:
        :return:
        """
        try:
            req_set_tournament_status = self.player_connect.method.set_tournament_status(status)
            req_set_tournament_status()
        except Exception:
            raise Exception('set_tournament_status::> unable to set the correct tournament status')

    def create_all_available_matches(self):
        """
        Sends a request to the server to create all available matches
        :return:
        """
        try:
            req_find_all_available_matches = self.player_connect.method.create_all_available_matches()
            req_find_all_available_matches()
        except Exception:
            raise Exception('create_all_available_matches::> unable to generate request')

    def set_max_rounds(self, max_num):
        """
        Sends a request to the server to set the maximum number of rounds per match
        :param max_num: the maximum of rounds
        """
        try:
            req_set_max_rounds = self.player_connect.method.set_max_rounds(max_num)
            req_set_max_rounds()
        except Exception:
            raise Exception("set_max_rounds::> unable to set the max rounds")

    def get_num_registered(self):
        """
        Sends a request to the server to return the number of players registered in the current tournament
        :return: the number of registered players
        """
        try:
            req_get_num_reg = self.player_connect.method.get_num_registered()
            return req_get_num_reg()
        except Exception:
            raise Exception('get_num_registered::> unable to get the number of registered players')
