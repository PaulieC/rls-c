#################################################
# 
# Game designed to work with RPSFramework
# Created by Matt Martorana + Justin Read
#
#################################################

class Game (Object):
    listPlayers = []

    listRules = []

    listMoves = []

    # Need to get list of Players involved
    # All we need is to pass in a list of players involved and
    # a list for their moves respectively
    def get_players(self, playerList, moveList):
        listPlayers = playerList
        listMoves = moveList

    # Need a list of valid moves, most likely way will be
    # ['rock>scissors','scissors>paper','paper>rock']
    # or other simple boolean statements
    #
    def get_rules(self, ruleList):
        listRules = ruleList


    # need method to determine winners
    def determine_winner(self, moves):
        # child of this class will have to figure out how winners
        # are determined using the listRules, listMoves
        #
        # Also take note, eval('string') evaluates string as if it were
        # a boolean or mathematic expression, and exec('string')
        # executes the string as if it were exact python code.
        #
        # Don't forget an elimination process if move is illegal
        # 
        # @return String array of winner(s) and move is preferable
        pass
