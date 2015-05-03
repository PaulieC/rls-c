__author__ = "Paul Council, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Victor M"]

# imports
import random

from ClientPackage import Player


class RPSPlayerSwitcharoo(Player.Player):
    """
    Rock paper scissors player

    Attributes:
        strategy: An object designed to calculate/manipulate this player's strategy
    """

    def __init__(self):
        # Call super class constructor
        Player.Player.__init__(self)
        self.strategy = RPSOppositeStrategy()
        self.reset()

    def reset(self):
        """ Clears the list of opponent's previous moves """
        self.opponents_moves = []

    def get_name(self):
        """
        Gets the name of this player
        :return: The player's name
        :rtype: str
        """
        return "Switch-a-roo"

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
            players = msg.get_players()
            if players[0] == self or players[1] == self:
                self.reset()
        elif msg.is_round_end_message():
            players = msg.get_players()
            # Check if this message is for me and only then proceed
            if (players[0] == self) or (players[1] == self):
                # In this case, (by convention) the info is a tuple of the moves made and result e.g. ((1, 0), 1) which
                # means player 1 played paper (1), the player 2 played rock(0) and the result was that
                # player 1 won

                moves, result = msg.get_info()

                # RPS is a two person game; figure out which of the players is me
                # and which one is the opponent
                if players[0] == self:
                    opponent = 1
                else:
                    opponent = 0

                # Update opponent's past moves history
                self.opponents_moves.append(moves[opponent])

    def play(self):
        """
        Calculates the next move that the player should make, then returns this.
        :return: The calculated move
        :rtype: int
        """
        self.decide_strategy(self.opponents_moves)
        return self.strategy.make_move(self.opponents_moves)

    def set_strategy(self, new_strategy):
        """
        Allows this player's strategy to be changed
        :param new_strategy: The new strategy to set to this player
        :type new_strategy: object
        """
        self.strategy = new_strategy

    def decide_strategy(self, opponents_moves):
        """
        Randomly sets a strategy
        :param opponents_moves: the list of the opponent's moves
        :type opponents_moves: list
        """
        # No prior opponent moves to learn from so random.
        if not opponents_moves:
            self.set_strategy(RPSRandomStrategy)
        else:
            strategies = [RPSOppositeStrategy, RPSLeastUsedStrategy, RPSMostUsedStrategy, RPSRandomStrategy]
            self.set_strategy(random.choice(strategies))


class RPSRandomStrategy(object):
    """ Random move """

    @staticmethod
    def make_move():
        """
        Returns a random move for this turn
        :return: a random int between 0 and 2 (inclusive)
        :rtype: int
        """
        return random.randint(0, 2)


class RPSOppositeStrategy(object):
    """
    Chose what beats the last played move by the opponent.
    Weak in that it's an easy-to-spot pattern.
    """

    @staticmethod
    def make_move(opponents_moves):
        """
        Returns a move based on the list of opponent's previous move
        :param opponents_moves: the list of opponent's moves
        :type opponents_moves: list
        :return: the move to make
        :rtype: int
        """
        if opponents_moves[-1] == 0:
            return 1
        elif opponents_moves[-1] == 1:
            return 2
        elif opponents_moves[-1] == 2:
            return 0


class RPSLeastUsedStrategy(object):
    """
    Determine the least picked by the opponent and play the choice that would beat the least picked by opponent.
    The logic being that the opponent will not expect you to expect the least picked hand.
    Weak against players who repeatedly choose the same thing.
    Taken from https://github.com/geebzter/game-framework/blob/master/RPSPlayerExample.py
    """

    @staticmethod
    def make_move(opponents_moves):
        """
        Implements some way of predicting what the opponent might do next
        and play accordingly.
        For instance, assume he is going to play the move he has played the
        least.

        count number of rock, paper and scissors moves made in the past

        :param opponents_moves: the list of opponent's previous moves
        :type opponents_moves: list
        :return: the determined move to use
        :rtype: int
        """
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


class RPSMostUsedStrategy(object):
    """
    Determine most picked by the opponent and play the choice that would beat the most picked.
    Strong against players who tend to play the same hand
    reworked https://github.com/geebzter/game-framework/blob/master/RPSPlayerExample.py
    """

    @staticmethod
    def make_move(opponents_moves):
        """
        Implements some way of predicting what the opponent might do next
        and play accordingly.
        For instance, assume he is going to play the move he has played the
        least.

        count number of rock, paper and scissors moves made in the past
        :param opponents_moves: the list of the opponent's previous moves
        :type opponents_moves: list
        :return: the determined move to make
        :rtype: int
        """

        count = [0, 0, 0]

        for move in opponents_moves:
            count[move] += 1

        if count[0] > count[1]:
            most = 0
        else:
            most = 1

        if count[most] < count[2]:
            most = 2

        # Assuming that opponent's move is going to be the value of most, play to beat it
        return (most + 1) % 3