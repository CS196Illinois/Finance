import tkinter as tk

HEIGHT = 800
WIDTH = 200

# colors used in this watching window
ColorBack = '#1E1F23'
ColorBull = '#55A36F'
ColorBear = '#C64353'
ColorFont = '#FCF2F4'
ColorName = '#E4BB63'
ColorBloc = '#393E46'
ColorSell = '#F19236'
ColorBuy  = '#4F90F7'

window = tk.Tk()

# the background
canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH, bg=ColorFont)
canvas.pack()

# the boundary of the watching window
StockList = tk.Frame(canvas, bg=ColorBack)
StockList.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

title = tk.Label(StockList, text='My Favorite Stocks', bg=ColorBloc, fg=ColorFont)
title.pack(side='top', fill='x')

trade = tk.Frame(StockList, bg=ColorBloc)
trade.place(relx=0, rely=0.85, relwidth=1, relheight=0.15)

sellButton = tk.Button(trade, text='sell', bg=ColorSell)
sellButton.place(relx=0, rely=0, relwidth=1, relheight=0.5)

buyButton = tk.Button(trade, text='buy', bg=ColorBuy)
buyButton.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)




#ex1 = tk.Frame(StockList, bg=ColorBloc)
#ex1.grid(row=0, column=0)

window.mainloop()