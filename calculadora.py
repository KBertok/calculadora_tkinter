import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()
frame=tk.Frame(win)
frame.grid()
win.title("Calculadora")
win.geometry('300x200')


expr=''
text=tk.StringVar()

def press(num):
   global expr 
   expr += str(num)
   text.set(expr)

def clr():
    global expr
    expr = ''
    text.set(expr)

def equal():
    global expr
    total = str(eval(expr))
    text.set(total)


answer=ttk.Entry(frame, justify='right', textvariable=text)
answer.grid(row=0, columnspan=4, sticky='nsew')


boton7 = ttk.Button(frame, text='7', command=lambda:press(7))
boton7.grid(column=0, row=1)
boton8 = ttk.Button(frame, text='8', command=lambda:press(8))
boton8.grid(column=1, row=1)
boton9 = ttk.Button(frame, text='9', command=lambda:press(9))
boton9.grid(column=2, row=1)
boton_div=ttk.Button(frame, text='/', command=lambda:press('/'))
boton_div.grid(column=3, row=1)


boton4 = ttk.Button(frame, text='4', command=lambda:press(4))
boton4.grid(column=0, row=2)
boton5 = ttk.Button(frame, text='5', command=lambda:press(5))
boton5.grid(column=1, row=2)
boton6 = ttk.Button(frame, text='6', command=lambda:press(6))
boton6.grid(column=2, row=2)
boton_mul=ttk.Button(frame, text='*', command=lambda:press('*'))
boton_mul.grid(column=3, row=2)


boton1 = ttk.Button(frame, text='1', command=lambda:press(1))
boton1.grid(column=0, row=3)
boton2 = ttk.Button(frame, text='2', command=lambda:press(2))
boton2.grid(column=1, row=3)
boton3 = ttk.Button(frame, text='3', command=lambda:press(3))
boton3.grid(column=2, row=3)
boton_mul=ttk.Button(frame, text='*', command=lambda:press('*'))
boton_mul.grid(column=3, row=3)




boton0 = ttk.Button(frame, text='0', command=lambda:press(0))
boton0.grid(column=0, row=4)
boton_pto = ttk.Button(frame, text='.', command=lambda:press('.'))
boton_pto.grid(column=1, row=4)
boton_cer = ttk.Button(frame, text='c', command=lambda:clr())
boton_cer.grid(column=2, row=4)
boton_mas=ttk.Button(frame, text='+', command=lambda:press('+'))
boton_mas.grid(column=3, row=4)


boton_eq = ttk.Button(frame, text='=', command=lambda:equal())
boton_eq.grid(row=5,columnspan=4, sticky='nsew')





win.mainloop()
