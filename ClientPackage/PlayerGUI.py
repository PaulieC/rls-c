__author__ = "Paul Council, Anand Patel"
__version__ = "sprint5"

from Tkinter import *
import tkMessageBox
from PlayerClient import *
from AvailablePlayers.TestPlayer1 import *
import importlib

player = TestPlayer1()
client = PlayerClient(player)


def list_files(path):
    """
    Lists files inside the given path
    Web: http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
    Username: Apogentus
    :param path: the path we want to search
    :return files: the list of files
    """
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            if name != "__init__.py" and name.endswith(".py"):
                files.append(name)
    return files


def quit_game():
    try:
        if tkMessageBox.askyesno("Quit Game", "Are you sure you want to quit?"):
            main.quit()
    except Exception:
        console.insert(END, "Unknown error thrown in quit_game.\n")


def set_player_name():
    try:
        client.set_name(str(player_name.get()))
        console.insert(END, player_name.get() + " is now your player's name.\n")
    except Exception:
        console.insert(END, "Error trying to set the player's name.\n"
                            "The name should not include an underscore or special character.\n" + network_error_message)


def set_ip_address():
    try:
        console.insert(END, ip_address.get() + " is now the address you are connecting to.\n")
    except Exception:
        console.insert(END, "Error trying to set the ip address.\n"
                            "Check your values.\n"
                            "An IP address should consist of 4 groups of digits.\n"
                            "EXAMPLE: 000.000.000.000\n"
                            "NOTE: they aren't necessarily groups of 3.\n")


def set_port():
    try:
        console.insert(END, port.get() + " is now the port you are connecting to.\n")
    except Exception:
        console.insert(END, "Error trying to set the port value.\n"
                            "Remember that the port should be 5 digits.\n"
                            "EXAMPLE: 12345\n"
                            "Try again.\n")


def connect():
    console.insert(END, "Attempting to connect...\n")
    try:
        client.client_connect(host=ip_address.get(), port=int(port.get()))
    except Exception:
        console.insert(END, "Error trying to connect to server.\n"
                            "Check ip address as well as port number.\n"
                            "Verify values with the game admin.\n" + network_error_message)


def verify_connection():
    console.insert(END, "Verifying that you are connected...\n")
    try:
        client.verify_connection()
    except Exception:
        console.insert(END, "Error verifying connection.\n" + network_error_message)


def register():
    console.insert(END, "Attempting to register...\n")
    try:
        client.register_player()
    except Exception:
        console.insert(END, "Error trying to register to tournament.\n" + network_error_message)


def verify_registration():
    console.insert(END, "Verifying that you are registered...\n")
    try:
        client.verify_connection()
    except Exception:
        console.insert(END, "Error trying to verify registration.\n" + network_error_message)


def change_player():
    try:
        player_type = selected_player.get().replace(".py", "")
        client.change_player(player_type)
        console.insert(END, "Player changed to: " + client.player.get_name() + "\n")
    except Exception:
        console.insert(END, "Error trying to load in player.\n"
                            "This may be due to a corrupt/missing player file.\n"
                            "Notify the game admin.\n")


def submit_move():
    try:
        client.submit_move()
        console.insert(END, "Submit" + "\n")
    except Exception:
        console.insert(END, "Error trying to submit the move.\n" + network_error_message)


main = Tk()
main.wm_title("Player")
network_error_message = "Check physical network adapter.\n" \
                        "If error occurs again, notify the game admin.\n"


"""
Set Player Name row
"""
setPlayerNameLabel = Label(main, text="Set Player Name:").grid(row=1, column=0)
player_name = StringVar()
player_name.set("Fuzzy Dunlop")
setPlayerNameField = Entry(main, width=15, textvariable=player_name).grid(row=1, column=1)
setPlayerNameButton = Button(main, text="Select", command=set_player_name).grid(row=1, column=2, columnspan=2)

"""
Set Game Address row
"""
setGameAddressLabel = Label(main, text="Set IP Address:").grid(row=2, column=0)
ip_address = StringVar()
ip_address.set("150.250.190.225")
setIPAddressField = Entry(main, width=15, textvariable=ip_address).grid(row=2, column=1)
setIPAddressButton = Button(main, text="Select", command=set_ip_address).grid(row=2, column=2, columnspan=2)

"""
Set Port row
"""
setPortLabel = Label(main, text="Set Port:").grid(row=3, column=0)
port = StringVar()
port.set("12345")
setPortField = Entry(main, width=15, textvariable=port).grid(row=3, column=1)
setPortButton = Button(main, text="Select", command=set_port).grid(row=3, column=2, columnspan=2)

"""
Change AI row
"""
os.chdir("..")
os.chdir(os.curdir + "/AvailablePlayers")
result = os.path.abspath(os.curdir) + "/"
players = list_files(result)
changePlayerLabel = Label(main, text="Change Player:").grid(row=4, column=0)
selected_player = StringVar()
selected_player.set("...")
changePlayerMenu = OptionMenu(main, selected_player, *players, command='').grid(row=4, column=1)
changePlayerButton = Button(main, text="Select", command=change_player).grid(row=4, column=2, columnspan=2)

"""
Attempt Connection row
"""
attemptConnectionLabel = Label(main, text="Attempt Connection:").grid(row=5, column=0)
attemptConnectionButton = Button(main, text="Connect", command=connect).grid(row=5, column=1, columnspan=3)

"""
Verify Connection row
"""
verifyConnectionLabel = Label(main, text="Verify Connection:").grid(row=6, column=0)
verifyConnectionButton = Button(main, text="Verify", command=verify_connection).grid(row=6, column=1, columnspan=3)

"""
Attempt Registration row
"""
attemptRegistrationLabel = Label(main, text="Attempt Registration:").grid(row=7, column=0)
attemptRegistrationButton = Button(main, text="Register", command=register).grid(row=7, column=1, columnspan=3)

"""
Verify Registration row
"""
verifyRegistrationLabel = Label(main, text="Verify Registration:").grid(row=8, column=0)
verifyRegistrationButton = Button(main, text="Verify", command=verify_registration).grid(row=8, column=1, columnspan=3)

"""
Submit Move row
"""
submitMoveLabel = Label(main, text="Start submitting moves:").grid(row=9, column=0)
submitMoveButton = Button(main, text="Submit", command=submit_move).grid(row=9, column=1, columnspan=3)

"""
Console block
"""
console = Text(main, bg="#434A54", fg="white")
console.grid(row=12, columnspan=4)

"""
Quit Button
"""
quitButton = Button(main, text="Quit", command=quit_game).grid(row=13, columnspan=4)

# Begin the mainloop
main.mainloop()
