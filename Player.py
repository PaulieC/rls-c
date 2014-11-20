#Samantha Holloway, Joe Pannizzo 11/2014

#Class Player is used as the top level class abstraction to play in a Tournament
#It specifies what a concrete Player must do to be a part of the Tournament
#Each Player can be registered for a Tournament
#Concrete implementations of a Player will play against other ones playing
#the same game.
#Since there can be many player types for many games
#the AI for making moves in the 'play' function must be
#delegated to the concrete implementations that subclass Player.

#Ex: A Rock Paper Scissors Player that subclasses Player would
#define some AI in 'play' to return 'rock' 'paper or 'scissors'

import Observer

class Player(Observer.Observer):
    def __init__(self):
        self.name = None
    #play should be defined to return a move based on AI/Strategy,
    #it takes in move history of opponent
    def play(self):
        pass
    #should be defined to return the Player instance variable 'name'
    def get_name(self):
        pass
    #should be defined to set the Player instance variable name
    def set_name(self, playername):
        self.name = playername




