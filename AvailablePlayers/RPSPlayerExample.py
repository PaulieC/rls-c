__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["geebzter"]

# imports
from ServerPackage import Message
from ClientPackage import Player


class RPSPlayerExample(Player.Player):
    """
    Example of how to implement an RPS player within the framework

    Attributes:
        opponents_moves: the list of moves that the opponent has played
    """

    def __init__(self):
        """ Call super class constructor """
        Player.Player.__init__(self)
        self.reset()

    def play(self):
        """
        Executes the strategy of this player
        :return: The calculated move for this player
        :rtype: int
        """
        return RpsPlayingStrategy.play(self.opponents_moves)

    def reset(self):
        """ Clears the list of moves that the opponent has played """
        self.opponents_moves = []

    def get_name(self):
        return "Minimizer"

    def notify(self, msg):
        """
        We use notifications to store opponent's moves in past rounds
        Process match-start and round-end messages
        At the start of the match, clear opponent moves history since a new match has started
        At the end of a round, append move to opponent's move history. Move history is used
        to compute the next move played.
        :param msg: the message that will be sent upon Observer moments
        :type msg: Message.Message
        """
        if msg.is_match_start_message():
            player_list = msg.get_players()
            if player_list[0] == self or player_list[1] == self:
                self.reset()
        elif msg.is_round_end_message():
            player_list = msg.get_players()
            # Check if this message is for me and only then proceed
            if (player_list[0] == self) or (player_list[1] == self):
                # In this case, (by convention) the info is a tuple of the moves made and result
                # e.g. ((1, 0), (1,0)) which means player 1 played paper (1), the player 2 played
                # rock(0) and the result was that player 1 won (got 1 point) and player 2 lost (got 0 point)

                moves, result = msg.get_info()

                # RPS is a two person game; figure out which of the players is me
                # and which one is the opponent
                if player_list[0] == self:
                    opponent_name = 1
                else:
                    opponent_name = 0

                # Update opponent's past moves history
                self.opponents_moves.append(moves[opponent_name])


class RpsPlayingStrategy(object):
    """ An implementation of a simple rps playing strategy """

    @staticmethod
    def play(opponents_moves):
        """
        Implements some way of predicting what the opponent might do next
        and play accordingly.
        For instance, assume he is going to play the move he has played the least.
        :param opponents_moves: the list of of the opponent's past moves
        :return: the calculated move to make
        :rtype: int
        """

        # count number of rock, paper and scissors moves made in the past
        count = [0, 0, 0]

        for opp_move in opponents_moves:
            count[opp_move] += 1

        if count[0] < count[1]:
            least = 0
        else:
            least = 1

        if count[least] > count[2]:
            least = 2

        # Assuming that opponent's move is going to be the value of least, play to beat it
        return (least + 1) % 3

# Test driver
# Run by typing "python2 RpsPlayerExample.py"
if __name__ == "__main__":
    player = RPSPlayerExample()
    opponent = RPSPlayerExample()
    players = [opponent, player]
    fake_moves = [1, 2]
    fake_result = [0, 1]

    player.notify(Message.Message.get_match_start_message(players))
    player.notify(Message.Message.get_round_start_message(players))
    move = player.play()
    print "Move played: ", move
    player.notify(Message.Message.get_round_end_message(players, fake_moves, fake_result))