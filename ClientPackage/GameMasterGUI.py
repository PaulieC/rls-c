from Tkinter import *
import os
import tkMessageBox
import importlib
from ClientPackage.GameMasterClient import *
from AvailablePlayers.GMPlayer import *


my_player = GMPlayer()
gmc = GameMasterClient(my_player)
#gmc.client_connect('150.250.190.225')
# verify connection
# client.verify_connection()

reg_status = "Closed"
num_connections = 0
num_registered = 0
network_error = "Verify your physical network adapter settings.\n" \
                "Check the server's connection.\n" \
                "Is the server running at this time?\n"


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


def set_rounds_max():
    try:
        gmc.set_max_rounds(maxRoundsCount.get())
    except Exception:
        console.insert(END, "\nUnknown error when trying to set the number of rounds.\n" + network_error)


def select_game_type():
    game_type = selectedGameType.get().replace(".py", "")
    try:
        gmc.set_game(game_type)
        console.insert(END, "\nThe selected game type is now: " + selectedGameType.get() + "\n")
    except Exception:
        console.insert(END, "\nError changing the game type.\n"
                            "This is likely due to a corrupt/missing .py file on either/both server and admin sides.\n"
                            + network_error)


def select_tournament_type():
    try:
        gmc.set_tournament((selectedTournamentType.get().replace(".py", "")))
        console.insert(END, "\nThe selected tournament type is now: " + selectedTournamentType.get() + "\n")
    except Exception:
        console.insert(END, "\nError changing the tournament type.\n"
                            "This is likely due to a corrupt/missing .py file on either/both server and admin sides.\n"
                       + network_error)


def open_registration():
    try:
        console.insert(END, "\n" + gmc.open_tournament_registration() + "\n")
        reg_status.set("Open")
    except Exception:
        console.insert(END, "Error trying to open the tournament's registration.\n" + network_error)


def close_registration():
    try:
        console.insert(END, "\n" + gmc.close_tournament_registration() + "\n")
        reg_status.set("Closed")
    except Exception:
        console.insert(END, "\nError trying to close the tournament's registration.\n" + network_error)

def get_tournament_status():
    try:
        console.insert(END, "\nThe tournament is currently: " + str(gmc.get_tournament_status()) + "\n")
    except Exception:
        console.insert(END, "\nError trying to retrieve the server's tournament status.\n" + network_error)


def start_tournament():
    try:
        gmc.start_tournament()
        console.insert(END, "\nThe tournament has been started.\n")
    except Exception:
        console.insert(END, "\nError trying to start the tournament.\n" + network_error)


def end_tournament():
    try:
        if tkMessageBox.askyesno("End Tournament", "Are you sure you want to end this tournament?"):
            gmc.end_game()
            console.insert(END, "\nThe tournament has been stopped.\n")
        else:
            console.insert(END, "\nThe tournament is still running.\n")
    except Exception:
        console.insert(END, "Error trying to end the tournament.\n" + network_error)


def update_players_connected():
    try:
        num = gmc.get_num_registered()
        console.insert(END, num)
        num_registered.set(str(num))
    except Exception:
        console.insert(END, "Error trying to retrieve the number of players.\n" + network_error)


def print_connections():
    console.insert(END, "Here's your list of connections...:\n")


def kill_server():
    try:
        gmc.client_connect.call.stop()
        console.insert(END, "He's dead Jim.")
    except Exception:
        console.insert(END, "Error trying to destroy the server.\n"
                            "Is it running?\n" + network_error)


def connect():
    try:
        console.insert(END, "Attempting to connect...\n")
        gmc.client_connect(host=ip.get(), port=port.get())      # TODO client quits if it has nothing to connect to.
        try:
            console.insert(END, gmc.verify_connection() + "\n")
        except Exception:
            console.insert(END, "Unable to verify connection at this time.\n"
                                "Try again after checking ip/port settings.\n")
    except Exception:
        console.insert(END, "Unable to make a connection at this time.\n"
                            "Try again after checking ip/port settings.\n")


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
ip.set("150.250.190.225")
setIPField = Entry(main, width=10, textvariable=ip).grid(row=0, column=1)


#SetPort
setPortLabel = Label(main, text="Set the Port:").grid(row=1, column=0)
port = IntVar()
port.set(12345)
setPortField = Entry(main, width=10, textvariable=port).grid(row=1, column=1)


#Connect
connectButton = Button(main, text="Connect", command=connect).grid(row=0, column=2, columnspan=2, rowspan=2)

#GAME TYPE
gameTypeLabel = Label(main, text="Choose a game type:").grid(row=2, column=0)
selectedGameType = StringVar()
selectedGameType.set("RockPaperScissors.py")
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
reg_status = StringVar()
reg_status.set("Closed")
registrationStatus = Label(main, textvariable=reg_status).grid(row=4, column=1)
openRegistrationButton = Button(main, text="Open", command=open_registration).grid(row=4, column=2)
closeRegistrationButton = Button(main, text="Close", command=close_registration).grid(row=4, column=3)

#SET MAX ROUNDS
setMaxRoundsLabel = Label(main, text="Set the maximum number of rounds:").grid(row=5, column=0)
maxRoundsCount = StringVar()
maxRoundsCount.set("0")
setMaxRoundsField = Entry(main, width=10, textvariable=maxRoundsCount).grid(row=5, column=1)
setMaxRoundsButton = Button(main, text="Select", command=set_rounds_max).grid(row=5, column=2, columnspan=2)

#GameStatus
gameStatusLabel = Label(main, text="Tournament Status:").grid(row=6, column=0)
gameStatusButton = Button(main, text="Tournament Status", command=get_tournament_status).grid(row=6, column=1)



#LIST CONNECTED PLAYERS
connectionsLabel = Label(main, text="Number of players connected:").grid(row=7, column=0)
num_registered = StringVar()
num_registered.set("0")
connectionsLabel= Button(main, textvariable=num_registered, command='').grid(row=7, column=1)
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