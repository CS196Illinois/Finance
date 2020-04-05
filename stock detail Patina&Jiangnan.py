Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
>>> window = tk.Tk()
>>> window.title('stock detail')
''
>>> window.geometry('200x100')
''
>>> var = tk.StringVar()
>>> l = tk.Label(window, textvariable=var, bg='black',font=('Arial',14),width=15,height=2)
>>> l.pack()
>>> on_hit = False
>>> def hit_me():
	global on_hit
	if on_hit == False:
	   on_hit = True
	   var.set('purchase succeeds')

>>> def hit_me():
	global on_hit
	if on_hit == False:
	   on_hit = True
	   var.set('purchase succeeds')
	else:
	  on_hit=False
	  var.set('')

>>> # general label
genLbl = Label(window, text = "STOCK", font = ("Arial Bold", 10))
genLbl.grid(column = 2, row = 0)
# the info label
infoLbl = Label(window, text = "INFORMATION", font = ("Arial Bold", 10))
infoLbl.grid(column = 2, row = 1)
# the note label
noteLbl = Label(window, text = "YOUR NOTES", font = ("Arial Bold", 10))
noteLbl.grid(column = 2, row = 2)
# create the label and set its place and size.
decideLbl = Label(window, text = "YOUR DECISION", font = ("Arial Bold", 10))
decideLbl.grid(column = 2, row = 4)



#add txt box here
noteText = Entry(window, width = 10)
noteText.grid(column = 3, row = 2)

sellingText = Entry(window, width = 10)
sellingText.grid(column = 3, row = 4)

buyingText = Entry(window, width = 10)
buyingText.grid(column = 3, row = 5)


# create buttons here.
btn0 = Button(window, text = "Save Your Notes")

btn1 = Button(window, text = "Sell The Stock")

btn2 = Button(window, text = "Buy The Stock")

btn3 = Button(window, text = "Stock Prices")

# the reaction after the click
def clicked0():
    noteLbl.configure(text = noteText.get(), bg = "white", fg = "black")
   
def clicked1():
    decideLbl.configure(text = "Stock **" + sellingText.get() + "** was sold!", bg = "black", fg = "red")
   
def clicked2():
    decideLbl.configure(text = "Stock **" + buyingText.get() + "** was bought!", bg = "yellow", fg = "green")

def clicked3():
    decideLbl.configure(text = "Stock **" + buyingText.get() + "The price of ** is **", bg = "black", fg = "red")

    

   
# operations of buttons
btn0 = Button(window, text = "Save Your Notes", command = clicked0)
btn1 = Button(window, text = "Sell The Stock", command = clicked1)
btn2 = Button(window, text = "Buy The Stock", command = clicked2)
btn3 = Button(window, text = "Stock Price", command = clicked3)



# the location of the button
# button will be over txt and label if they are at the same place.
btn0.grid(column = 4, row = 2)
btn1.grid(column = 4, row = 4)
btn2.grid(column = 4, row = 5)
btn3.grid(column = 4, row = 6)
