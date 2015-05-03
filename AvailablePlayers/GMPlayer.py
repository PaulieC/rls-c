__author__ = "Paul Council, Anand Patel"
__version__ = "sprint1"
__credits__ = ["William Ezekiel"]


# imports
from ClientPackage import Player


class GMPlayer(Player.Player):
    """

    Player class

    Attributes:
        past_moves: a list of the past moves performed by this player for the current match
        opp_moves: a list of the past moves performed by the opponent for the current match
        win_record: a list of wins/losses; 1 = win, 0 = loss
        player_number: the player number for the current round
        opp_number: the opponent's number for the current round
        name: this Player's name
    """

    def __init__(self):
        """
        Initializes the player's class fields
        All lists are set to an empty value and
        the player/opp numbers should be negative
        """
        Player.Player.__init__(self)
        self.past_moves = []
        self.opp_moves = []
        self.win_record = []
        self.player_number = -1
        self.opp_number = -1
        self.name = "Game Master"

    def play(self):
        """
        Returns the value calculated by
        the class function strategy()
        :return self.strategy: The selected move
        :rtype: int
        """
        return self.strategy()

    def reset(self):
        """Calls all of the clear functions
        for this player's lists. This is needed
        to ensure that the strategy is accurate
        for the next match
        """
        self.clear_opp_moves()
        self.clear_past_moves()
        self.clear_win_record()

    def notify(self, message):
        """
        Performs actions based on the information
        received when this function is called externally.

        If the match is over, this player should reset
        itself to prepare for another match.

        If the round is over, this player should take
        the information available from the passed message
        and add wins/losses to its fields.
        :param message: A message Object
        :type message: Message
        """
        if message.is_match_end_message():
            # Match is over. Reset lists
            self.reset()
        elif message.is_round_end_message():
            # round is over. Evaluate events
            players = message.get_players()
            # Checks to see if this player is involved in the current message
            player_result = self.check_for_players(players)
            if player_result:
                temp_moves, winner = message.get_info()
                # now update information for both player's moves
                self.game_move_updates(temp_moves, winner)

    def game_move_updates(self, round_moves, winning_player):
        """
        Called in the notify function. This function
        discovers if the past round was a win/loss for
        this player and adds the appropriate information
        to the player lists and opponent's lists accordingly
        :param round_moves: The moves tuple retrieved from the Message object
        :type round_moves: tuple
        :param winning_player: The player number of who won the round
        :type winning_player: int
        """
        # first, check if we are the winning player
        if winning_player == self.get_player_number():
            # WE WON!
            # Add our winning move to the list
            self.add_past_moves(round_moves[self.get_player_number() - 1])
            # Add opponent's losing move to the list
            self.add_opp_moves(round_moves[self.get_opp_number() - 1])
            # Keep track of winning this round
            self.add_win_record(1)
        # We know we are the losing player
        else:
            # WE LOST!!
            # Add opponent's winning move to the list
            self.add_opp_moves(round_moves[self.get_opp_number() - 1])
            # Add our losing move to the list
            self.add_past_moves(round_moves[self.get_player_number() - 1])
            # Keep track of losing this round
            self.add_win_record(0)

    def check_for_players(self, players):
        """Called in the notify function. This function
        figures out who the winner/loser is and sets
        the player's number to the number they are set
        to in the current match
        :param players: The players who played the last round
        :type players: list
        :return: True if this player was a part of the last round
        :rtype: bool
        """
        if players[0] == self:
            # We are player 1
            self.set_player_number(1)
            self.set_opp_number(2)
            return True
        elif players[1] == self:
            # We are player 2
            self.set_player_number(2)
            self.set_opp_number(1)
            return True
        else:
            return False

    def strategy(self):
        """
        Returns 0 for rock, 1 for paper and 2 for scissors
        past moves is a [blank] of you and your current opponent's
        previous moves in the current game.
        :return counter_play: 2 if this is the first move played for the
                              match. 0 - 3 depending on the predicted counter.
        :rtype: int
        """
        # first move "scissors" (2)
        if len(self.get_past_moves()) == 0:
            counter_play = 2
            # print counter_play
            return counter_play
        else:  # predict the next move and counter it
            counter_play = self.counter(self.predict(self.get_opp_moves()))
            # print counter_play
            return counter_play

    @staticmethod
    def predict(opp_mvs):
        """
        Find the count of your opponents
        previous moves and return the most likely move.
        :param opp_mvs: List of opponents previous moves
        :type opp_mvs: list
        :return: The index value calculated based on the previous moves played
        :rtype: int
        """
        play_count = []
        play_count.append(opp_mvs.count(0))  # rock
        play_count.append(opp_mvs.count(1))  # paper
        play_count.append(opp_mvs.count(2))  # scissors
        # Return most likely move.
        # Will need to change later if moves are not numbers.
        return play_count.index(max(play_count))

    @staticmethod
    def counter(opp_move):
        """
        given a predicted opponents move,
        return the counter play.
        :param opp_move: the opponent's move this turn
        :type opp_move: int
        :return: The number representing the play to make
        :rtype: int
        0 - rock
        1 - paper
        2 - scissors
        """
        if opp_move == 0:  # opponent plays rock
            return 1    # play paper
        elif opp_move == 1:  # opponent plays paper
            return 2    # play scissors
        else:
            return 0    # opponent plays scissors, play rock.

    """
    Getters and Setters follow
    """
    def set_name(self, player_name):
        """
        Sets this player's name
        :param player_name: The name to assign this player
        :type player_name: str
        """
        self.name = player_name

    def set_opp_number(self, num):
        """
        Sets the player number of the current opponent
        :param num: The number to assign the opponent
        :type num: int
        """
        self.opp_number = num

    def set_player_number(self, num):
        """
        Sets this player's number
        :param num: The number to assign this player
        :type num: int
        """
        self.player_number = num

    def clear_opp_moves(self):
        """ Empties the moves stored from the opponents past moves """
        self.opp_moves = []

    def clear_past_moves(self):
        """ Empties the moves stored from this player's past moves """
        self.past_moves = []

    def clear_win_record(self):
        """ Empties the wins stored from this player's history """
        self.win_record = []

    def get_name(self):
        """
        Returns this player's name
        :return name: The name of this player
        :rtype: str
        """
        return self.name

    def get_opp_number(self):
        """
        Returns the opponent's number
        :return opp_number: The opponent's player number
        :rtype: int
        """
        return self.opp_number

    def get_player_number(self):
        """
        Returns this player's number
        :return player_number: This player's number
        :rtype: int
        """
        return self.player_number

    def get_opp_moves(self):
        """
        Returns the list of opponent's previous moves
        :return opp_moves: The opponent's history
        :rtype: list
        """
        return self.opp_moves

    def get_past_moves(self):
        """
        Returns the list of this player's previous moves
        :return past_moves: The player's history
        :rtype: list
        """
        return self.past_moves

    def get_win_record(self):
        """
        Returns the list of wins/loses for this player
        :return win_record: The player's win/loss history
        :rtype: list
        """
        return self.win_record

    def add_past_moves(self, move):
        """
        Appends the parameter to the list of this player's past moves.
        :param move: The move that this player has recently made
        :type move: int
        """
        self.past_moves.append(move)

    def add_opp_moves(self, move):
        """
        Appends the parameter to the list of the opponent's past moves.
        :param move: The move that the opponent has recently made
        :type move: int
        """
        self.opp_moves.append(move)

    def add_win_record(self, result):
        """
        Appends the parameter to the list of this player's win/loss record
        :param result: 1 - win; 0 - lose
        :type result: int
        """
        self.win_record.append(result)