from tkinter import *
from tkinter import ttk
from pubsub import pub


class Home(Frame):
    # Frame for returning users to log into their accounts
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, padx=10, pady=10)
        label = Label(self, text="HOME")
        label.grid(row=0, column=0, columnspan=2)