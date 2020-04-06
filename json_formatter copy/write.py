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

    def update_previous_account_values(self, value):
        to_add = {
            'time' : str(round(t.time() * 1000000)),
            'amount' : value
        }
        Writer.user['previous_account_values'].append(to_add)

    def add_stock(self, name):
            Writer.user['portfolio'][name] = {
                'current_qty' : 0,
                'transactions' : {}
            }

    def add_transaction(self, name, price, quantity):
        Writer.user['portfolio'][name]['transactions'][str(round(t.time() * 1000000)) + name.upper()] = {
            'price' : price,
            'quantity' : quantity,
            'time' : round(t.time() * 1000000)
        }

    def to_json(self):
        return json.dumps(Writer.user, indent=4, sort_keys=True)

    def write_file(self):
        with open('user.txt', 'w') as jsonfile:
            json.dump(Writer.user, jsonfile, indent=4, sort_keys=True)
