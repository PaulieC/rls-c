"""
This class will act like the game administrator. It should be connected by the person handling the
tournament. This 'player' will manage the current tournament, game, number of players, etc...
"""
__author__ = 'system2'
from ClientPackage.GameMasterClient import *
from ClientPackage.GMPlayer import *
import time

my_player = GMPlayer()
client = GameMasterClient(my_player)
# attempt to game controller to the server room
client.client_connect()
# verify connection
client.verify_connection()
# register player
client.register_player()
# request a verification that this player has been registered to the tournament
client.verify_registration()
# TODO set the tournament style
client.set_tournament()
# TODO set the game to play
time.sleep(15)
# close the connection
client.close_connection()