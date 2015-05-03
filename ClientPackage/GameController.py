"""
This class will act like the game administrator. It should be connected by the person handling the
tournament. This 'player' will manage the current tournament, game, number of players, etc...
"""
__author__ = "Paul Council, Anand Patel"
__version__ = "sprint5"

import time

from ClientPackage.GameMasterClient import *
from AvailablePlayers.GMPlayer import *


my_player = GMPlayer()
client = GameMasterClient(my_player)
# attempt to connect game controller to the server room
client.client_connect(host="150.250.190.253")

# verify connection
client.verify_connection

# TODO set the tournament style
# client.set_tournament()

# TODO set the game to play
# client.set_game()

# open the room for registration
client.open_tournament_registration()
# time.sleep(10)  # allow 1 minute for registration before closing

# close the room for registration
# client.close_tournament_registration()

client.set_game_status(True)

client.get_game_status()
# get list of ready players
client.list_registered_players()

# create player pairs based on ID
client.create_match_pairs()

# generate all matches we can using the player_id pairs from above
# client.create_all_available_matches()

# run all ready matches
client.run_available_matches()

# close the connection
client.close_connection()