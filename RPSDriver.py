__author__ = 'Tony'

from TournamentService import *
from AllPlayAll import *
from RPSPlayerExample import *
from RPSGame import *

# Create a tournament service that will set the tournament accordingly, register the players to the tournament
# and run the instance of Tournament
class RPSDriver(TournamentService.TournamentService):

    def __init__(self):
        self.tournament
        self.game

    def set_tournament(self, tournament_type):
        pass

    def register_player(self, player):
        pass

    def register_players(self, player_list):
        for player in player_list:
            self.register_player(self,player)

    def set_game(self, game):
        pass


if __name__ == "__main__":
    driver = RPSDriver()
    player = RPSPlayerExample()
    opponent = RPSPlayerExample()
    players = [player,opponent]
    rps = RPSGame()
    driver.register_players(players)
    driver.set_game(rps)
    driver.set_tournament(AllPlayAll)
    driver.tournament.run()










