__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["jeffrey creighton"]

# imports
import ScorekeeperHistoryItem
import ScoreKeeperListItem


class Scorekeeper:
    """
    Purpose: to collect and store scores from all players and matches

    Attributes:
        leader_board: the list of player's score keeper list items
        match_history: the list scorekeeperhistoryitems from the match
    """

    leader_board = []
    match_history = []

    def __init__(self):
        self.leader_board = []
        self.match_history = []

    def update_tournament(self, player_1, player_2, winner, score_1, score_2):
        """
        updates both the leader_board and match_history
        :param player_1: player in position 1
        :type player_1: ScoreKeeperListItem.ScorekeeperListItem
        :param player_2: player in position 2
        :type player_2: ScoreKeeperListItem.ScorekeeperListItem
        :param winner: the winning player
        :type winner: Player.Player
        :param score_1: player_1's score
        :type score_1: int
        :param score_2: player_2's score
        :type score_2: int
        """

        # creates the history item based on the match details
        history_item = ScorekeeperHistoryItem.ScorekeeperHistoryItem(player_1, player_2, winner, score_1, score_2)

        # adds the history item to match_history[]
        self.match_history.append(history_item)

        # creates the list_items for both players and checks to see if they are on the leader_board
        # if not present on the leader board, they are appended
        list_item_a = ScoreKeeperListItem.ScorekeeperListItem(player_1)
        list_item_b = ScoreKeeperListItem.ScorekeeperListItem(player_2)
        if self.check_player(list_item_a):
            self.leader_board.append(list_item_a)
        if self.check_player(list_item_b):
            self.leader_board.append(list_item_b)

        # Checks the winner and awards a point to that player
        if score_1 > score_2:
            self.make_winner(player_1)
        elif score_2 > score_1:
            self.make_winner(player_2)
        # in the unlikely event of a tie, no points awarded
        else:
            pass

    def check_player(self, player_list_item):
        """
        checks to see if the player is already on the leader board.
        returns true if they are not, false if they are.
        :param player_list_item: the player list item to check against on the board
        :type player_list_item: ScoreKeeperListItem.ScorekeeperListItem
        :return check: the result of the check
        :rtype: bool
        """
        check = True
        for i in range(len(self.leader_board)):
            if self.leader_board[i] == player_list_item.get_player():
                check = False
            else:
                check = True
        return check

    def make_winner(self, player_list_item):
        """
        update the winner's score
        :param player_list_item: the player's list item to update as the winner
        :type player_list_item: ScoreKeeperListItem.ScorekeeperListItem
        """
        for i in range(len(self.leader_board)):
            if player_list_item is self.leader_board[i]:
                player_list_item.update_score()

    def get_leader_board(self):
        """
        #returns this leader_board
        :return: the list of player's who have won
        :rtype: list
        """
        return self.leader_board

    def get_match_history(self):
        """
        #returns this match_history
        :return: the list of scorekeeperhistory items from the match
        :rtype: list
        """
        return self.match_history