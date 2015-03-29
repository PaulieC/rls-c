__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Samantha Holloway, Joe Pannizzo"]

# imports
from ServerPackage import Observer


class Player(Observer.Observer):
    """
    Class Player is used as the top level class abstraction to play in a Tournament
    It specifies what a concrete Player must do to be a part of the Tournament
    Each Player can be registered for a Tournament
    Concrete implementations of a Player will play against other ones playing
    the same game.
    Since there can be many player types for many games
    the AI for making moves in the 'play' function must be
    delegated to the concrete implementations that subclass Player.

    Ex: A Rock Paper Scissors Player that subclasses Player would
    define some AI in 'play' to return 'rock' 'paper or 'scissors'

    Attributes:
        name: The name to be assigned to this Player instance
    """

    def __init__(self):
        self.name = None
        self.id_num = None
        self.player_id = None

    def play(self):
        """
        play should be defined to return a move based on AI/Strategy,
        it takes in move history of opponent
        """
        pass

    def get_name(self):
        """ should be defined to return the Player instance variable 'name' """
        pass

    def set_name(self, player_name):
        """
        should be defined to set the Player instance variable name
        :param player_name: the name to be assigned to this player object
        :type player_name: str
        """
        self.name = player_name

    def get_method(self):
        """
        :return:
        """
        return self

    def set_id(self, num):
        """
        :param num:
        :return:
        """
        self.id_num = num
        self.player_id = self.name + "_" + str(self.id_num)

    def get_id_num(self):
        """
        :return:
        """
        return self.id_num

    def get_player_id(self):
        """
        :return:
        """
        return self.player_id