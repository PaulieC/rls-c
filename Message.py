__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["geebzter"]


class Message(object):
    """
    Defines message types for standard framework message
    Provides free (global) functions that help create standard messages
    such as get_round_end_message etc.
    Message types:
        Defines standard types of messages that are broadcast within the game.
    Attributes:
        msg_type: an integer determining the type of message sent
        self.players: the players that the message can correspond to
        self.info: additional information that could be set
    """
    Tournament_Start = 1
    Tournament_End = 2
    Match_Start = 3
    Match_End = 4
    Round_Start = 5
    Round_End = 6

    '''
    Different types of message builders
    These are static methods, so use them like this:
    m = Message.get_match_start_message(players)
    '''

    @staticmethod
    def get_match_start_message(players):
        """
        Creates the start of the match message
        :param players: the players that are in the match
        :type players: list
        :return: returns the match start message
        :rtype: Message
        """
        return Message.create_message(Message.Match_Start, players)

    @staticmethod
    def get_match_end_message(players, result):
        """
        Result format: tuple (wins for each player) eg. (2, 4) means first player won 2, second won 4
        :param players: a list of players that this message corresponds to
        :type players: list
        :param result: additional information
        :type result: str
        :return: returns the end message
        :rtype: Message
        """
        return Message.create_message(Message.Match_End, players, result)

    @staticmethod
    def get_round_start_message(players):
        """
        Creates the start of the round message
        :param players: players in the current round
        :type players: list
        :return: returns the start round message
        :rtype: Message
        """
        return Message.create_message(Message.Round_Start, players)

    @staticmethod
    def get_round_end_message(players, moves, result):
        """
        moves is a tuple. For eg. (2,1) means first player played scissors and the second played paper
        result is 0 if tied, 1 if first player won and 2 if second player won
        :param players: the players in the round
        :type players: list
        :param moves: the moves that the players made
        :type moves: list
        :param result: additional message concerning the round
        :type result: str
        :return: returns the end of round message
        :rtype: Message
        """
        info = (moves, result)
        return Message.create_message(Message.Round_End, players, info)

    def __init__(self, msg_type):
        self.msg_type = msg_type
        self.players = None
        self.info = None

    def set_players(self, players):
        """
        Set players in a players related message such as GameEnd
        :param players: the players
        :type players: list
        """
        self.players = players

    def get_players(self):
        """
        Returns players relating to the message
        :return: the players
        :rtype: list
        """
        return self.players

    def set_info(self, info):
        """
        Set additional information, such as the result of a match etc,
        that needs to be transported with the message
        :param info: the additional information
        :type info: tuple
        """
        self.info = info

    def get_info(self):
        """
        Returns the information stored in the message
        :return: the information set to this instance
        :rtype: tuple
        """
        return self.info

    def is_tournament_start_message(self):
        """
        Whether the message is a start of tournament notification
        :return: True if message is a start of tournament notification, False otherwise
        :rtype: bool
        """
        return self.msg_type == Message.Tournament_Start

    def is_tournament_end_message(self):
        """
        Whether the message is an end of tournament notification
        :return: True if message is an end of tournament notification, False otherwise
        :rtype: bool
        """
        return self.msg_type == Message.Tournament_End

    def is_match_start_message(self):
        """
        Whether the message is a start of match notification
        :return: True if message is a start of match notification, False otherwise
        :rtype: bool
        """
        return self.msg_type == Message.Match_Start

    def is_match_end_message(self):
        """
        Whether the message is a end of match notification
        :return: True if the message is a end of match notification, False otherwise
        :rtype: bool
        """
        return self.msg_type == Message.Match_End

    def is_round_start_message(self):
        """
        Whether the message is a start of round notification
        :return: True if the message is a start of round notification, False otherwise
        :rtype: bool
        """
        return self.msg_type == Message.Round_Start

    def is_round_end_message(self):
        """
        Whether the message is a end of round notification
        :return: True if the message is a end of round notification, False otherwise
        :rtype: bool
        """
        return self.msg_type == Message.Round_End

    @staticmethod
    def create_message(msg_type, players=None, info=None):
        """
        Helper method that builds different kinds of messages
        :param msg_type: Message type
        :type msg_type: int
        :param players: Players involved in the message if any
        :type players: list
        :param info: Additional information that is contained in the message,
                     such as the moves made in a game and the result etc...
        :type info: tuple
        :return m: the message that is created
        :rtype m: Message
        """
        m = Message(msg_type)
        m.set_players(players)
        m.set_info(info)
        return m



