__author__ = 'Tony'

from TournamentService import *
from RPSPlayerExample import *
from RPSGame import *
from Display import *

# Create a tournament service that will set the tournament accordingly, register the players to the tournament
# and run the instance of Tournament
class RPSDriver(TournamentService):

    def __init__(self):
        TournamentService.__init__(self)

    def register_players(self, player_list):
        for player in player_list:
            self.register_player(player)

if __name__ == "__main__":
    driver = RPSDriver()
    player = RPSPlayerExample()
    opponent = RPSPlayerExample()
    players = [player,opponent]
    rps = RPSGame()
    driver.register_players(players)
    driver.set_game(rps)
    driver.set_display(Display())
    driver.run()










