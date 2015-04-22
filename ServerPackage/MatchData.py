"""
This class should be called in TournamentData once a new match has been created.
It should exist for the players to keep track of round information as it is
updated each round in TournamentData.
"""
__author__ = "Paul Council, Anand Patel"
__version__ = "sprint3"


class MatchData:
    """
    Class to track the match information between two players
    """
    def __init__(self, player1, player2, num_rounds):
        """
        :param player1: str
        :param player2: str
        :param num_rounds: int
        """
        self.player1_id = player1
        self.plr1_client_ready = False
        self.plr2_client_ready = False
        self.player2_id = player2
        self.match_head = player1 + player2
        self.max_rounds = num_rounds
        self.round_num = 1
        self.player1_round = ()     # (player_id, move, round_num, win/loss)
        self.player1_rounds = []    # [(player_id, move, round_num, win/loss), etc]
        self.player2_round = ()     # (player_id, move, round_num, win/loss)
        self.player2_rounds = []    # [(player_id, move, round_num, win/loss), etc]

# General Functions
    def submit_move(self, player_id, player_move):
        """
        Holds the move for the respective player. This information is used
        when storing/retrieving results for the winner/loser
        :param player_id: str
        :param player_move: int
        :return: Boolean
        """
        result = False
        if player_id == self.player1_id:
            if not self.player1_round:
                self.player1_round = (player_id, player_move, self.round_num)
                self.plr1_client_ready = True
                result = True
        elif player_id == self.player2_id:
            if not self.player2_round:
                self.player2_round = (player_id, player_move, self.round_num)
                self.plr2_client_ready = True
                result = True
        return result

    def submit_round_results(self, match_results):
        """
        Holds the winner of the round's information as well as the loser's.
        Also checks if this object should allow another
        """
        # -1 = this is the end of the match for these two players
        # 0 = failed to find player ids
        # 1 = found ids and set the proper information
        success = False
        if self.player1_id == match_results[0][0][0] and self.player2_id == match_results[1][0][0]:
            self.player1_round = (match_results[0][0][0],
                                  match_results[0][0][1],
                                  match_results[0][0][2],
                                  match_results[0][1])
            self.player2_round = (match_results[1][0][0],
                                  match_results[1][0][1],
                                  match_results[1][0][2],
                                  match_results[1][1])
            self.player1_rounds.append(self.player1_round)
            self.player2_rounds.append(self.player2_round)
            success = True
        print "submit_round_results::> " + str(success)
        return success

    def clear_round(self):
        """
        Clears the current round info
        """
        self.player1_round = ()
        self.player2_round = ()

    def prep_next_round(self):
        """
        Clears the current round info IF the next round isn't greater than
        the max number of rounds
        :return:
        """
        self.round_num += 1
        result = False
        if self.round_num > self.max_rounds:
            pass
        else:
            self.clear_round()
            result = True
        return result

    def check_for_ready(self):
        """
        Returns true if both players are set to ready
        :return: Boolean
        """
        result = False
        if self.plr1_client_ready and self.plr2_client_ready:
            result = True
        return result

    def is_my_match(self, player_id):
        """
        Returns true if this match belongs to the requesting player
        :param player_id: str
        :return: Boolean
        """
        result = -1
        if player_id == self.player1_id:
            result = 1
        elif player_id == self.player2_id:
            result = 2
        return result

    def switch_ready(self):
        """ Inverts the ready status of the player """
        self.plr1_client_ready = not self.plr1_client_ready
        self.plr2_client_ready = not self.plr2_client_ready

    def get_result(self):
        """
        Returns the result of the most recent round for the respective player
        :return: int
        """
        return self.player1_round, self.player2_round

    def match_verify(self, match_item):
        """
        Method used to check if a match item is the same as this instance
        :param match_item: MatchData
        :return: Boolean
        """
        result = False
        if match_item.player1_id == self.player1_id and match_item.player2_id == self.player2_id:
            result = True
        return result
# Setters
    def set_ready(self, player_id):
        """
        Allows the caller to set themselves to ready
        :param player_id: str
        :return: Boolean
        """
        result = False
        if self.player1_id == player_id:
            result, self.plr1_client_ready = True
        elif self.player2_id == player_id:
            result, self.plr2_client_ready = True
        else:
            return result

    def to_tuple(self):
        """
        Gets the current round info and returns it in the form of two tuples
        :return: tuple
        """
        return self.player1_round, self.player2_round

# Getters
    def get_curr_round(self):
        return self.round_num

    def get_max_round(self):
        return self.max_rounds