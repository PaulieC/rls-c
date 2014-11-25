__author__ = 'Tara Crittenden'

# Displays the state of the game in a simple text format.

import Observer
import Message

class Display(Observer.Observer):

    #Determine which method to display
    def notify(self, msg):
        if msg.msgtype == 1:
            #start of a tournament
            display_start_tournament(msg)
        elif msg.msgtype == 2:
            #end of a tournament
            display_end_tournament(msg)
        elif msg.msgtype == 3:
            #start of a match
            display_start_match(msg)
        elif msg.msgtype == 4:
            #end of a match
            display_end_match(msg)
        elif msg.msgtype == 5:
            #start of a round
            display_start_round(msg)
        elif msg.msgtype == 6:
            #end of a round
            display_end_round(msg)
        else:
            print('Unknown message type')

    #Provides easy readiablity
    def indent_cushion():
        for i in range(8):
            print('+')


    #Helper method for deconstructing the info portion of a end round message
    #Returns the char representation of the move
    def get_move(mademove):
        """
        :param mademove: move that was made in int form
        :return: move that was made in char form

        """
        if mademove == 0:
            return 'Rock'
        elif mademove == 1:
            return 'Paper'
        elif mademove == 2:
            return 'Scissors'

    #Display the start of a tournament
    def display_start_tournament(msg):
        """
        :param msg: message to be displayed

        """
        indent_cushion()
        print(' Tournament Start! ')
        indent_cushion()
        m = Message.get_players(msg)
        print('\nPlayers: ' + m)
        #assuming for the time being that info will hold the specified game
        m = Message.get_info(msg)
        print('\nGame: ' + m)

    #Display the end of a tournament
    def display_end_tournament(msg):
        """
        :param msg: message to be displayed

        """
        indent_cushion()
        print(' Tournament End! ')
        indent_cushion()
        #assuming for the time being that info will hold the winner of the tournament
        m = Message.get_info(msg)
        print('\nWinner: ' + m)
        indent_cushion()
        indent_cushion()
        print('\n')
        indent_cushion()
        indent_cushion()

    #Display the start of a match        
    def display_start_match(msg):
        """
        :param msg: message to be displayed

        """
        indent_cushion()
        print(' Match Start! ')
        indent_cushion()
        m = Message.get_players(msg)
        print('\nPlayers: ' + m)

    #Display the end of a match       
    def display_end_match(msg):
        """
        :param msg: message to be displayed

        """
        indent_cushion()
        print(' Match End! ')
        indent_cushion()
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
        print('Winner: ' + r + '( ' + winnings + ' out of ' + (m[1] + m[2]) + ')')

    #Display the start of a round       
    def display_start_round(msg):
        """
        :param msg: message to be displayed

        """
        pass
    
    #Display the end of a round    
    def display_end_round(msg):
        """
        :param msg: message to be displayed

        """
        print('\nRound Results: ')
        m = Message.get_info(msg)
        #r is the winner of the round
        if m[2] == 0:
            r = 'Tied'
        elif m[2] == 1:
            #player 1 won
            r = 'Player 1 '
        elif m[2] == 1:
            #player 2 won
            r = 'Player 2 '
        print('Winner: ' + r)
        #find the moves that were played during this round
        moves = m[1]
        a = get_move(moves[1])
        b = get_move(moves[2])
        print('   Moves made: Player 1: ' + a + ' Player 2: ' + b)

    
