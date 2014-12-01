__author__ = 'geebzter'
# Defines message types for standard framework message
# Provides free (global) functions that help create standard messages
# such as get_round_end_message etc.

class Message(object):
    """
    Message types:
        Defines standard types of messages that are broadcast within the game.
    """
    Tournament_Start = 1
    Tournament_End = 2
    Match_Start = 3
    Match_End = 4
    Round_Start = 5
    Round_End = 6

    # Different types of message builders
    # These are static methods, so use them like this:
    # m = Message.get_match_start_message(players)

    @staticmethod
    def get_match_start_message(players):
        return Message.create_message(Message.Match_Start, players)

    @staticmethod
    def get_match_end_message(players, result):
        # result format: tuple (wins for each player) eg. (2, 4) means first player won 2, second won 4
        return Message.create_message (Message.Match_End, players, result)

    @staticmethod
    def get_round_start_message(players):
        return Message.create_message(Message.Round_Start, players)

    @staticmethod
    def get_round_end_message(players, moves, result):
        # moves is a tuple. For eg. (2,1) means first player played scissors and the second played paper
        # result is 0 if tied, 1 if first player won and 2 if second player won
        info = (moves, result)
        return Message.create_message(Message.Round_End, players, info)

    def __init__(self, msgtype):
        self.msgtype = msgtype
        self.players = None
        self.info = None

    def set_players(self, players):
        """
        Set players in a players related message such as GameEnd
        :param players: the players
        :return:
        """
        self.players = players

    def get_players(self):
        """
        Returns players in relating to the message
        :return:
        """
        return self.players


    def set_info(self, info):
        """
        Set additional information, such as the result of a match etc,
        that needs to be transported with the message
        :param info: the additional information
        :return:
        """
        self.info = info

    def get_info(self):
        """
        Returns the information stored in the message
        :return:
        """
        return self.info


    def is_match_start_message(self):
        """
        Whether the message is a start of match notification
        :return: True if message is a start of match notification, False otherwise
        """
        return self.msgtype == Message.Match_Start

    def is_match_end_message(self):
        """
        Whether the message is a end of match notification
        :return: True if the message is a end of match notification, False otherwise
        """
        return self.msgtype == Message.Match_End

    def is_round_start_message(self):
        """
        Whether the message is a start of round notification
        :return: True if the message is a start of round notification, False otherwise
        """
        return self.msgtype == Message.Round_Start

    def is_round_end_message(self):
        """
        Whether the message is a end of round notification
        :return: True if the message is a end of round notification, False otherwise
        """
        return self.msgtype == Message.Round_End

    @staticmethod
    def create_message(msgtype, players=None, info=None):
        """
        Helper method that builds different kinds of messages
        :param msgtype: Message type
        :param players: Players involved in the message if any
        :param info: Additional information that is contained in the message, such as the moves made in a game and the result etc.
        :return: the message that is created
        """
        m = Message(msgtype)
        m.set_players(players)
        m.set_info(info)
        return m



