# Alex Ciaramella and Greg Suner
# Abstract Tournament Class

#Tournament is observable while players are observers

import Message

class Tournament(Observable):
    # set up a list of players when tournament is initialized
    def __init__(self):
        self.playerList = []
	self.game

    # run the tournament
    def run(self):	
        self.begin_tournament()
        while(True):
        	match = self.create_next_match()
                if match == None:
                    break
                self.play_match(match)
        self.end_tournament()
			
			
    # get a reference to the next game to be played
    def create_next_match(self):
        pass

    # register a player for the tournament by adding them to       # the  list of current players
    def register_player(self, player):
        self.playerList.append(player)

    # stores a reference to the type of game we will be playing
    def set_game(self, game):
        self.game = game

    # play the next match and return the results
    def play_match(self, match):
        self.start_match(match[0])
        result = self.play_game(match)
	self.end_match(match[0], result)

    # plays each indvidual game in the match
    def play_game(self, match):
        for i in range(0, match[1]):
            self.start_game(match[0])
            result = match.get_results(match[0])
            # need to find out definite structure of results!!
            self.end_game(result[0], result[1], result[2])

	# notifies players tournament has begun
    def begin_tournament(self):
        pass	
	
	# Announces results of tournament to all players
    def end_tournament(self):
        pass

    # send a message containing a list of all the players in the current match
    def start_match(self, players):
        message = Message.get_match_start_message(players)
        self.notify_all(message)

    # send a message containing the result of the match
    def end_match(self,players, result):
        message = Message.get_match_end_message(players, result)
        self.notify_all(message)

    # send a message containing the players in the next game
    def start_game(self, players):
        message = Message.get_round_start_message(players)
        self.notify_all(message)

    # send a message containing the players, moves, and result of the last game
    def end_game(players, moves, result):
        message = Message.get_round_end_message(players, moves, result)
        self.notify_all(message)
