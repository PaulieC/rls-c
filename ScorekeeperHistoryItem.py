__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["jeffrey creighton"]


class ScorekeeperHistoryItem:
    """
    Purpose: data structure for tracking match history

    Attributes:
        player_1: player in position 1
        player_2: player in position 2
        winner: the winning player
        score_1: player_1's score
        score_2: player_2's score
    """

    def __init__(self, player_1, player_2, winner, score_1, score_2):
        self.player1 = player_1
        self.player2 = player_2
        self.winner = winner
        self.score1 = score_1
        self.score2 = score_2