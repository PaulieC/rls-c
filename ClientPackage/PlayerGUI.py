from Tkinter import *
import os
import tkMessageBox


def quit_game():
    if tkMessageBox.askyesno("Quit Game", "Are you sure you want to quit?"):
        main.quit()

def set_player_name():
    console.insert(END, player_name.get() + " is now your player's name.\n")

def set_ip_address():
    console.insert(END, ip_address.get() + " is now the address you are connecting to.\n")

def set_port():
    console.insert(END, port.get() + " is now the port you are connecting to.\n")

def connect():
    console.insert(END, "Attempting to connect...\n")

def verify_connection():
    console.insert(END, "Verifying that you are connected...\n")

def register():
    console.insert(END, "Attempting to register...\n")

def verify_registration():
    console.insert(END, "Verifying that you are registered...\n")

def change_player():
    console.insert(END, "Player changed to: " + player.get() + "\n")


main = Tk()
main.wm_title("Player")

registrationLabel = Label(main, text="Registration Status:").grid(row=0, column=0)

# SetPlayerName
setPlayerNameLabel = Label(main, text="Set Player Name:").grid(row=1, column=0)
player_name = StringVar()
player_name.set("Fuzzy Dunlop")
setPlayerNameField = Entry(main, width=15, textvariable=player_name).grid(row=1, column=1)
setPlayerNameButton = Button(main, text="Select", command=set_player_name).grid(row=1, column=2, columnspan=2)

#Set Address
setGameAddressLabel = Label(main, text="Set IP Address:").grid(row=2, column=0)
ip_address = StringVar()
ip_address.set("192.168.0.1")
setIPAddressField = Entry(main, width=15, textvariable=ip_address).grid(row=2, column=1)
setIPAddressButton = Button(main, text="Select", command=set_ip_address).grid(row=2, column=2, columnspan=2)

#SetPort
setPortLabel = Label(main, text="Set Port:").grid(row=3, column=0)
port = StringVar()
port.set("12345")
setPortField = Entry(main, width=15, textvariable=port).grid(row=3,column=1)
setPortButton = Button(main, text="Select", command=set_port).grid(row=3, column=2,columnspan=2)

changePlayerLabel = Label(main, text="Change Player:").grid(row=4, column=0)
player = StringVar()
player.set("...")
listy = "some choices."
changePlayerMenu = OptionMenu(main, player, *listy, command='').grid(row=4, column=1)
changePlayerButton = Button(main, text="Select", command=change_player).grid(row=4, column=2, columnspan=2)

attemptConnectionLabel = Label(main, text="Attempt Connection:").grid(row=5, column=0)
attemptConnectionButton = Button(main, text="Connect", command=connect).grid(row=5, column=1,columnspan=3)

verifyConnectionLabel = Label(main, text="Verify Connection:").grid(row=6, column=0)
verifyConnectionButton = Button(main, text="Verify", command=verify_connection).grid(row=6,column=1,columnspan=3)

attemptRegistrationLabel = Label(main, text="Attempt Registration:").grid(row=7, column=0)
attemptRegistrationButton = Button(main, text="Register", command=register).grid(row=7,column=1,columnspan=3)

verifyRegistrationLabel = Label(main, text="Verify Registration:").grid(row=8, column=0)
verifyRegistrationButton = Button(main, text="Verify", command=verify_registration).grid(row=8, column=1, columnspan=3)

currentGameLabel = Label(main, text="Current Game:").grid(row=9, column=0)
currentTournamentLabel = Label(main, text="Current Tournament:").grid(row=10, column=0)
setPlayerReadyLabel = Label(main, text="Set your player:").grid(row=11, column=0)

console = Text(main, bg="#434A54", fg="white")
console.grid(row=12, columnspan=4)

quitButton = Button(main, text="Quit", command=quit_game).grid(row=13, columnspan=4)

main.mainloop()
