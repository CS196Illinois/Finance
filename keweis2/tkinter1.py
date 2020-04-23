import tkinter as tk

window = tk.Tk()
window.title('Xrealm')
window.geometry('800x400')
var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='yellow', font=('Arial', 12)
             , width=100, height=2)
l.pack()
var.set('choose the one you want to purchase')


def hit_me():
    var.set('sucessful purchase')


b = tk.Button(window, text='purchase', width=15, height=2, command=hit_me)
b.pack()
window.mainloop()
