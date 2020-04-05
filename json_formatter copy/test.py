from write import Writer

def test():

    writer = Writer()
    # creation of object yields empty user
    print("output 1")
    print(writer.to_json())

    # update_account_balance updates account balance
    writer.update_account_balance(100000.0)
    print("output 2")
    print(writer.to_json())

    #add stock adds a new stock to profile
    writer.add_stock("apple")
    writer.add_stock("orange")
    writer.add_stock("lemon")
    writer.add_stock("penguin")
    writer.add_stock("blue")
    print("output 3")
    print(writer.to_json())

    # add transaction adds transaction with unique ID to specified stock
    writer.add_transaction("apple", 50.0, 10)
    writer.add_transaction("apple", 40.0, 30)
    writer.add_transaction("apple", 20.0, 50)
    writer.add_transaction("apple", 90.0, -10)
    writer.add_transaction("apple", 40.0, 20)
    writer.add_transaction("orange", 20.0, 40)
    writer.add_transaction("orange", 40.0, -20)
    writer.add_transaction("orange", 50.0, -10)
    writer.add_transaction("lemon", 20.0, 40)
    writer.add_transaction("lemon", 40.0, 20)
    writer.add_transaction("lemon", 70.0, -10)
    writer.add_transaction("penguin", 80.0, 120)
    writer.add_transaction("blue", 90.0, 10)
    writer.add_transaction("blue", 60.0, 30)
    writer.add_transaction("blue", 20.0, -20)
    print("output 4")
    print(writer.to_json())

    # update previous account values stores the account value and the time of recording
    writer.update_previous_account_values(10)
    writer.update_previous_account_values(100)
    writer.update_previous_account_values(1000)
    writer.update_previous_account_values(10000)
    writer.update_previous_account_values(10000)
    writer.update_previous_account_values(10000)
    writer.update_previous_account_values(1000)
    writer.update_previous_account_values(100)
    writer.update_previous_account_values(10)
    print("output 5")
    print(writer.to_json())

    # write file writes the python dictionary in json format on file user.txt
    writer.write_file()



test()