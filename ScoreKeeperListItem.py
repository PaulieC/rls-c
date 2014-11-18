__author__ = 'jeffrey creighton & anad patel'
#Purpose: data structure for tracking tournament leaders

class ScorekeeperListItem:
    def __init__(self, player):
        self.player = player
        self.score = 0

    #increment this player's score to signify a win
    def update_score(self):
        self.score = self.score + 1

    def get_score(self):
        return self.score

    def get_player(self):
        return self.score