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
        self.player2_id = player2
        self.match_head = player1 + player2
        self.max_rounds = num_rounds
        self.round_num = 1
        self.player1_round = ()     # (player_id, move, round_num)
        self.player1_rounds = []    # [(player_id, move, win/loss, opponent_id), etc]
        self.player2_round = ()     # (player_id, move)
        self.player2_rounds = []    # [(player_id, move, win/loss, opponent_id), etc]

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
        if player_id is self.player1_id:
            if self.player1_round:
                self.player1_round = (player_id, player_move, self.round_num)
                result = True
        elif player_id is self.player2_id:
            if self.player2_round:
                self.player2_round = (player_id, player_move, self.round_num)
                result = True
        return result

    def submit_round_results(self, winner, loser):
        """
        Holds the winner of the round's information as well as the loser's.
        Also checks if this object should allow another
        :param winner: str
        :param loser: str
        :return: int
        """
        # -1 = this is the end of the match for these two players
        # 0 = failed to find player ids
        # 1 = found ids and set the proper information
        success = 0
        if winner is self.player1_id:
            plr1_round = (winner, self.player1_round[1], 1, loser)
            plr2_round = (loser, self.player2_round[1], 0, winner)
            success = 1
        elif loser is self.player1_id:
            plr2_round = (winner, self.player1_round[1], 1, loser)
            plr1_round = (loser, self.player1_round[1], 0, winner)
            success = 1
        else:
            return success
        self.player1_rounds.append(plr1_round)
        self.player2_rounds.append(plr2_round)
        if self.prep_next_round():
            return success
        else:
            return -1

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

# Setters

# Getters