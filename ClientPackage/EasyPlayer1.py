__author__ = 'Anand'
"""
This class will act like the game administrator. It should be connected by the person handling the
tournament. This 'player' will manage the current tournament, game, number of players, etc...
"""
__author__ = 'Paul Council'
import time

from PlayerClient import *

from AvailablePlayers.TestPlayer1 import *




HOST = "150.250.190.192"


player1 = TestPlayer1()

client1 = PlayerClient(player1)

# attempt to connect game controller to the server room

client1.client_connect(host=HOST)
client1.verify_connection()
client1.register_player()
client1.verify_registration()
time.sleep(10)
client1.submit_move()
client1.close_connection()