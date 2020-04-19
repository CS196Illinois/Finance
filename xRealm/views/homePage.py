import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.animation as animation
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')

from ..models import *
from write import Writer
from EpochConverter import EpochConverter as ec



matplotlib.rcParams['xtick.labelsize'] = 7
matplotlib.rcParams['ytick.labelsize'] = 7
f = Figure(figsize = (4,5), dpi = 100)
a = f.add_subplot()

class TheApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, 'xRealm')
        
        container = tk.Frame(self)
        container.pack(side = 'top', fill = 'both', expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for F in (HomePage, YoursPage, FindPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
            
        self.show_frame(HomePage)
        
    def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

def animate(i):
    writer = Writer()
    times = []
    amounts = []
    
    writer = Writer()
    entry_array = writer.get_progressive_balances()
    for entry in entry_array:
        times.append(ec.get_date(int(entry['time'][:10])))
        amounts.append(entry['amount'])
        
    a.clear()
    a.plot(times, amounts)
    
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        self.writer = Writer()
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Home Page').pack()
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
        value = self.writer.get_account_balance()
        label2 = tk.Label(self, text = 'Buying Power: $' + str(value)).pack()
        
        button1 = ttk.Button(self, text = 'Yours',
                             command = lambda: controller.show_frame(YoursPage)).pack()
        button2 = ttk.Button(self, text = 'Find',
                             command = lambda: controller.show_frame(FindPage)).pack()
           
class YoursPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Yours page')
        label.pack()
        
        button1 = ttk.Button(self, text = 'Back to home',
                             command = lambda: controller.show_frame(HomePage))
        button1.pack()

class FindPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Find Page')
        label.pack()
        button1 = ttk.Button(self, text = 'Back to home',
                             command = lambda: controller.show_frame(HomePage)).pack()
        

app = TheApp()
ani = animation.FuncAnimation(f, animate, interval = 1000)
app.mainloop()
        