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
# client.verify_connection()

reg_status = "Closed"
num_connections = 0


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
    gmc.set_game((selectedGameType.get().replace(".py", "")))


def select_tournament_type():
    console.insert(END, "The selected tournament type is now: " + selectedTournamentType.get() + "\n")
    gmc.set_tournament((selectedTournamentType.get().replace(".py", "")))


def open_registration():
    gmc.open_tournament_registration()
    console.insert(END, "Registration Open\n")


def close_registration():
    gmc.close_tournament_registration()
    console.insert(END, "Registration Closed\n")


def get_tournament_status():
    console.insert(END, "The tournament is currently: " + gmc.get_tournament_status() + "\n")


def start_tournament():
    gmc.start_game()
    console.insert(END, "The tournament has been started.\n")


def end_tournament():
    if tkMessageBox.askyesno("End Tournament", "Are you sure you want to end this tournament?"):
        gmc.end_game()
        console.insert(END, "The tournament has been stopped\n")


def update_players_connected():
    num_connections = gmc.get_num_registered()


def print_connections():
    console.insert(END, "Here's your list of connections...:\n")


def kill_server():
    gmc.close_connection()
    console.insert(END, "He's dead Jim.")


def connect():
    gmc.client_connect(host=ip, port=port)
    console.insert(END, str(gmc.verify_connection()))


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
#SetIP
setIPLabel = Label(main, text="Set the IP Address:").grid(row=0, column=0)
ip = StringVar()
ip.set("0.0.0.0")
setIPField = Entry(main, width=10, textvariable=ip).grid(row=0, column=1)


#SetPort
setPortLabel = Label(main, text="Set the Port:").grid(row=1, column=0)
port = StringVar()
port.set("12345")
setPortField = Entry(main, width=10, textvariable=port).grid(row=1, column=1)


#Connect
connectButton = Button(main, text="Connect", command=connect).grid(row=0, column=2, columnspan=2, rowspan=2)

#GAME TYPE
gameTypeLabel = Label(main, text="Choose a game type:").grid(row=2, column=0)
selectedGameType = StringVar()
selectedGameType.set("...")
gameTypeMenu = OptionMenu(main, selectedGameType, *listy).grid(row=2, column=1)
gameTypeButton = Button(main, text="Select", command=select_game_type).grid(row=2, column=2, columnspan=2)

#TOURNAMENT TYPE
tourneyTypeLabel = Label(main, text="Choose a tournament type:").grid(row=3, column=0)
selectedTournamentType = StringVar()
selectedTournamentType.set("...")
tournamentTypeMenu = OptionMenu(main, selectedTournamentType, *tourney).grid(row=3, column=1)
tournamentTypeButton = Button(main, text="Select", command=select_tournament_type).grid(row=3, column=2, columnspan=2)

#Open/Close Registration
registrationLabel = Label(main, text="Registration Status:").grid(row=4, column=0)
registrationStatus = Label(main, text=reg_status).grid(row=4, column=1)
openRegistrationButton = Button(main, text="Open", command=open_registration).grid(row=4, column=2)
closeRegistrationButton = Button(main, text="Close", command=close_registration).grid(row=4, column=3)

#SET MAX PLAYERS
setMaxPlayersLabel = Label(main, text="Set the maximum number of players:").grid(row=5, column=0)
maxPlayerCount = StringVar()
maxPlayerCount.set("0")
setMaxPlayerField = Entry(main, width=10, textvariable=maxPlayerCount).grid(row=5, column=1)
setMaxPlayerButton = Button(main, text="Select", command=print_player_max).grid(row=5, column=2, columnspan=2)

#GameStatus
gameStatusLabel = Label(main, text="Tournament Status:").grid(row=6, column=0)
gameStatusButton = Button(main, text="STATUS", command=get_tournament_status).grid(row=6, column=1)
start = Button(main, text="Start", command=start_tournament).grid(row=6, column=2)
end = Button(main, text="End", command=end_tournament).grid(row=6, column=3)


#LIST CONNECTED PLAYERS
connectionsLabel = Label(main, text="Number of players connected:").grid(row=7, column=0)
connectionsButton = Button(main, text=num_connections, command='').grid(row=7, column=1)
viewConnectionsButton = Button(main, text="Update", command=update_players_connected).grid(row=7, column=2,
                                                                                           columnspan=2)

#Kill Tournament
killLabel = Label(main, text="Ends the tournament by stopping the server:").grid(row=9, columnspan=2)
killButton = Button(main, text="KILL", command=kill_server).grid(row=10, columnspan=2)

#console
console = Text(main, bg="#434A54", fg="white")
console.grid(row=12, columnspan=4)
sys.stdout = console

main.mainloop()