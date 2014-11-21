#################################################
# 
# Game specification for the RPSFramework
#
# Created by Matt Martorana + Justin Read
#
#################################################

import Observer

class Game (Observer.Observer):


    def num_players_per_game(self):
        """
        Number of players in a game. Default setting is two-player games
        :return:
        """
        return 2

    def get_result(self, moves):
        """
        Computes the result for the given moves.
        :param moves: A tuple containing the moves made by the players
        :return: a tuple containing the result for the players
        """
        # child of this class will have to figure out how win/loss/tie
        # is determined moves
        #
        # Don't forget an elimination process if move is illegal
        # 
        # @return array of points given to each player
        pass

    def is_legal(self, move):
        """
        Checks if a given move is legal
        :param move: given move
        :return: True if the move is legal, false otherwise
        """
        pass

