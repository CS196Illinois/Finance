import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.animation as animation
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')

matplotlib.rcParams['xtick.labelsize'] = 7
matplotlib.rcParams['ytick.labelsize'] = 7
f = Figure(figsize = (4,5), dpi = 100)
a = f.add_subplot()

class TheApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
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
    pullData = open('sampleData.txt', 'r').read()
    dataList = pullData.split("\n")
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(float(x))
            yList.append(float(y))
    a.clear()
    a.plot(xList, yList)
            
    
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Home Page')
        label.pack()
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
        #toolbar = NavigationToolbar2Tk(canvas, self)
        #toolbar.update()
        #canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
        # unpack sampleData
        pullData = open('sampleData.txt', 'r').read()
        dataList = pullData.split('\n')
        last_pair = dataList[-1]
        as_two = last_pair.split(',')
        cash = float(as_two[1])
        
        label2 = tk.Label(self, text = 'Net worth: ' + str(cash))
        label2.pack()
        
        button1 = ttk.Button(self, text = 'Yours',
                             command = lambda: controller.show_frame(YoursPage))
        button1.pack()
        
        button2 = ttk.Button(self, text = 'Find',
                             command = lambda: controller.show_frame(FindPage))
        button2.pack()
        
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
                             command = lambda: controller.show_frame(HomePage))
        button1.pack()

app = TheApp()
ani = animation.FuncAnimation(f, animate, interval = 1000)
app.mainloop()
        