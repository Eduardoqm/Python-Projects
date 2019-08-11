# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:28:43 2019

@author: Eduardo Q Marques
"""

from tkinter import *

def soma():
    a=float(e1.get())
    b=float(e2.get())
    x=a+b
    Label(master, text=x).grid(row=3, column=1)

master = Tk()
master.title('Sum Machine - Beta')

Label(master, text='Inserir nª').grid(row=0) 
Label(master, text='Inserir nª').grid(row=1) 
result = Label(master, text='Resultado->').grid(row=3, column=0) 

e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 

somabt = Button(master, text='somar', command=soma)
somabt.grid(row=3, column=5, columnspan=3)





master.mainloop()
