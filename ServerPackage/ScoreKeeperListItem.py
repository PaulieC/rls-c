__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["jeffrey creighton"]


class ScorekeeperListItem:
    """
    Purpose: data structure for tracking tournament leaders

    Attributes:
        player: the player who this item is associated with
        score: the current score for the associated player
    """

    def __init__(self, player):
        """
        :param player: the player to register with this score item
        :type player: Player.Player
        """
        self.player = player
        self.score = 0

    def update_score(self):
        """ increment this player's score to signify a win """
        self.score += 1

    def get_score(self):
        """
        returns this score
        :return: the current score
        :rtype: int
        """
        return self.score

    def get_player(self):
        """
        returns this player
        :return: the player that this object is associated with
        :rtype: Player.Player
        """
        return self.player