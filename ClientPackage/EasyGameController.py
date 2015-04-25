__author__ = 'Anand'
"""
This class will act like the game administrator. It should be connected by the person handling the
tournament. This 'player' will manage the current tournament, game, number of players, etc...
"""
__author__ = 'Paul Council'
import time

from ClientPackage.GameMasterClient import *
from AvailablePlayers.GMPlayer import *
from AvailablePlayers.TestPlayer1 import *
from AvailablePlayers.BEPCPlayer import  *
from AvailablePlayers.TestPlayer2 import *


HOST = "150.250.190.192"
my_player = GMPlayer()
game_controller = GameMasterClient(my_player)
# player1 = TestPlayer1()
# player2 = TestPlayer1()
# client1 = PlayerClient(player1)
# client2 = PlayerClient(player2)
# attempt to connect game controller to the server room
game_controller.client_connect(host=HOST)
# client1.client_connect(host=HOST)
# client2.client_connect(host=HOST)
#
# verify connection
game_controller.verify_connection()
# client1.verify_connection()
# client2.verify_connection()
# TODO set the tournament style
# game_controller.set_tournament()

# TODO set the game to play
# game_controller.set_game()

# open the room for registration
game_controller.open_tournament_registration()
# time.sleep(10)  # allow 1 minute for registration before closing
# client1.register_player()
# client2.register_player()

# client1.verify_registration()
# client2.verify_registration()
# close the room for registration
# game_controller.close_tournament_registration()

game_controller.set_game_status(True)

game_controller.get_game_status()
time.sleep(5)
# get list of ready players
game_controller.list_registered_players()

# create player pairs based on ID
# game_controller.create_match_pairs()

time.sleep(5)
game_controller.create_all_available_matches()
time.sleep(2)


# client1.submit_move()
# #time.sleep(2)
# client2.submit_move()
#
# time.sleep(2)
#
# #this was being called above and it wasn't working
# #game_controller.create_match_pairs()
#
# # generate all matches we can using the player_id pairs from above
# # game_controller.create_all_available_matches()
# time.sleep(2)
# #time.sleep(15)
#
# # run all ready matches
# game_controller.run_available_matches()
#
#
# client1.get_round_results()
# client2.get_round_results()

#for x in range(0,6):
#client1.submit_move()
#client2.submit_move()
    #time.sleep(2)
    #game_controller.run_available_matches()
    #time.sleep(2)
    #client1.get_round_results()
    #client2.get_round_results()
    #time.sleep(2)

# close the connection
game_controller.close_connection()
# client1.close_connection()
# client2.close_connection()
