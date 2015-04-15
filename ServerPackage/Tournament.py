__author__ = "Paul Council, Joseph Gonzoph, Anand Patel"
__version__ = "sprint1"
__credits__ = ["Alex Ciaramella, Greg Suner"]

# imports
from ServerPackage import Display, Message, Observable
import time
from ServerPackage.MatchData import *

#


class Tournament(Observable.Observable):
    """
    Abstract Tournament Class
    Tournament is observable while players are observers

    Attributes:
        playerList: the array that holds the Player objects
        game: the game that this tournament will use in play
        display: TODO
    """

    def __init__(self):
        """ set up a list of players when tournament is initialized """
        Observable.Observable.__init__(self)
        self.name = None
        self.playerList = []
        self.game = None
        self.display = None
        self.num_players = 0
        self.max_players = 30

    def attach_display(self, display):
        """
        Register the display to this Tournament
        :param display: the display to sync with this Tournament
        :type display: Display.Display
        """
        self.display = display
        self.add_observer(self.display)

    def get_players(self):
        """
        Returns the players in the tournament
        :return playerList: The array that holds the players
        :rtype: list
        """
        return self.playerList

    def run(self):
        """ run the tournament """
        self.begin_tournament()
        while True:
            match = self.create_next_match()
            if match is None:
                break
            self.play_match(match)
        self.end_tournament()

    def create_next_match(self):
        """
        Get a reference to the next game to be played .
        This should be implemented
        """
        pass

    def register_player(self, player):
        """
        register a player for the tournament by
        adding them to the  list of current players
        :param player: the Player object to register
        :type player: Player.Player
        """
        self.playerList.append(player)
        self.add_observer(player)
        self.num_players += 1

    def set_game(self, game):
        """
        stores a reference to the type of game we will be playing
        :param game: the Game object to be registered to this Tournament
        :type game: Game
        """
        self.game = game

    def get_result(self, moves):
        """
        Computes the result of a round based on the moves made by the players
        :param moves: the moves list of the Player
        :type moves: list
        """
        return self.game.get_result(moves)

    def play_match(self, match):
        """
        play the next match and return the results
        :param match: the information for the current match
        :type match: tuple
        """
        players = match[0]
        self.start_match(players)
        result = self.play_rounds(match)
        self.end_match(players, result)

    def play_round(self, match):
        players = [match.player1_round, match.player2_round]
        # self.start_round(players)
        moves = []
        for p in players:
            moves.append(p[1])
        result = self.get_result(moves)
        round_result = ((players[0], result[0]), (players[1], result[1]))
        # self.end_round(players, moves, result)
        return round_result

    def play_rounds(self, match):
        """
        This function should return a result, but when it does return result,
        it stops the match in the preceding play_match function.
        This is likely a bug, but I haven't figured out a solution to this.
        :param match: the current match that the tournament should play rounds in
        :type match: tuple
        """
        players = match[0]
        rounds = match[1]
        for i in range(rounds):
            self.start_round(players)
            moves = []
            for p in players:
                moves.append(p[1])
            result = self.get_result(moves)
            round_result = ((players[0], result[0]), (players[1], result[1]))
            self.end_round(players, moves, result)
            return round_result

    @staticmethod
    def begin_tournament():
        """ notifies players tournament has begun """
        pass

    @staticmethod
    def end_tournament():
        """ Announces results of tournament to all players """
        pass    # TODO

    def start_match(self, players):
        """
        send a message containing a list of all the players in the current match
        :param players: the list of players registered to this tournament
        :type players: list
        """
        message = Message.Message.get_match_start_message(players)
        self.notify_all(message)
        time.sleep(3)

    def end_match(self, players, result):
        """
        send a message containing the result of the match
        :param players: players that participated in the current match
        :type players: list
        :param result: the results of the match
        :type result: Match
        """
        message = Message.Message.get_match_end_message(players, result)
        self.notify_all(message)

    def start_round(self, players):
        """
        send a message containing the players in the next game
        :param players: the players to participate in the match
        :type players: list
        """
        message = Message.Message.get_round_start_message(players)
        self.notify_all(message)

    def end_round(self, players, moves, result):
        """
        send a message containing the players, moves, and result of the last game
        :param players: the list of players in the round
        :type players: list
        :param moves: the list of moves that were in this round
        :type moves: list
        :param result: the message concerning the round results
        :type result: str
        """
        message = Message.Message.get_round_end_message(players, moves, result)
        self.notify_all(message)
        time.sleep(3)

    def get_method(self):
        """
        :return:
        """
        return self

    def set_number_of_players(self, max_players):
        self.max_players = max_players

    def get_num_players(self):
        return self.num_players

    def get_max_num_players(self):
        return self.max_players

    def get_name(self):
        return self.name
