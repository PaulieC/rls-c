__author__ = 'jeffrey creighton & anand patel'
# Purpose: to collect and store scores from all players and matches

import ScorekeeperHistoryItem
import ScoreKeeperListItem


class Scorekeeper:
    leaderboard = []
    matchhistory = []

    def __init__(self):
        self.leaderboard = []
        self.matchhistory = []

    #updates both the leaderboard and matchhistory
    def update_tournament(self, p1, p2, w, s1, s2):

        #creates the history item based on the match details
        historyitem = ScorekeeperHistoryItem.ScorekeeperHistoryItem(p1, p2, w, s1, s2)

        #adds the history item to matchhistory[]
        self.matchhistory.append(historyitem)

        #creates the listitems for both players and checks to see if they are on the leaderboard
        #if not present on the leader board, they are appended
        listitema = ScoreKeeperListItem.ScorekeeperListItem(p1, s1)
        listitemb = ScoreKeeperListItem.ScorekeeperListItem(p2, s2)
        if self.check_player(listitema):
            self.leaderboard.append(listitema)
        if self.check_player(listitemb):
            self.leaderboard.append(listitemb)

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
    def check_player(self, item):
        check = True
        for i in range(len(self.leaderboard)):
            if i.get_player() == item.get_player():
                check = False
            else:
                check = True
        return check

    #update the winner's score
    def make_winner(self, player):
        for i in range(len(self.leaderboard)):
            if player is i.get_player():
                i.update_score()

    #returns this leaderboard
    def get_leaderboard(self):
        return self.leaderboard

    #returns this matchhistory
    def get_matchhistory(self):
        return self.matchhistory