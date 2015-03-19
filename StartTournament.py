__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

"""
This file should fully replace the RPSDriver.py file and RPSDriver.py class
after it is fully implemented.

The players should connect through the TournamentServer and these objects should be retrieved
and registered in the TournamentService.
"""

# imports
from RPSPlayerExample import *
from RPSGame import *
from Display import *
from BEPCPlayer import *
from TournamentServer import *
from PlayerClient import *
from TournamentService import *

# sets up a basic game with networking
if __name__ == "__main__":
    # initialize objects
    tournament_events = TournamentService()
    server = ServerObject()
    client = ClientObject()
    player = RPSPlayerExample()
    opponent = BEPCPlayer()

    # execute
    players = [player, opponent]
    rps = RPSGame()
    tournament_events.register_players(players)
    tournament_events.set_game(rps)
    tournament_events.set_display(Display())
    tournament_events.run()