import json
import time as t

class Writer:
    """
    The class that creates, edits and reads the user data
    ...
    Attributes
    ----------
    user : dict
        A dictionary containing the relevant user information that is turned into a json object when saved as a file
    Methods
    -------
    update_account_balance(balance)
        Updates the account balance of the user
    update_previous_account_values(value)
        Creates a dictionary that stores the total account value and the time in microseconds since epoch
        and adds it to the end of an array
    add_stock(name)
        Adds a new stock type to the portfolio
    add_transaction(name, price, quantity)
        Adds a new transaction to the stock in the portfolio along with its price, quantity and time in microseconds
        since epoch
    get_current_quantity(name)
        Returns the total quantity of a specified stock owned by the user as an int
    get_portfolio()
        Returns the portfolio of the user as a dictionary
    get_progressive_balances()
        Returns a list of dictionaries containing balances and time in microseconds since epoch
    get_account_balance()
        Returns the account balance of the user as a double
    get_stock_names()
        Returns a list of the stock names
    to_json()
        Stores the user dictionary as a json object
    write_file()
        Writes the user dictionary onto a text file
    """

    user = {}

    @staticmethod
    def new_user_setup():
        with open('user.txt', 'r+') as jsonfile:
            file = json.load(jsonfile)
            Writer.user['portfolio'] = file['portfolio']
            Writer.user['account_balance'] = file['account_balance']
            Writer.user['previous_account_values'] = file['previous_account_values']
            Writer.user['stock_names'] = file['stock_names']

    @staticmethod
    def update_account_balance(balance):
        """ Updates the account value of the user and writes it into text file.
        :param balance: (double) The new account value
        :return: none
        """

        Writer.user['account_balance'] = balance
        Writer.write_file()

    @staticmethod
    def update_previous_account_values(value):
        """ Creates a dictionary that stores the total account value and the time in microseconds since epoch
        and adds it to the end of an array and then updates the text file.
        :param value: (double) The new total account value which is stored along with time since epoch
        :return: none
        """

        to_add = {
            'time' : str(round(t.time() * 1000000)),
            'amount' : value
        }
        Writer.user['previous_account_values'].append(to_add)
        Writer.write_file()

    @staticmethod
    def add_stock(name):
        """ Adds a new stock type to the portfolio and then updates the text file.
        :param name: (str) The name of the new kind of stock
        :return: none
        """

        Writer.user["portfolio"][name] = {'current_qty' : 0, 'transactions' : {}}
        Writer.user['stock_names'].append(name)


        Writer.write_file()


    @staticmethod
    def stock_exists(ticker):
        """ Adds a new stock type to the portfolio and then updates the text file.

        :param ticker: (str) The name of the stock
        :return: none
        """
        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)["portfolio"]
        for name in file:
            print(name)
            if str(name) == ticker:
                return True
        return False

    @staticmethod
    def add_transaction(name, price, quantity):
        """ Adds a new transaction to the stock in the portfolio along with its price, quantity and time in microseconds
        since epoch and updates the text file.
        :param name: (str) The name of the stock
        :param price: (double) Price of stock during transaction
        :param quantity: (int) The quantity of the stock being transacted
        :return: none
        """
        time = round(t.time() * 1000000)

        Writer.user['portfolio'][name]['transactions'][str(round(t.time() * 1000000)) + name.upper()] = {
            'price' : price,
            'quantity' : quantity,
            'time' : time
        }
        current = Writer.user['portfolio'][name]["current_qty"]
        total = current + int(quantity)
        Writer.user['portfolio'][name]["current_qty"] = total


        Writer.write_file()

    @staticmethod
    def get_current_quantity(name):
        """ Returns the total quantity of a specified stock owned by the user as an int.
        :param name: (str) The name of the stock
        :return: (int) The quantity of stocks
        """

        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            return file['portfolio'][name]["current_qty"]

    @staticmethod
    def get_portfolio():
        """ Returns the portfolio of the user.
        :return: (dict) the portfolio of the user
        """

        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            return file['portfolio']

    @staticmethod
    def get_progressive_balances():
        """ Returns the previous account values and the time they were saved since epoch
        :return: (list) a list containing the previous account values and the time they were saved since epoch
        """

        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            return file['previous_account_values']

    @staticmethod
    def get_account_balance():
        """ Returns the account balance of the user.
        :return: (double) the account balance
        """

        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            return file['account_balance']

    @staticmethod
    def get_stock_names():
        """ Returns the stock names.
        :return: (List) the stock names
        """

        with open('user.txt', 'r') as jsonfile:
            file = json.load(jsonfile)
            return file['stock_names']

    @staticmethod
    def to_json():
        """ Converts the user to json object.
        :return: none
        """

        return json.dumps(Writer.user, indent=4, sort_keys=True)
        print(Writer.user)

    @staticmethod
    def write_file():
        """ Writes the user onto a text file.
        :return: none
        """

        with open('user.txt', 'r+') as jsonfile:
            json.dump(Writer.user, jsonfile, indent=4, sort_keys=True)
