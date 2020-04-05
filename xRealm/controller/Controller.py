from tkinter import *
import tkinter.ttk as ttk
from view.LoginView import LoginView, SignupView, NewAccount
from view.Home import Home
from pubsub import pub
from ttkthemes import themed_tk as tk
from model.Model import Model


class XRealm(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("xRealm: Market Sim")
        self.geometry('400x600')
        self.current_view = LoginView
        self.user = {}
        self.model = Model()

        pub.subscribe(self.verify_user, 'verify')
        pub.subscribe(self.create_user, 'create')
        pub.subscribe(self.login_error, 'login_error')
        pub.subscribe(self.new_account, 'new_account')

        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginView, SignupView, Home):
            self.create_frame(F)

        self.show_frame(self.current_view)

    # Creates each Frame (aka page) and stores it in frames list
    def create_frame(self, cont):
        frame = cont(self.container, self)
        self.frames[cont] = frame

    # Shows the specified frame in this Tk
    def show_frame(self, cont):
        self.frames[self.current_view].place_forget()
        frame = self.frames[cont]
        self.current_view = cont
        frame.place(anchor="c", relx=.5, rely=.5)
        frame.tkraise()

    # Called from "sign in" button to verify user
    def verify_user(self, arg1, arg2):
        if self.model.verify_user(arg1, arg2):
            self.user = self.model.pull_user()
            self.create_frame(NewAccount)
            self.show_frame(NewAccount)

    # Called from "sign up" button to create user
    def create_user(self, arg1, arg2, arg3):
        if self.model.create_user(arg1, arg2, arg3):
            self.user = self.model.pull_user()
            self.show_frame(Home)

    # Called when user entered any information incorrectly
    def login_error(self, arg1):
        label = Label(self, text=arg1)
        label.place(anchor='c', relx=.5, rely=.8)
        label.after(3000, lambda: label.destroy())

    # Called from "Open New Account" button to open a new account with a fresh balance
    def new_account(self):
        self.model.new_account()
        self.show_frame(Home)

    # Getters
    def get_balance(self):
        return str(self.user['balance'])

    def get_portfolio_size(self):
        return str(len(self.user['portfolio']))


if __name__ == '__main__':
    view = XRealm()
    view.mainloop()
