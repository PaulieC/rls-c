__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint2"

# imports
from ClientPackage.PlayerClient import *
from ClientPackage.BEPCPlayer import *
from ClientPackage.TestPlayer1 import *
import time

my_player = TestPlayer1()
client = PlayerClient(my_player)
# attempt to connect player to server
client.client_connect()
# verify connection
client.verify_connection()
# attempt to register this player in the tournament
client.register_player()
# request a verification that this player has been registered to the tournament
client.verify_registration()
# TODO keep connection open for 15 seconds
time.sleep(15)
# close the connection
client.close_connection()
