import tkinter as tk
from tkinter import ttk

import matplotlib
import matplotlib.animation as animation
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')

from MVP.write import Writer
from MVP.EpochConverter import EpochConverter as ec
from MVP.StockPage import StockDetails
from MVP.vertical_scroll_frame import VerticalScrolledFrame



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

    def show_home(self):
        self.show_frame(HomePage)
        
    def new_details_frame(self, ticker):
        frame = StockDetails(self.container, self, ticker)
        self.frames[StockDetails] = frame
        frame.grid(row=0, column=0, sticky='nsew')
        frame.tkraise()

    def new_transaction(self, ticker, price, qty):
        print(qty)
        if not Writer.stock_exists(ticker):
            Writer.add_stock(ticker)

        Writer.add_transaction(ticker, price, qty)
        self.show_frame(HomePage)

def animate(i):
    times = []
    amounts = []
    

    entry_array = Writer.get_progressive_balances()
    for entry in entry_array:
        times.append(ec.get_date(int(entry['time'][:10])))
        amounts.append(entry['amount'])
        
    a.clear()
    a.plot(times, amounts)
    
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = 'Home Page').pack()
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
        value = Writer.get_account_balance()
        label2 = tk.Label(self, text = 'Buying Power: $' + str(value)).pack()
        
        button1 = ttk.Button(self, text = 'Yours',
                             command = lambda: controller.show_frame(YoursPage)).pack()
        button2 = ttk.Button(self, text = 'Find',
                             command = lambda: controller.show_frame(FindPage)).pack()
           
class FindPage(tk.Frame):
    """A pure Tkinter scrollable frame that actually works!
        * Use the 'interior' attribute to place widgets inside the scrollable frame
        * Construct and pack/place/grid normally
        * This frame only allows vertical scrolling
        """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        scframe = VerticalScrolledFrame(self)
        scframe.pack()
        # scframe.grid(column=0, row=0)

        back_home = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage)).pack()
        # back_home.grid(column=0, row=1)

        valid_tickers = ["ABT", "ABBV", "ACN", "ACE", "ADBE", "ADT", "AAP", "AES", "AET", "AFL", "AMG", "A", "GAS",
                         "APD", "AKAM", "AA", "AGN", "ALXN", "ALLE", "ADS", "ALL", "ALTR", "MO", "AMZN", "AEE", "AAL",
                         "AEP", "AXP", "AIG", "AMT", "AMP", "ABC", "AME", "AMGN", "APH", "AON", "APA", "AIV", "AMAT",
                         "ADM", "AIZ", "T", "ADSK", "ADP", "AN", "AZO", "AVGO", "AVB", "AVY", "BHI", "BLL", "BAC", "BK",
                         "BAX", "BBBY", "BRK-B", "BBY", "BLX", "HRB", "BA", "BWA", "BXP", "BSK", "BMY", "CHRW", "CA",
                         "COF", "CAH", "HSIC", "KMX", "CCL", "CAT", "CELG", "CNP", "CTL", "CERN", "CF", "SCHW", "CHK",
                         "CVX", "CMG", "CB", "CI", "XEC", "CINF", "CTAS", "CSCO", "C", "CTXS", "CLX", "CME", "CMS",
                         "CCE", "CTSH", "CL", "CMCSA", "CMA", "CSC", "CAG", "COP", "CNX", "ED", "STZ", "GLW", "COST",
                         "CCI", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DLPH", "DAL", "XRAY", "DVN",
                         "DO", "DISCA", "DISCK", "DG", "DLTR", "D", "DOV", "DOW", "DD", "DUK", "DNB", "ETFC", "EMN",
                         "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMC", "EMR", "ENDP", "EOG", "EQT", "EFX", "EQIX",
                         "EQR", "ESS", "EL", "ES", "EXC", "EXPE", "EXPD", "ESRX", "XOM", "FFIV", "FB", "FAST", "FDX",
                         "FIS", "FITB", "FSLR", "FE", "FLS", "FLR", "FMC", "FTI", "F", "FOSL", "BEN", "FCX", "FTR",
                         "GME", "GPS", "GRMN", "GD", "GE", "GM", "GPC", "GNW", "GILD", "GS", "GT", "GOOGL", "GOOG",
                         "GWW", "HAL", "HBI", "HOG", "HAR", "HAS", "HCA", "HP", "HES", "HPQ", "HD", "HON", "HRL",
                         "HBAN", "ITW", "IR", "INTC", "ICE", "IBM", "IP", "IPG", "IFF", "INTU", "ISRG", "IVZ", "IRM",
                         "JEC", "JBHT", "JNJ", "JCI", "JNPR", "KSU", "K", "KEY", "KSS", "LB", "LRCX", "LM", "LEG",
                         "LEN", "LLY", "LNC", "L", "LOW", "LYB", "MTB", "MAC", "M", "MNK", "MRO", "MPC", "MAR", "MMC",
                         "MLM", "MAS", "MA", "MAT", "MKC", "MCD", "MDT", "MRK", "MET", "MU", "MSFT", "MHK", "TAP",
                         "MDLZ", "MON", "MNST", "MCO", "MS", "MOS", "MSI", "MUR", "MYL", "NDAQ", "NOV", "NAVI", "NTAP",
                         "NFLX", "NWL", "NFX", "NEM", "NWSA", "NEE", "NLSN", "NKE", "NI", "NE", "NBL", "JWN", "NSC",
                         "NTRS", "NOC", "NRG", "NUE", "NVDA", "ORLY", "OXY", "OMC", "OKE", "ORCL", "OI", "PCAR", "PLL",
                         "PH", "PDCO", "PAYX", "PNR", "PBCT", "POM", "PEP", "PKI", "PRGO", "PFE", "PCG", "PM", "PSX",
                         "PNW", "PXD", "PBI", "PCL", "PNC", "RL", "PPG", "PPL", "PX", "PCP", "PG", "PGR", "PLD", "PRU",
                         "PEG", "PSA", "PHM", "PVH", "QRVO", "PWR", "QCOM", "DGX", "RRC", "RTN", "O", "RF", "RSG",
                         "ROK", "COL", "ROP", "ROST", "RLC", "R", "CRM", "SLB", "SNI", "STX", "SEE", "SRE", "SHW",
                         "SWKS", "SLG", "SJM", "SNA", "SO", "LUV", "SWN", "SE", "HOT", "STT", "SRCL", "SYK", "STI",
                         "TROW", "TGT", "TEL", "THC", "TDC", "TXT", "HSY", "TRV", "TMO", "TIF", "TWX", "TSCO", "RIG",
                         "TRIP", "FOXA", "TSN", "UNP", "UNH", "UPS", "URI", "UTX", "UHS", "UNM", "URBN", "VFC", "VLO",
                         "VAR", "VTR", "VRSN", "VZ", "VRTX", "VIAB", "V", "VNO", "VMC", "WMT", "WBA", "DIS", "WM",
                         "WAT", "ANTM", "WFC", "WDC", "WU", "WY", "WHR", "WEC", "XEL", "XRX", "XLNX", "XL", "XYL",
                         "ZBH", "ZION", "ZTS"]

        for ticker in valid_tickers:
            btn = tk.Button(scframe.interior, height=1, width=20, relief=tk.FLAT,
                            bg="gray99", fg="purple3",
                            font="Dosis", text=ticker, command=lambda ticker=ticker: controller.new_details_frame(ticker))
            btn.pack(padx=10, pady=5, side=tk.TOP)

class YoursPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        scframe = VerticalScrolledFrame(self)
        scframe.pack()

        back_home = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(HomePage)).pack()

        stock_names = Writer.get_stock_names()
        for ticker in stock_names:
            btn = tk.Button(scframe.interior, height=1, width=20, relief=tk.FLAT,
                            bg="gray99", fg="purple3",
                            font="Dosis", text=ticker, command=lambda ticker=ticker: controller.new_details_frame(ticker))
            btn.pack(padx=10, pady=5, side=tk.TOP)

Writer.new_user_setup()
app = TheApp()
ani = animation.FuncAnimation(f, animate, interval = 1000)
app.mainloop()
        