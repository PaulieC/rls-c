__author__ = 'jeffrey creighton & anand patel'
# Purpose: to collect and store scores from all players and matches

import ScorekeeperHistoryItem
import ScoreKeeperListItem


class Scorekeeper:
    leader_board = []
    match_history = []

    def __init__(self):
        self.leader_board = []
        self.match_history = []

    #updates both the leader_board and match_history
    def update_tournament(self, p1, p2, w, s1, s2):

        #creates the history item based on the match details
        history_item = ScorekeeperHistoryItem.ScorekeeperHistoryItem(p1, p2, w, s1, s2)

        #adds the history item to match_history[]
        self.match_history.append(history_item)

        #creates the list_items for both players and checks to see if they are on the leader_board
        #if not present on the leader board, they are appended
        list_item_a = ScoreKeeperListItem.ScorekeeperListItem(p1)
        list_item_b = ScoreKeeperListItem.ScorekeeperListItem(p2)
        if self.check_player(list_item_a):
            self.leader_board.append(list_item_a)
        if self.check_player(list_item_b):
            self.leader_board.append(list_item_b)

        #Checks the winner and awards a point to that player
        if s1 > s2:
            self.make_winner(p1)
        elif s2 > s1:
            self.make_winner(p2)
        #in the unlikely event of a tie, no points awarded
        else:
            pass

    #checks to see if the player is already on the leader board.
    #returns true if they are not, false if they are.
    def check_player(self, player):
        check = True
        for i in range(len(self.leader_board)):
            if self.leader_board[i] == player.get_player():
                check = False
            else:
                check = True
        return check

    #update the winner's score
    def make_winner(self, player):
        for i in range(len(self.leader_board)):
            if player is self.leader_board[i]:
                player.update_score()

    #returns this leader_board
    def get_leader_board(self):
        return self.leader_board

    #returns this match_history
    def get_match_history(self):
        return self.match_history