from Tkinter import *
import os
import tkMessageBox


def set_ip():
    console.insert(END, "The IP Address is now: " + ip.get()+ "\n")

def set_port():
    console.insert(END, "The Port is now set to: " + port.get() + "\n")

def generate_ip():
    generated.set("0.0.0.0")
    console.insert(END, "Generated an IP\n")

def open_connection():
    console.insert(END, "Opened the connection\n")

def close_connection():
    if tkMessageBox.askyesno("Close Connection", "Are you sure you want to close your connection?"):
        console.insert(END, "Closed the connection\n")
    else:
        console.insert(END, "The connection is still open\n")


main = Tk()
main.wm_title("Server")

#SetIP
setIPLabel = Label(main, text="Set the IP Address:").grid(row=1,column=0)
ip = StringVar()
ip.set("0.0.0.0")
setIPField = Entry(main, width=10, textvariable=ip).grid(row=1,column=1)
setIPButton = Button(main, text="Select", command=set_ip).grid(row=1,column=2,columnspan=2)

#SetPort
setPortLabel = Label(main, text="Set the Port:").grid(row=2,column=0)
port = StringVar()
port.set("12345")
setPortField = Entry(main, width=10, textvariable=port).grid(row=2,column=1)
setPortButton = Button(main, text="Select", command=set_port).grid(row=2,column=2,columnspan=2)

#Generate IP
generateIPLabel = Label(main, text="Generate an IP:").grid(row=3, column=0)
generated = StringVar()
generated.set("-.-.-.-")
generateIPField = Entry(main, width=10, textvariable=generated).grid(row=3, column=1)
generateIPButton = Button(main, text="Generate", command=generate_ip).grid(row=3,column=2,columnspan=2)

#Open/Close serving
connectionLabel = Label(main, text="Open or Close the connection:").grid(row=4,column=0)
openButton = Button(main, text="Open", command=open_connection).grid(row=4, column=2)
closeButton = Button(main, text="Close", command=close_connection).grid(row=4, column=3)

#console
console = Text(main, bg="#434A54", fg="white")
console.grid(row=8,columnspan=4)

main.mainloop()