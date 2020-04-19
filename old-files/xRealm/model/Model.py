import json
from pubsub import pub
import time


class Model:
    def __init__(self):
        # Opens the json file to read from or creates new if none
        with open("../data/users.json", 'r+') as readfile:
            file = json.load(readfile)
            self.json_users = file["users"]
            self.user_index = -1
            self.start_time = time.time()
        readfile.close()
        return

    # True if a username is found in the database. Sets the index of that user to user_index
    def user_exists(self, username):
        for user in self.json_users:
            if user['username'] == username:
                self.user_index = self.json_users.index(user)
                return True
        return False

    # Called from Login screen. Verifies username and password. True if successful, false otherwise
    def verify_user(self, username, password):
        if self.user_exists(username):
            if self.json_users[self.user_index]["password"] == password:
                return True
            else:
                pub.sendMessage('login_error', arg1="Your password is incorrect")
                return False
        else:
            pub.sendMessage('login_error', arg1="Your username is incorrect")
            return False

    # Called from Login screen. Adds new user to json. True if successful, false otherwise
    def create_user(self, username, password, email):
        if self.user_exists(username):
            pub.sendMessage('login_error', arg1="This username already exists. Please choose another.")
            return False
        new_user = {"username": username,
                    "password": password,
                    "email": email,
                    "portfolio": [],
                    "balance": 50000,
                    "accounts": []}

        self.start_time = time.time()

        with open("../data/users.json", 'r+') as writefile:
            users = json.load(writefile)
            users["users"].append(new_user)
            writefile.seek(0)
            json.dump(users, writefile, indent=4)
            self.json_users = users['users']
            return True

    # Called from Login screen. Returns user data as list
    def pull_user(self):
        return self.json_users[self.user_index]

    # Called when user wants to open a new account with a fresh balance
    def new_account(self):
        new_account = {
            "epoch": self.start_time,
            "balance": self.json_users[self.user_index]['balance']
        }
        self.start_time = time.time()
        with open("../data/users.json", 'r+') as writefile:
            users = json.load(writefile)
            users['users'][self.user_index]['accounts'].append(new_account)
            users['users'][self.user_index]['balance'] = 50000
            writefile.seek(0)
            json.dump(users, writefile, indent=4)
            self.json_users = users['users']