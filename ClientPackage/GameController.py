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
client.client_connect()
# verify connection
client.verify_connection()
# open the tournament for registration

# TODO set the tournament style
# client.set_tournament()
# TODO set the game to play
# client.set_game()
# open the room for registration
client.open_tournament_registration()
time.sleep(60)  # allow 1 minute for registration
# close the room for registration
client.close_tournament_registration()

# close the connection
client.close_connection()