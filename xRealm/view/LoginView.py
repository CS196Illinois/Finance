from tkinter import *
from tkinter import ttk
from pubsub import pub
from view.Home import Home


class LoginView(Frame):
    # Frame for returning users to log into existing accounts
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, padx=10, pady=10)
        username, password = Entry(self), Entry(self)
        Label(self, text="username").grid(row=0)
        Label(self, text="password").grid(row=2)
        bSignIn = Button(self, text="Begin Trading", command=lambda: verify_user(username.get(), password.get()))
        bSignUp = Button(self, text="New User? Sign up here", command=lambda: controller.show_frame(SignupView))

        username.grid(row=0, column=1), password.grid(row=2, column=1)
        bSignIn.grid(row=6, column=0, columnspan=2)
        bSignUp.grid(row=7, column=0, columnspan=2)

        self.grid_rowconfigure(1, minsize=10)
        self.grid_rowconfigure(3, minsize=43)


class SignupView(Frame):
    # Frame for new users to create new accounts
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, padx=10, pady=10)
        username, password, email = Entry(self), Entry(self), Entry(self)
        Label(self, text="username").grid(row=0)
        Label(self, text="password").grid(row=2)
        Label(self, text="e-mail").grid(row=4)
        bSignUp = Button(self, text="Begin Trading",
                         command=lambda: create_user(username.get(), password.get(), email.get()))
        bSignIn = Button(self, text="Already a user? Log in here",
                        command=lambda: controller.show_frame(LoginView))

        username.grid(row=0, column=1), password.grid(row=2, column=1)
        email.grid(row=4, column=1)
        bSignUp.grid(row=6, column=0, columnspan=2)
        bSignIn.grid(row=7, column=0, columnspan=2)

        self.grid_rowconfigure(1, minsize=10)
        self.grid_rowconfigure(3, minsize=10)
        self.grid_rowconfigure(5, minsize=10)


class NewAccount(Frame):
    # Frame for new users to open new portfolio with fresh balance
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, padx=10, pady=10)
        status = Label(self, text="The current balance in your account is " + controller.get_balance() +
                       "\n with " + controller.get_portfolio_size() + " trades in progress")
        bNewAccount = Button(self, text="Open New Account",
                         command=lambda: new_account())
        bSameAccount = Button(self, text="Continue with Current Account",
                        command=lambda: controller.show_frame(Home))

        status.grid(row=2, column=0, columnspan=2)
        bNewAccount.grid(row=6, column=0, columnspan=2)
        bSameAccount.grid(row=7, column=0, columnspan=2)

        self.grid_rowconfigure(1, minsize=10)
        self.grid_rowconfigure(3, minsize=10)
        self.grid_rowconfigure(5, minsize=10)


# Static helper methods --> Tells controller when user presses sign in/up

def verify_user(user, password):
    pub.sendMessage('verify', arg1=user, arg2=password)


def create_user(user, password, email):
    pub.sendMessage('create', arg1=user, arg2=password, arg3=email)


def new_account():
    pub.sendMessage('new_account')
