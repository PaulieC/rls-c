"""
This class will act like the game administrator. It should be connected by the person handling the
tournament. This 'player' will manage the current tournament, game, number of players, etc...
"""
__author__ = 'Paul Council'
import time

from ClientPackage.GameMasterClient import *
from AvailablePlayers.GMPlayer import *


my_player = GMPlayer()
client = GameMasterClient(my_player)
# attempt to connect game controller to the server room
client.client_connect(host="192.168.1.25")

# verify connection
client.verify_connection()

# TODO set the tournament style
# client.set_tournament()

# TODO set the game to play
# client.set_game()

# open the room for registration
client.open_tournament_registration()
# time.sleep(10)  # allow 1 minute for registration before closing

# close the room for registration
# client.close_tournament_registration()

# get list of ready players
client.list_registered_players()

# create pairs of matches server side. Should be empty at this stage
client.check_for_ready_pairs()

# generate ready pairs for a match
client.find_next_match()

# close the connection
client.close_connection()