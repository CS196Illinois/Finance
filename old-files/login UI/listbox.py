import tkinter as tk

window = tk.Tk()
window.title('LogIN Page')
window.geometry('200x200')

var1 =tk.StringVar()
l=tk.Label(window,bg='yellow',width=16,textvariable=var1)
l.pack()
var1.set('please select one')
def print_selection():
    value = lb.get(lb.curselection())
    
    var1.set(value)

b1 = tk.Button(window, text='print selection', width=15,
              height=2, command=print_selection)
b1.pack()
var2 = tk.StringVar()
var2.set(('stock a','stock b','stock c','stock d'))
lb = tk.Listbox(window,listvariable = var2)
#list_items=[1,2,3,4]
#for item in list_items:
 #   lb.insert('end',item)
lb.insert(1,'stock e')
lb.insert(2,'stock f')
lb.insert(3,'stock g')
lb.insert(4,'stock h')
lb.pack()
window.mainloop()
