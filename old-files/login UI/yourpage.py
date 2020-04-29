import tkinter as tk
import pickle
import tkinter.messagebox
window = tk.Tk()
window.title('Your main page')
window.geometry('900x600')
var1 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=16, textvariable=var1)
l.pack()
var1.set('Stock at hand')


def print_selection():
    value = lb.get(lb.curselection())

    var1.set(value)


b1 = tk.Button(window, text='print selection', width=15,
               height=2, command=print_selection)
b1.pack()
var2 = tk.StringVar()
# var2.set(('stock a', 'stock b', 'stock c', 'stock d'))
lb = tk.Listbox(window, listvariable=var2, width = 46)

# list_items=[1,2,3,4]
# for item in list_items:
#   lb.insert('end',item)
# lb.insert(1, 'stock e')
# lb.insert(2, 'stock f')
# lb.insert(3, 'stock g')
# lb.insert(4, 'stock h')
lb.pack()

"""""
var5 = tk.StringVar()
tem = tk.Label(window, bg='yellow', width=16, textvariable=var5)
var5.set("wait for your decision")
"""
var5 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=100, textvariable=var5)
l.pack()
var5.set('wait for your selection')
def buy_command():
    var5.set("I press the buy button. I need to increase something in list. And my account balance will decrease")
    lb.insert(4, 'stock neeeeewww           getPrice()          getQuantity()')


buybutton = tk.Button(window, text='addbutton', width=15, height=2, command=buy_command)
buybutton.pack()



var6 = tk.StringVar()
l = tk.Label(window, bg='yellow', width=100, textvariable=var6)
l.pack()
var6.set('wait for your selection')
def sell_command():
    var6.set("I press the sell button. I need to decrease something in list. And my account balance will increase")
    lb.delete(lb.curselection())


sellbutton = tk.Button(window, text='sellbutton', width=15, height=2, command=sell_command)
sellbutton.pack()

"""""
def trade_detail(self):
    self.page.destroy()


tradebutton = tk.Button(window, text='trade detail', width=15, height=2, command=trade_detail)
tradebutton.pack()
"""

window.mainloop()
