# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:28:43 2019

@author: Eduardo Q Marques
"""

from tkinter import *

def soma():
    a=float(e1.get())
    b=17.07
    c = a + b
    Label(master, text='                                ',).grid(row=3, column=1, columnspan=5)
    Label(master, text=c,).grid(row=3, column=1, columnspan=5)
    b = c

master = Tk()
master.title('Percent Calc - Beta')
master.geometry('300x100+0+0') #L,A

Label(master, text='= N1').grid(row=0, column=3) 
result = Label(master, text='').grid(row=3, column=2) 

e1 = Entry(master) 
e1.grid(row=0, column=1) 

somabt = Button(master, text='Somar', command=soma)
somabt.grid(row=3, column=0)





master.mainloop()
