__author__ = 'jeffrey creighton & anad patel'
#Purpose: to collect and store scores from all players and matches

import ScorekeeperHistoryItem
import ScoreKeeperListItem

class Scorekeeper:
    leaderboard = []
    matchhistory = []

    def __init__(self):
        self.leaderboard = []
        self.matchhistory = []

        def update_tournament(self, p1, p2, w, s1, s2):

            historyitem = ScorekeeperHistoryItem(p1, p2, w, s1, s2)

            self.matchhistory.append(historyitem)


            listitemA = ScoreKeeperListItem(p1, s1)
            listitemB = ScoreKeeperListItem(p2, s2)
            if(check_player(listitemA)):
                self.leaderboard.append(listitemA)
            if(check_player(listitemB)):
                self.leaderboard.append(listitemB)

            if(s1 > s2):
                make_winner(p1)
            elif(s2 > s1):
                make_winner(p2)
            #in the unlikely event of a tie, no points awarded
            else:
                pass



        def check_player(self, item):
            check = True
            for i in range(len(self.leaderboard)):
                if (i.get_player() == item.get_player()):
                    check = False
                else:
                    check = True
            return check

        #update the winner's score
        def make_winner(self, player):
            for i in range(len(self.leaderboard)):
                if(player is i.get_player()):
                    i.update_score()
