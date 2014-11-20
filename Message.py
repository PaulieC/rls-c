__author__ = 'geebzter'
# Defines message types for standard framework message
# Provides free (global) functions that help create standard messages
# such as get_round_end_message etc.

class Message(object):
    """
    Message types:
        Defines standard types of messages that are broadcast within the game.
    """
    TournamentStart = 1
    TournamentEnd = 2
    MatchStart = 3
    MatchEnd = 4
    RoundStart = 5
    RoundEnd = 6

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
        return self.msgtype == Message.MatchStart

    def is_match_end_message(self):
        """
        Whether the message is a end of match notification
        :return: True if the message is a end of match notification, False otherwise
        """
        return self.msgtype == Message.MatchEnd

    def is_round_start_message(self):
        """
        Whether the message is a start of round notification
        :return: True if the message is a start of round notification, False otherwise
        """
        return self.msgtype == Message.RoundStart

    def is_round_end_message(self):
        """
        Whether the message is a end of round notification
        :return: True if the message is a end of round notification, False otherwise
        """
        return self.msgtype == Message.RoundEnd


# Free (global) functions for creating messages of different types
def get_match_start_message(players):
    return createmessage(Message.MatchStart, players)

def get_match_end_message(players, result):
    return createmessage (Message.MatchEnd, players, result)

def get_round_start_message(players):
    return createmessage(Message.RoundStart, players)

def get_round_end_message(players, result):
    return createmessage(Message.RoundEnd, players, result)

def createmessage(msgtype, players=None, info=None):
    m = Message(msgtype)
    m.setplayers(players)
    m.setinfo(info)
    return m