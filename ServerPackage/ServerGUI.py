from Tkinter import *
import tkMessageBox
from ServerPackage.TournamentServer import *


def set_ip():
    """
    Function to allow the user to set the ip for the running server.
    This new ip is then displayed in the respective GUI label.
    """
    try:
        ip.set(new_server.set_ip(ip.get()))
        console.insert(END, "The IP Address is now: " + ip.get() + "\n")
    except Exception:
        console.insert(END, "Error while trying to assign ip address.\n"
                            "This is likely due to an improper value for the ip.\n"
                            "Please try again with a different ip setting.\n")


def set_port():
    """
    Functions to allow the user to set the port for the running server.
    This port number is then displayed in the respective GUI label
    """
    try:
        port.set(new_server.set_port(int(port.get())))
        console.insert(END, "The Port is now set to: " + port.get() + "\n")
    except Exception:
        console.insert(END, "Error while trying to assign the port.\n"
                            "This is likely due to an improper value for the port.\n"
                            "Please try again with a different port value.\n")


def generate_ip():
    """
    Function to search the Linux machine for a unique host address.
    This host address is then displayed in all of the ip labels.
    NOTE: this call will not work on other operating systems. An error
            handled to print information to the user.
    """
    new_ip = False
    try:
        new_ip = new_server.generate_ip()
    except Exception:
        console.insert(END, "Unknown error when trying to generate ip address.")
    if not new_ip:
        console.insert(END, "The ip couldn't be generated...\n"
                            "Please note that at this time ip generation only"
                            "works on Linux distros.\n"
                            "Manually type in your unique ip in:\n"
                            "\'Set the IP Address:\' box\n ")
    else:
        generated.set(new_ip)
        ip.set(generated.get())
        console.insert(END, "Generated an IP\n")


def open_connection():
    """
    Function to create the server object and open the connection of this server
    to listen for connections.
    WARNING:
            Once this is launched, a keystroke cancel is the only method of
            quiting this server at this time...
    """
    serve = new_server.create_server()
    if serve:
        console.insert(END, "Server has started. Opening the connection...\n")
        console.insert(END, "Opened the connection\n")
        try:
            new_server.open_connection()
        except Exception:
            console.insert(END, "Server has been forced closed...\n")
    elif serve is None:
        console.insert(END, "There was an error in creating the server...\n")
    else:
        console.insert(END, "The server couldn't be started at this time\n"
                            "Try checking the ip and/or port setting...\n")


def close_connection():
    """
    Function to close the server's connection. This should only be accessible from
    the GameController's client.
    """
    # TODO implement fully or remove option entirely
    if tkMessageBox.askyesno("Close Connection", "Are you sure you want to close your connection?"):
        closed = False
        try:
            closed = new_server.close_connection()
        except Exception:
            console.insert(END, "Unknown error when trying to close the server's connection.\n")
        if closed:
            console.insert(END, "Closed the connection\n")
        else:
            console.insert(END, "CONNECTION COULD NOT BE STOPPED!!!\n")
    else:
        console.insert(END, "The connection is still open\n")

main = Tk()
new_server = TournamentServer()
main.wm_title("Server")

# SetIP
setIPLabel = Label(main, text="Set the IP Address:").grid(row=1, column=0)
ip = StringVar()
ip.set("0.0.0.0")
setIPField = Entry(main, width=10, textvariable=ip).grid(row=1, column=1)
setIPButton = Button(main, text="Select", command=set_ip).grid(row=1, column=2, columnspan=2)

# SetPort
setPortLabel = Label(main, text="Set the Port:").grid(row=2, column=0)
port = StringVar()
port.set("12345")
setPortField = Entry(main, width=10, textvariable=port).grid(row=2, column=1)
setPortButton = Button(main, text="Select", command=set_port).grid(row=2, column=2, columnspan=2)

# Generate IP
generateIPLabel = Label(main, text="Generate an IP:").grid(row=3, column=0)
generated = StringVar()
generated.set("-.-.-.-")
generateIPField = Entry(main, width=10, textvariable=generated).grid(row=3, column=1)
generateIPButton = Button(main, text="Generate", command=generate_ip).grid(row=3, column=2, columnspan=2)

# Open/Close serving
connectionLabel = Label(main, text="Open or Close the connection:").grid(row=4, column=0)
openButton = Button(main, text="Open", command=open_connection).grid(row=4, column=2)
closeButton = Button(main, text="Close", command=close_connection).grid(row=4, column=3)

# console
console = Text(main, bg="#434A54", fg="white")
console.grid(row=8, columnspan=4)

main.mainloop()