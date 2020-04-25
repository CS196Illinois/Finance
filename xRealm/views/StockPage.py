
import tkinter as tk
from tkinter import ttk

import matplotlib
from matplotlib import style
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from xRealm.models.StockData import StockData

import matplotlib.animation as animation

import urllib
import json

import numpy as np

from tkinter import *



LARGE_FONT= ("Verdana", 12)
style.use("ggplot")

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)

# Global variables to graph stock
ticker = "MSFT"
time_interval = "1d"



def animate():
    data = StockData.getHistoricalPrices(ticker, time_interval)
    xList = []
    yList = []
    for date in data:
        if str(date) is not "":
            xList.append(str(date))
            yList.append(float(data[date]))
    a.clear()
    a.plot(xList, yList)


class StockDetails(tk.Frame):
    def __init__(self, parent, controller, tik):
        global ticker
        ticker = tik

        tk.Frame.__init__(self, parent)

        self.update_animation(ticker)

        label = tk.Label(self, text="Stock Details: " + ticker, font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StockDetails))
        button1.pack()

        oneHour = ttk.Button(self, text="5M",
                             command=lambda: self.setTimeInterval("5m", controller))
        oneHour.pack()

        oneHour = ttk.Button(self, text="1H",
                             command=lambda: self.setTimeInterval("60m", controller))
        oneHour.pack()

        oneDay = ttk.Button(self, text="1D",
                             command=lambda: self.setTimeInterval("1d", controller))
        oneDay.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

        quantity = Entry(self)
        quantity.pack()

        button2 = ttk.Button(self, text="Buy",
                            command=lambda: controller.show_frame(StockDetails))
        button2.pack()

        button3 = ttk.Button(self, text = "Sell",
                            command =lambda: controller.show_frame(self))
        button3.pack()

    def setTimeInterval(self, interval, controller):
        global time_interval
        time_interval = interval
        self.update_animation()
        controller.new_details_frame(ticker)

    def update_animation(self, tick=None):
        if tick is not None:
            global ticker
            ticker = tick
        animation.FuncAnimation(f, animate(), interval=1000)
