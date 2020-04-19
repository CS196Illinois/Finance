# Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk

window = tk.Tk()
window.title('stock detail')

window.geometry('800x400')

var2 = tk.StringVar()
l1 = tk.Label(window, textvariable=var2, bg='green',font=('Arial',14),width=15,height=2)
var2.set("getprice()")
l1.pack()

"""""
on_hit = False
def hit_me():
	global on_hit
	if on_hit == False:
	   on_hit = True
	   var.set('purchase succeeds')

def hit_me():
	global on_hit
	if on_hit == False:
	   on_hit = True
	   var.set('purchase succeeds')
	else:
	  on_hit=False
	  var.set('')
"""
# general label
genLbl = tk.Label(window, text = "STOCK", font = ("Arial Bold", 10))
# genLbl.grid(column = 2, row = 0)
# the info label
infoLbl = tk.Label(window, text = "INFORMATION", font = ("Arial Bold", 10))
# infoLbl.grid(column = 2, row = 1)
# the note label
noteLbl = tk.Label(window, text = "YOUR NOTES", font = ("Arial Bold", 10))
# noteLbl.grid(column = 2, row = 2)
# create the label and set its place and size.
decideLbl = tk.Label(window, text = "YOUR DECISION", font = ("Arial Bold", 10))
# decideLbl.grid(column = 2, row = 4)



#add txt box here
noteText = tk.Entry(window, width = 10)
# noteText.grid(column = 3, row = 2)

sellingText = tk.Entry(window, width = 10)
# sellingText.grid(column = 3, row = 4)

buyingText = tk.Entry(window, width = 10)
# buyingText.grid(column = 3, row = 5)


# create buttons here.
btn0 = tk.Button(window, text = "Save Your Notes")

btn1 = tk.Button(window, text = "Sell The Stock")

btn2 = tk.Button(window, text = "Buy The Stock")

btn3 = tk.Button(window, text = "Stock Prices")

# the reaction after the click
def clicked0():
    noteLbl.configure(text = noteText.get(), bg = "white", fg = "black")
   
def clicked1():
    decideLbl.configure(text = "Stock **" + sellingText.get() + "** was sold!", bg = "black", fg = "red")
    var1.set("you have " + "getQuantity() - 1")
    var3.set("you have getAccount() + getPrice()")
   
def clicked2():
    decideLbl.configure(text = "Stock **" + buyingText.get() + "** was bought!", bg = "yellow", fg = "green")
    var1.set("you have " + "getQuantity() + 1")
    var3.set("you have getAccount() - getPrice()")

def clicked3():
    decideLbl.configure(text = "Stock **" + buyingText.get() + "The price of ** is **", bg = "black", fg = "red")

    

   
# operations of buttons
btn0 = tk.Button(window, text = "Save Your Notes", command = clicked0)
btn0.pack()

btn1 = tk.Button(window, text = "Sell The Stock", command = clicked1)
btn1.pack()

btn2 = tk.Button(window, text = "Buy The Stock", command = clicked2)
btn2.pack()

btn3 = tk.Button(window, text = "Stock Price", command = clicked3)
btn3.pack()

var1 = tk.StringVar()
l2 = tk.Label(window, textvariable=var1, bg='green',width = 100)
var1.set("you have " + "getQuantity()")
l2.pack()

var3 = tk.StringVar()
l3 = tk.Label(window, textvariable=var3, bg='green',width = 100)
var3.set("you have " + "getaccount")
l3.pack()
# the location of the button
# button will be over txt and label if they are at the same place.
# btn0.grid(column = 4, row = 2)
# btn1.grid(column = 4, row = 4)
# btn2.grid(column = 4, row = 5)
# btn3.grid(column = 4, row = 6)
window.mainloop()
