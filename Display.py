__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Tara Crittenden"]

# imports
import Observer
from Message import *


class Display(Observer.Observer):
    """
    Displays the state of the game in a simple text format.
    """

    def notify(self, msg):
        """
        Determine which method to display
        :param msg: the message object to handle for output
        :type msg: Message
        """
        if msg.is_tournament_start_message():
            # start of a tournament
            self.display_start_tournament(msg)
        elif msg.is_tournament_end_message():
            # end of a tournament
            self.display_end_tournament(msg)
        elif msg.is_match_start_message():
            # start of a match
            self.display_start_match(msg)
        elif msg.is_match_end_message():
            # end of a match
            self.display_end_match(msg)
        elif msg.is_round_start_message():
            # start of a round
            self.display_start_round(msg)
        elif msg.is_round_end_message():
            # end of a round
            self.display_end_round(msg)
        else:
            print "Unknown message type"

    @staticmethod
    def indent_cushion():
        """ Provides easy readability """
        for i in range(4):
            print "+"

    @staticmethod
    def get_move(made_move):
        """
        Helper method for deconstructing the info portion of a end round message
        Returns the char representation of the move
        :param made_move: move that was made in int form
        :type made_move: int
        :return: move that was made in char form
        :rtype: int
        """
        if made_move == 0:
            return 'Rock'
        elif made_move == 1:
            return 'Paper'
        elif made_move == 2:
            return 'Scissors'

    def display_start_tournament(self, msg):
        """
        Display the start of a tournament
        :param msg: message to be displayed
        :type msg: Message
        """
        self.indent_cushion()
        print "Tournament Start! "
        self.indent_cushion()
        m = Message.get_players(msg)
        print "\nPlayers: " + m
        # assuming for the time being that info will hold the specified game
        m = Message.get_info(msg)
        print "\nGame: " + m

    def display_end_tournament(self, msg):
        """
        Display the end of a tournament
        :param msg: message to be displayed
        :type msg: Message
        """
        self.indent_cushion()
        print "Tournament End! "
        self.indent_cushion()
        # assuming for the time being that info will hold the winner of the tournament
        m = Message.get_info(msg)
        print "\nWinner: " + m
        self.indent_cushion()
        self.indent_cushion()
        print "\n"
        self.indent_cushion()
        self.indent_cushion()

    def display_start_match(self, msg):
        """
        Display the start of a match
        :param msg: message to be displayed
        :type msg: Message
        """
        self.indent_cushion()
        print "Match Start! "
        self.indent_cushion()
        players = Message.get_players(msg)
        print "\nPlayers: "
        for player in players:
            print player.get_name()

    def display_end_match(self, msg):
        """
        Display the end of a match
        :param msg: message to be displayed
        :type msg: Message
        """
        self.indent_cushion()
        print("Match end!")

        # TODO fix
        """
        self.indent_cushion()
        print " Match End! "
        self.indent_cushion()
        m = Message.get_info(msg)
        #r is the winner
        #winnings is the number of times that r won
        if m[1] > m[2]:
            #player 1 won
            r = 'Player 1 '
            winnings = m[1]
        else:
            #player 2 won
            r = 'Player 2 '
            winnings = m[2]
        print "Winner: " + r + "( " + winnings + " out of " + (m[1] + m[2]) + ")"
        """

    @staticmethod
    def display_start_round(msg):
        """
        Display the start of a round
        :param msg: message to be displayed
        :type msg: Message
        """
        pass    # TODO This needs to be implemented

    def display_end_round(self, msg):
        """
        Display the end of a round
        :param msg: message to be displayed
        :type msg: Message
        """
        print "\nRound Results: "
        m = Message.get_info(msg)
        # r is the winner of the round
        if m[1] == (0, 0):
            r = "Tied"
        elif m[1] == (1, 0):
            # player 1 won
            r = "Player 1 "
        # elif m[1] == (0,1):
        else:
            # player 2 won
            r = "Player 2 "
        print "Winner: " + r
        # find the moves that were played during this round
        moves = m[0]
        a = self.get_move(moves[0])
        b = self.get_move(moves[1])
        print "   Moves made: Player 1: " + a + " Player 2: " + b