# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:28:43 2019

@author: Eduardo Q Marques
"""

from tkinter import *

def soma():
    a=float(e1.get())
    b=float(e2.get())
    x=(b*100)/a
    Label(master, text='                                ',).grid(row=3, column=1, columnspan=5)
    Label(master, text=x,).grid(row=3, column=1, columnspan=5)

master = Tk()
master.title('Percent Calc - Beta')
master.geometry('300x100+0+0') #L,A

Label(master, text='= 100%').grid(row=0, column=3) 
Label(master, text='= X').grid(row=1, column=3) 
result = Label(master, text='%').grid(row=3, column=2) 

e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 

somabt = Button(master, text='Calculate', command=soma)
somabt.grid(row=3, column=0)





master.mainloop()
