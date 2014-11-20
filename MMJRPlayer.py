#################################################
# 
# RPSPlayer designed to work with RPSFramework
# Created by Matt Martorana + Justin Read
#

#################################################
import Player
import Observer
import Message

class MMJRPlayer(Player.Player,Observer):
   
# change these to object specific, not
# class specific
#
#

    global name 
    name = "MattMJustinR"
    global rock
    rock = 0
    global scissors
    scissors = 1
    global paper
    paper = 2
    global listOfMoves
    listOfMoves=[]
    #c = rpyc.connect(serverAddress, 12345)

    def notify(self,message):

#
#
# do self.
#
#



    def my_rps_play_strategy(self):
        result = 0
        for i in range(len(listOfMoves)):
            result = result + eval(listOfMoves[i])
        result = result % 3
        if (result == rock):
            return rock
        elif (result == paper):
            return paper
        elif (result == scissors):
            return scissors

    def play(self):
        move = my_rps_play_strategy()
        return move

    def set_history(self,listPastMoves):
        listOfMoves = listPastMoves

    def get_name(self):
        return name

    
    
def main():
    
    player = MattJustinRPSPlayer()
    player.set_history (['rock','scissors', 'paper', 'rock'])
    print(player.play())

if  __name__ =='__main__':
    main()
