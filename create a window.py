from tkinter import *

window = Tk()

# here I create the window size.
window.geometry('400x400')

window.title("Welcome to stock page")

# create the label and set its place and size.
lbl = Label(window, text = "STOCK", font = ("Arial Bold", 10))

lbl.grid(column = 0, row = 0)

# create buttons here. 
btn = Button(window, text = "Sell The Stock", bg = "black", fg = "red")

# the reaction after the click 
def clicked():
    lbl.configure(text = "Stock was sold!")
    
btn = Button(window, text = "Sell The Stock", command = clicked)

# the location of the button
# if botton is in the same place as lable, it will cover it
btn.grid(column = 1, row = 0)






# This is to make sure that users can access it!
window.mainloop()

