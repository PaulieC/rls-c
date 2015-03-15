__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Tony"]

# imports
from TournamentService import *
from RPSPlayerExample import *
from RPSGame import *
from Display import *
from BEPCPlayer import *


class RPSDriver(TournamentService):
    """
    Create a tournament service that will set the tournament accordingly, register the players to the tournament
    and run the instance of Tournament
    """

    def __init__(self):
        TournamentService.__init__(self)

    def register_players(self, player_list):
        """
        Registers the Player objects that exist in the player_list
        :param player_list: the collected list of players to register
        :type player_list: list
        """
        for plr in player_list:
            self.register_player(plr)

# sets up a basic game
if __name__ == "__main__":
    driver = RPSDriver()
    player = RPSPlayerExample()
    opponent = BEPCPlayer()
    players = [player, opponent]
    rps = RPSGame()
    driver.register_players(players)
    driver.set_game(rps)
    driver.set_display(Display())
    driver.run()










