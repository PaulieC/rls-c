from Tkinter import *
import os
import tkMessageBox
import importlib
from ClientPackage.GameMasterClient import *
from AvailablePlayers.GMPlayer import *

my_player = GMPlayer()
gmc = GameMasterClient(my_player)
gmc.client_connect('150.250.142.57')
# verify connection
#client.verify_connection()


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


def print_this(choice):
    print choice


def print_player_max():
    console.insert(END, "The current player count is: " + maxPlayerCount.get() + "\n")


def select_game_type():
    console.insert(END, "The selected game type is now: " + selectedGameType.get() + "\n")



def select_tournament_type():
    console.insert(END, "The selected tournament type is now: " + selectedTournamentType.get() + "\n")
    gmc.set_tournament(selectedTournamentType.get().replace(".py",""))


def open_registration():
    console.insert(END, "Registration Open\n")


def close_registration():
    console.insert(END, "Registration Closed\n")


def get_tournament_status():
    console.insert(END, "The tournament is currently: ...\n")


def start_tournament():
    console.insert(END, "The tournament has been started.\n")


def end_tournament():
    if tkMessageBox.askyesno("End Tournament", "Are you sure you want to end this tournament?"):
        console.insert(END, "The tournament has been stopped\n")


def set_ip():
    console.insert(END, "The IP Address is now: " + ip.get() + "\n")


def set_port():
    console.insert(END, "The Port is now set to: " + port.get() + "\n")


def print_connections():
    console.insert(END, "Here's your list of connections...:\n")


main = Tk()
main.wm_title("Game Master Client")


#
# THIS BLOCK JUST FOR POPULATING THE LISTS, NEEDS TO CHANGE
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
gameTypeLabel = Label(main, text="Choose a game type:").grid(row=0, column=0)
selectedGameType = StringVar()
selectedGameType.set("...")
gameTypeMenu = OptionMenu(main, selectedGameType, *listy, command='').grid(row=0, column=1)
gameTypeButton = Button(main, text="Select", command=select_game_type).grid(row=0, column=2, columnspan=2)

#TOURNAMENT TYPE
tourneyTypeLabel = Label(main, text="Choose a tournament type:").grid(row=1, column=0)
selectedTournamentType = StringVar()
selectedTournamentType.set("...")
tournamentTypeMenu = OptionMenu(main, selectedTournamentType, *tourney, command='').grid(row=1, column=1)
tournamentTypeButton = Button(main, text="Select", command=select_tournament_type).grid(row=1, column=2, columnspan=2)

#Open/Close Registration
registrationLabel = Label(main, text="Registration Status:").grid(row=2, column=0)
registrationStatus = Label(main, text="(Current)").grid(row=2, column=1)
openRegistrationButton = Button(main, text="Open", command=open_registration).grid(row=2, column=2)
closeRegistrationButton = Button(main, text="Close", command=close_registration).grid(row=2, column=3)

#SET MAX PLAYERS
setMaxPlayersLabel = Label(main, text="Set the maximum number of players:").grid(row=3, column=0)
maxPlayerCount = StringVar()
maxPlayerCount.set("0")
setMaxPlayerField = Entry(main, width=10, textvariable=maxPlayerCount).grid(row=3, column=1)
setMaxPlayerButton = Button(main, text="Select", command=print_player_max).grid(row=3, column=2, columnspan=2)

#GameStatus
gameStatusLabel = Label(main, text="Tournament Status:").grid(row=4, column=0)
gameStatusButton = Button(main, text="STATUS", command=get_tournament_status).grid(row=4, column=1)
start = Button(main, text="Start", command=start_tournament).grid(row=4, column=2)
end = Button(main, text="End", command=end_tournament).grid(row=4, column=3)

#SetIP
setIPLabel = Label(main, text="Set the IP Address:").grid(row=5, column=0)
ip = StringVar()
ip.set("0.0.0.0")
setIPField = Entry(main, width=10, textvariable=ip).grid(row=5, column=1)
setIPButton = Button(main, text="Select", command=set_ip).grid(row=5, column=2, columnspan=2)

#SetPort
setPortLabel = Label(main, text="Set the Port:").grid(row=6, column=0)
port = StringVar()
port.set("12345")
setPortField = Entry(main, width=10, textvariable=port).grid(row=6, column=1)
setPortButton = Button(main, text="Select", command=set_port).grid(row=6, column=2, columnspan=2)

#LIST CONNECTED PLAYERS
connectionsLabel = Label(main, text="Number of players connected:").grid(row=7, column=0)
connectionsButton = Button(main, text="4 Connections", command='').grid(row=7, column=1)
viewConnectionsButton = Button(main, text="View", command=print_connections).grid(row=7, column=2, columnspan=2)

#console
console = Text(main, bg="#434A54", fg="white")
console.grid(row=8, columnspan=4)

main.mainloop()