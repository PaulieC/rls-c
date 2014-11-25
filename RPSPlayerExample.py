__author__ = 'geebzter'

# Example of how to implement an RPS player within the framework

import Player
import Message

class RPSPlayerExample(Player.Player):

    def __init__(self):
        # Call super class constructor
        Player.Player.__init__(self)
        self.reset()

    def play(self):
        return RpsPlayingStrategy.play(self.opponents_moves)

    def reset(self):
        self.opponents_moves = []

    def get_name(self):
        return "Minimizer"

    def notify(self, msg):

        # We use notifications to store opponent's moves in past rounds
        # Process match-start and round-end messages
        # At the start of the match, clear opponent moves history since a new match has started
        # At the end of a round, append move to opponent's move history. Move history is used
        # to compute the next move played.
        if msg.is_match_start_message():
            players = msg.get_players()
            if players[0] == self or players[1] == self:
                self.reset()
        elif msg.is_round_end_message():
            players = msg.get_players()
            # Check if this message is for me and only then proceed
            if (players[0] == self) or (players[1] == self):
                # In this case, (by convention) the info is a tuple of the moves made and result e.g. ((1, 0), (1,0)) which
                # means player 1 played paper (1), the player 2 played rock(0) and the result was that
                # player 1 won (got 1 point) and player 2 lost (got 0 point)

                moves, result = msg.get_info()

                # RPS is a two person game; figure out which of the players is me
                # and which one is the opponent
                if players[0] == self:
                    opponent = 1
                else:
                    opponent = 0

                # Update opponent's past moves history
                self.opponents_moves.append(moves[opponent])



# An implementation of a simple rps playing strategy
class RpsPlayingStrategy(object):

    @staticmethod
    def play(opponents_moves):
        # Implements some way of predicting what the opponent might do next
        # and play accordingly.
        # For instance, assume he is going to play the move he has played the
        # least.

        # count number of rock, paper and scissors moves made in the past
        count = [0, 0, 0]

        for move in opponents_moves:
            count[move] += 1

        if count[0] < count[1]:
            least = 0
        else:
            least = 1

        if count[least] > count[2]:
            least = 2

        # Assuming that opponent's move is going to be the value of least, play to beat it
        return (least + 1) % 3

# Test driver
# Run by typing "python3 RpsPlayerExample.py"

if __name__ == "__main__":
    player = RPSPlayerExample()
    opponent = RPSPlayerExample()
    players = [opponent,player]
    fakemoves = (1,2)
    fakeresult = (0,1)

    player.notify(Message.Message.get_match_start_message(players))
    player.notify(Message.Message.get_round_start_message(players))
    move = player.play()
    print ("Move played: ", move)
    player.notify(Message.Message.get_round_end_message(players,fakemoves,fakeresult))
















