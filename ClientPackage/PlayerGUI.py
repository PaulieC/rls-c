__author__ = "Paul Council, Anand Patel"
__version__ = "sprint5"

from Tkinter import *
import tkMessageBox
from PlayerClient import *
from AvailablePlayers.TestPlayer1 import *

player = TestPlayer1()
client = PlayerClient(player)

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

def quit_game():
    if tkMessageBox.askyesno("Quit Game", "Are you sure you want to quit?"):
        main.quit()

def set_player_name():
    client.set_name(str(player_name.get()))
    console.insert(END, player_name.get() + " is now your player's name.\n")

def set_ip_address():
    console.insert(END, ip_address.get() + " is now the address you are connecting to.\n")

def set_port():
    console.insert(END, port.get() + " is now the port you are connecting to.\n")

def connect():
    client.client_connect(host = ip_address.get(), port =int(port.get()))
    console.insert(END, "Attempting to connect...\n")

def verify_connection():
    client.verify_connection
    console.insert(END, "Verifying that you are connected...\n")

def register():
    client.register_player()
    console.insert(END, "Attempting to register...\n")

def verify_registration():
    client.verify_connection
    console.insert(END, "Verifying that you are registered...\n")

def change_player():
    player = selected_player.get().replace(".py", "")
    console.insert(END, "Player changed to: " + player.get() + "\n")

def submit_move():
    client.submit_move()
    console.insert(END, "Submit" + "\n")


main = Tk()
main.wm_title("Player")

#registrationLabel = Label(main, text="Registration Status:").grid(row=0, column=0)

# SetPlayerName
setPlayerNameLabel = Label(main, text="Set Player Name:").grid(row=1, column=0)
player_name = StringVar()
player_name.set("Fuzzy Dunlop")
setPlayerNameField = Entry(main, width=15, textvariable=player_name).grid(row=1, column=1)
setPlayerNameButton = Button(main, text="Select", command=set_player_name).grid(row=1, column=2, columnspan=2)

#Set Address
setGameAddressLabel = Label(main, text="Set IP Address:").grid(row=2, column=0)
ip_address = StringVar()
ip_address.set("150.250.190.225")
setIPAddressField = Entry(main, width=15, textvariable=ip_address).grid(row=2, column=1)
setIPAddressButton = Button(main, text="Select", command=set_ip_address).grid(row=2, column=2, columnspan=2)

#SetPort
setPortLabel = Label(main, text="Set Port:").grid(row=3, column=0)
port = StringVar()
port.set("12345")
setPortField = Entry(main, width=15, textvariable=port).grid(row=3,column=1)
setPortButton = Button(main, text="Select", command=set_port).grid(row=3, column=2,columnspan=2)

#ChangePlayerAI
os.chdir("..")
os.chdir(os.curdir + "/AvailablePlayers")
result = os.path.abspath(os.curdir) + "/"
players = list_files(result)
changePlayerLabel = Label(main, text="Change Player:").grid(row=4, column=0)
selected_player = StringVar()
selected_player.set("...")
changePlayerMenu = OptionMenu(main, selected_player, *players, command='').grid(row=4, column=1)
changePlayerButton = Button(main, text="Select", command=change_player).grid(row=4, column=2, columnspan=2)

attemptConnectionLabel = Label(main, text="Attempt Connection:").grid(row=5, column=0)
attemptConnectionButton = Button(main, text="Connect", command=connect).grid(row=5, column=1,columnspan=3)

verifyConnectionLabel = Label(main, text="Verify Connection:").grid(row=6, column=0)
verifyConnectionButton = Button(main, text="Verify", command=verify_connection).grid(row=6,column=1,columnspan=3)

attemptRegistrationLabel = Label(main, text="Attempt Registration:").grid(row=7, column=0)
attemptRegistrationButton = Button(main, text="Register", command=register).grid(row=7,column=1,columnspan=3)

verifyRegistrationLabel = Label(main, text="Verify Registration:").grid(row=8, column=0)
verifyRegistrationButton = Button(main, text="Verify", command=verify_registration).grid(row=8, column=1, columnspan=3)

submitMoveLabel = Label(main, text="Start submitting moves:").grid(row=9, column=0)
submitMoveButton = Button(main, text="Submit", command=submit_move).grid(row=9, column=1)


console = Text(main, bg="#434A54", fg="white")
console.grid(row=12, columnspan=4)

quitButton = Button(main, text="Quit", command=quit_game).grid(row=13, columnspan=4)

main.mainloop()
