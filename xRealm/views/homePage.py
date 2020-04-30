import tkinter as tk
from tkinter import ttk
import matplotlib
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
from xRealm.models.write import Writer
from xRealm.models.EpochConverter import EpochConverter as ec
from xRealm.views.StockPage import StockDetails


matplotlib.use('TkAgg')
style.use('ggplot')


matplotlib.rcParams['xtick.labelsize'] = 7
matplotlib.rcParams['ytick.labelsize'] = 7
f = Figure(figsize = (4,5), dpi = 100)
a = f.add_subplot()

class TheApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, 'xRealm')
        
        self.container = tk.Frame(self)
        self.container.pack(side = 'top', fill = 'both', expand = True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for F in (HomePage, YoursPage, FindPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
            
        self.show_frame(HomePage)
        
    def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

    def new_details_frame(self, ticker):
        frame = StockDetails(self.container, self, ticker)
        self.frames[StockDetails] = frame
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def new_transaction(self, ticker, price, qty):
        writer = HomePage.get_writer(self.frames[HomePage])
        if not Writer.stock_exists(ticker):
            writer.add_stock(ticker)
        writer.add_transaction(ticker, price, qty)


def animate(i):
    writer = Writer()
    times = []
    amounts = []

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
    def get_writer(self):
        return self.writer
           
class YoursPage(tk.Frame):
    """A pure Tkinter scrollable frame that actually works!

                * Use the 'interior' attribute to place widgets inside the scrollable frame
                * Construct and pack/place/grid normally
                * This frame only allows vertical scrolling
                """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # create a canvas object and a vertical scrollbar for scrolling it
        vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=5, highlightthickness=5,
                           yscrollcommand=vscrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vscrollbar.config(command=canvas.yview)

        # reset the view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=tk.NW)
        back_home = tk.Button(self, text="Back to Home")
        back_home.pack()
        interior.bind('<Configure>', self._configure_interior)
        canvas.bind('<Configure>', self._configure_canvas)
        self.add_tickers()

        # track changes to the canvas and frame width and sync them,
        # also updating the scrollbar

    def _configure_interior(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # update the canvas's width to fit the inner frame
            self.canvas.config(width=self.interior.winfo_reqwidth())

    def _configure_canvas(self, event):
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # update the inner frame's width to fill the canvas
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())

    def add_tickers(self):
        writer = Writer()
        stock_names = writer.get_stock_names()
        for name in stock_names:
            btn = tk.Button(self.interior, height=1, width=20, relief=tk.FLAT,
                            bg="gray99", fg="purple3",
                            font="Dosis", text=name)
            btn.pack(padx=10, pady=5, side=tk.TOP)
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
        