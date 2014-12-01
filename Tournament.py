# Alex Ciaramella and Greg Suner
# Abstract Tournament Class

# Tournament is observable while players are observers

import Message
import Observable
import Display

class Tournament(Observable.Observable):
    # set up a list of players when tournament is initialized
    def __init__(self):
        Observable.Observable.__init__(self)
        self.playerList = []
        self.game = None


    def attach_display(self, display):
        self.display = display
        self.add_observer(self.display)

    # Returns the players in the tournament
    def get_players(self):
        return self.playerList

    # run the tournament
    def run(self):
        self.begin_tournament()
        while (True):
            match = self.create_next_match()
            if match == None:
                break
            self.play_match(match)
        self.end_tournament()


    # get a reference to the next game to be played
    def create_next_match(self):
        pass

    # register a player for the tournament by adding them to
    #  the  list of current players
    def register_player(self, player):
        self.playerList.append(player)
        self.add_observer(player)

    # stores a reference to the type of game we will be playing
    def set_game(self, game):
        self.game = game


    # Computes the result of a round based on the moves made by the players
    def get_result(self, moves):
        return self.game.get_result(moves)

    # play the next match and return the results
    def play_match(self, match):
        players = match[0]
        self.start_match(players)
        result = self.play_rounds(match)
        self.end_match(players, result)

    # plays each indvidual game in the match
    def play_rounds(self, match):
        players = match[0]
        rounds = match[1]
        for i in range(rounds):
            self.start_round(players)
            moves = []
            for p in players:
                moves.append(p.play())
            result = self.get_result(moves)
            self.end_round(players, moves, result)


    # notifies players tournament has begun
    def begin_tournament(self):
        pass

    # Announces results of tournament to all players
    def end_tournament(self):
        pass

    # send a message containing a list of all the players in the current match
    def start_match(self, players):
        message = Message.Message.get_match_start_message(players)
        self.notify_all(message)

    # send a message containing the result of the match
    def end_match(self, players, result):
        message = Message.Message.get_match_end_message(players, result)
        self.notify_all(message)

    # send a message containing the players in the next game
    def start_round(self, players):
        message = Message.Message.get_round_start_message(players)
        self.notify_all(message)

    # send a message containing the players, moves, and result of the last game
    def end_round(self, players, moves, result):
        message = Message.Message.get_round_end_message(players, moves, result)
        self.notify_all(message)
