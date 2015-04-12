from Tkinter import *
import os
import tkMessageBox

def quit_game():
    if tkMessageBox.askyesno("Quit Game", "Are you sure you want to quit?"):
        main.quit()

main = Tk()
main.wm_title("Player")

registrationLabel = Label(main, text= "Registration Status:").grid(row=0,column=0)
setPlayerNameLabel = Label(main, text="Set Player Name:").grid(row=1,column=0)
setGameAddressLabel = Label(main, text="Set IP Address:").grid(row=2,column=0)
setGamePortLabel = Label(main, text="Set Port:").grid(row=3, column=0)
changePlayerLabel = Label(main, text="Change Player:").grid(row=4, column=0)
attemptConnectionLabel = Label(main, text="Attempt Connection:").grid(row=5, column=0)
verifyConnectionLabel = Label(main, text="Verify Connection:").grid(row=6,column=0)
attemptRegistrationLabel = Label(main, text="Attempt Registration:").grid(row=7, column=0)
verifyRegistrationLabel = Label(main, text="Verify Registration:").grid(row=8,column=0)
currentGameLabel = Label(main, text="Current Game:").grid(row=9,column=0)
currentTournamentLabel = Label(main, text="Current Tournament:").grid(row=10,column=0)
setPlayerReadyLabel = Label(main, text="Set your player").grid(row=11,column=0)


console = Text(main, bg="#434A54", fg="white")
console.grid(row=12,columnspan=4)

quitButton = Button(main, text="Quit", command=quit_game).grid(row=13,columnspan=4)

main.mainloop()
