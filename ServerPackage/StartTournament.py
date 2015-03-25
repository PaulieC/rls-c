__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

"""
This file should fully replace the RPSDriver.py file and RPSDriver.py class
after it is fully implemented.

The players should connect through the TournamentServer and these objects should be retrieved
and registered in the TournamentService.
"""

# imports
from ServerPackage.TournamentServer import *

# sets up a basic game with networking
new_server = TournamentServer()
# set the tournament style
# set the game to play
# tournament_server.service.set_game(RPSGame)
# open connections
new_server.open_connection()
# run the tournament
