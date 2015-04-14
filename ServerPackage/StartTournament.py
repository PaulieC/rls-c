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
# get ip for connection
#new_server.generate_ip()
# set the port for the tournament: 12345
new_server.set_ip('150.250.142.57')
new_server.set_port(12345)
# create the server
new_server.create_server()
# open connections
new_server.open_connection()
# run the tournament
