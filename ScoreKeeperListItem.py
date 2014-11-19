__author__ = 'jeffrey creighton & anand patel'
# Purpose: data structure for tracking tournament leaders


class ScorekeeperListItem:
    def __init__(self, player):
        self.player = player
        self.score = 0

    #increment this player's score to signify a win
    def update_score(self):
        self.score += 1

    #returns this score
    def get_score(self):
        return self.score

    #returns this player
    def get_player(self):
        return self.player