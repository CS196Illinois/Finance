import tkinter as tk
window = tk.Tk()
window.title('Xrealm')
window.geometry('200x75')

var=tk.StringVar()
l = tk.Label(window,bg='yellow',width=16,text='empty')
l.pack()

def print_selection1():
    l.config(text= 'buy in this stock')
def print_selection2():
    l.config(text= 'sell out this stock')
r1=tk.Radiobutton(window,text='Buy in',variable = var, value='A',
                  command=print_selection1)
r1.pack()
r2=tk.Radiobutton(window,text='Sell out',variable = var, value='B',
                  command=print_selection2)
r2.pack()
window.mainloop()
