# Alex Ciaramella and Greg Suner
# Abstract Tournament Class

class Tournament:
    # set up a list of players when tournament is initialized
    def __init__(self):
        self.playerList = []

    # run the tournament
    def run(self):
        while(True):
        	match = create_next_match(self)
                if match == None:
                    break
                update_scoreboard(play_match(self, match))

    # get a reference to the next game to be played
    def create_next_match(self):
        pass

    # register a player for the tournament by adding them to       # the  list of current players
    def register_player(self, player):
        self.playerList.append(player)

    # play the next match and return the results
    # is tournament responsible for looping the match until someone reaches the score limit or is that game's responsiblity? Or some external class we still need???
    def play_match(self, match):
        return match.play()

    # update the score board with the winner and loser of the game
    def update_scoreboard(self, results):
	#I'm unsure how results are reported from the game
	# and how they're sent to scoreboard so pass
	# for now
        pass
