from tkinter import *
# as direction in google, we import matplotlib here.
import matplotlib
from pandas import DataFrame

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from pandas import DataFrame
import matplotlib.pyplot as plt

window = Tk()

# here I create the window size.
window.geometry('300x200')

window.title("Stock Page")

# general label
genLbl = Label(window, text="STOCK", font=("Arial Bold", 10))
genLbl.grid(column=2, row=0)
# the info label
infoLbl = Label(window, text="INFORMATION", font=("Arial Bold", 10))
infoLbl.grid(column=2, row=1)
# the note label
noteLbl = Label(window, text="YOUR NOTES", font=("Arial Bold", 10))
noteLbl.grid(column=2, row=2)
# create the label and set its place and size.
decideLbl = Label(window, text="YOUR DECISION", font=("Arial Bold", 10))
decideLbl.grid(column=2, row=4)

# add txt box here
noteText = Entry(window, width=10)
noteText.grid(column=3, row=2)

# create buttons here.
btn0 = Button(window, text="Save Your Notes")

btn1 = Button(window, text="Sell The Stock")

btn2 = Button(window, text="Buy The Stock")


# the reaction after the click
def clicked0():
    noteLbl.configure(text=noteText.get(), bg="white", fg="black")


def clicked1():
    decideLbl.configure(text="Stock **" + "** was sold!", bg="black", fg="red")


def clicked2():
    decideLbl.configure(text="Stock **" + "** was bought!", bg="yellow", fg="green")


# operations of buttons
btn0 = Button(window, text="Save Your Notes", command=clicked0)
btn1 = Button(window, text="Sell The Stock", command=clicked1)
btn2 = Button(window, text="Buy The Stock", command=clicked2)

# the location of the button
# button will be over txt and label if they are at the same place.
btn0.grid(column=4, row=2)
btn1.grid(column=4, row=4)
btn2.grid(column=4, row=5)

# here I insert a graph 2020/4/12
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = {'Year': ['2015', '2016', '2017', '2018', '2019'],
         'ROE%': [129.20, 25.68, 24.40, 22.73, 27.90]
         }
df1 = DataFrame(data1, columns=['Year', 'ROE%'])

data2 = {'Year': ['2015-07', '2016-07', '2017-07', '2018-07', '2019-07'],
         'Last Price': [9.8, 12, 8, 7.2, 6.9]
         }
df2 = DataFrame(data2, columns=['Year', 'Last Price'])

root = tk.Tk()

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Year', 'ROE%']].groupby('Year').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.set_title('Year Vs. ROE')

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Year', 'Last Price']].groupby('Year').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Year Vs. Last Price')

root.mainloop()

# This is to make sure that users can access it!
window.mainloop()

