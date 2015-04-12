from Tkinter import *
import os
import GameMasterClient

def list_files(path):
        """
        Web: http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
        Username: Apogentus
        :param path:
        :return:
        """
        # returns a list of names (with extension, without full path) of all files
        # in folder path
        files = []
        for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)):
                if name != "__init__.py" and name.endswith(".py"):
                    files.append(name)
        return files

def print_list(list):
        num = 0
        for name in list:
            print str(num) + ".   " + name
            num += 1

def print_this(v):
    print v

main = Tk()
main.wm_title("Game Master Client")

gameTypeLabel = Label(main, text= "Set your preferences:").pack()
gameTypeLabel = Label(main, text= "").pack()

#
#THIS BLOCK JUST FOR POPULATING THE LISTS, NEEDS TO CHANGE
#

os.chdir("..")
os.chdir(os.curdir + "/AvailableGames")
result = os.path.abspath(os.curdir) + "/"
listy = list_files(result)

os.chdir("..")
os.chdir(os.curdir + "/AvailableTournaments")
result = os.path.abspath(os.curdir) + "/"
tourney = list_files(result)

##########################################################

#GAME TYPE
gameTypeLabel = Label(main, text= "Choose a game type:").pack()
selectedGameType = StringVar()
selectedGameType.set(listy[0])
gameTypeMenu = OptionMenu(main, selectedGameType, *listy, command=print_this).pack()

#TOURNAMENT TYPE
tourneyTypeLabel = Label(main, text= "Choose a tournament type:").pack()
selectedTournamentType = StringVar()
selectedTournamentType.set(tourney[0])
tournamentTypeMenu = OptionMenu(main, selectedTournamentType, *tourney, command=print_this).pack()

#LIST CONNECTED PLAYERS
connectedPlayersLabel = Label(main, text= "View connected players:").pack()
connectedPlayersButton = Button(main, text="View").pack()

#SET MAX PLAYERS
setMaxPlayersLabel = Label(main, text="Set the maximum number of players:").pack()

#SEE NUMBER OF CONNECTIONS, CLICKING THIS SHOULD REFRESH
numConnectionsLabel = Label(main, text="Number of connections (Click to Refresh):").pack()
numConnectionsButton = Button(main, text="4 Connections", command='').pack()

gameTypeLabel = Label(main, text= "").pack()

bottomFrame = Frame(main).pack(side=BOTTOM, anchor=CENTER)
#START
start = Button(bottomFrame, text="Start!", command='').pack(side=TOP, fill=X)
#ADVANCE
adv = Button(bottomFrame, text="Advance!", command='').pack(side=TOP, fill=X)
#END
end= Button(bottomFrame, text="End!", command='').pack(side=TOP, fill=X)
main.mainloop()