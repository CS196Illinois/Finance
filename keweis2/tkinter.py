"""""""""
MUST BE RUN AT IDLE





import tkinter as tk
window = tk.Tk()
window.geometry('200x100')
window.title('赵菁雨是个大傻蛋')
l=tk.label(window,text="OMG!this is TK!",bg='green',font=('Arial',12),width=15,height=2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    l=tk.label(window,text="OMG!this is TK!",bg='green',font=('Arial',12),width=15,height=2)
AttributeError: module 'tkinter' has no attribute 'label'
>>> 
>>> l=tk.Label(window,text="OMG!this is TK!",bg='green',font=('Arial',12),width=15,height=2)
>>>  l=tk.Label(window,text="赵菁雨是个大傻蛋",bg='green',font=('Arial',12),width=15,height=2)
 
SyntaxError: unexpected indent
>>> l=tk.Label(window,text="赵菁雨是个大傻蛋",bg='green',font=('Arial',12),width=15,height=2)
>>> l.pack()
>>> b = tk.Botton(window,text='hit me', width =15,height=2,command= hit_me )
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b = tk.Botton(window,text='hit me', width =15,height=2,command= hit_me )
AttributeError: module 'tkinter' has no attribute 'Botton'
>>> b = tk.Button(window,text='hit me', width =15,height=2,command= hit_me )
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    b = tk.Button(window,text='hit me', width =15,height=2,command= hit_me )
NameError: name 'hit_me' is not defined
>>> var = tk.StringVar()
>>> b = tk.Button(window,textvariable= var, width =15,height=2,command= hit_me )
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b = tk.Button(window,textvariable= var, width =15,height=2,command= hit_me )
NameError: name 'hit_me' is not defined
>>> on_hit = False
>>> def hit_me():
	global on_hit
	if on_hit == False:
		
		var.set('赵菁雨是大笨蛋吗')
		on_hit= True

	else:
		on_hit=False
		var.set('不，赵菁雨是大傻蛋')

		
>>> b = tk.Button(window,textvariable= var, width =15,height=2,command= hit_me )
>>> b.pack()
>>> 
"""""