# Alex Ciaramella and Greg Suner
# Abstract Tournament Class

#Tournament is observable while players are observers

class Tournament(Observable):
    # set up a list of players when tournament is initialized
    def __init__(self):
        self.playerList = []
		registration = True
    # run the tournament
    def run(self):
		
		begin_tournament()
        while(True):
        	match = create_next_match(self)
                if match == None:
                    break
                play_match(self, match)
			
			
    # get a reference to the next game to be played
    def create_next_match(self):
        pass

    # register a player for the tournament by adding them to       # the  list of current players
    def register_player(self, player):
		if registration
			self.playerList.append(player)
		else
			print ("Sorry, registration is closed")

    # play the next match and return the results
    # is tournament responsible for looping the match until someone reaches the score limit or is that game's responsiblity? Or some external class we still need???
	#I believe we talked about a match class that is used only within tournament. I think it loops the game to the score limit
    def play_match(self, match):
        return match.play()

    # update the score board with the winner and loser of the game
    def update_scoreboard(self, results):
	#I'm unsure how results are reported from the game
	# and how they're sent to scoreboard so pass
	# for now
        pass
	
	# Closes registration and notifies players tournament has begun
	def begin_tournament(self):
		registration = False
		#Dont know how we should notify the players with observable/observer in python
	
	# Announces results of tournament to all players
	def end_tournament(self)
		pass

		
		
#Match class that handles the players playing each other		
class Match:
	
	#Takes 2 players and number of games to play
	#I believe Dr. Baliga said it was ok to leave it hard coded at 2 players for the first sprint
	def __init__(self, p, q, num_games):
		self.p = p
		self.q = q
		self.num_games = num_games
		
	#Loops until total number of games is played
	#Here should be taking the players moves and getting the results I think
	#Unsure of the format that the rules/game class has
	#Is this also where we have to track the scores for the match?
	#Also it should notify the scoreboard of who won and the players of the result right?
	
	def play(self):
		for x in range(num_games)
			
			