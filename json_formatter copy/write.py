import json
import time as t

class Writer:

    user = {}

    def __init__(self):
        Writer.user['portfolio'] = {}
        Writer.user['account_balance'] = 0.0
        Writer.user['previous_account_values'] = []

    def update_account_balance(self, balance):
        Writer.user['account_balance'] = balance
        self.write_file()

    def update_previous_account_values(self, value):
        to_add = {
            'time' : str(round(t.time() * 1000000)),
            'amount' : value
        }
        Writer.user['previous_account_values'].append(to_add)
        self.write_file()

    def add_stock(self, name):
        Writer.user['portfolio'][name] = {
            'current_qty' : 0,
            'transactions' : {}
        }
        self.write_file()

    def add_transaction(self, name, price, quantity):
        Writer.user['portfolio'][name]['transactions'][str(round(t.time() * 1000000)) + name.upper()] = {
            'price' : price,
            'quantity' : quantity,
            'time' : round(t.time() * 1000000)
        }
        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            current = file['portfolio'][name]["current_qty"]
            total = current + quantity

        Writer.user['portfolio'][name]["current_qty"] = total
        self.write_file()


    def get_current_quantity(self, name):
        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            return file['portfolio'][name]["current_qty"]

    def to_json(self):
        return json.dumps(Writer.user, indent=4, sort_keys=True)

    def write_file(self):
        with open('user.txt', 'w') as jsonfile:
            json.dump(Writer.user, jsonfile, indent=4, sort_keys=True)

    def get_portfolio(self, name):
        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            return file['portfolio'][name]["transactions"]

    def get_progressive_balances(self):
        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            return file['previous_account_values']

    def get_account_balance(self):
        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            return file['account_balance']
