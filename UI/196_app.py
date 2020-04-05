import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')

f = Figure(figsize = (4,4), dpi = 100)
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

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Home Page')
        label.pack()
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
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
app.mainloop()
        