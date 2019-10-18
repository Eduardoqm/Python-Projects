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
master.title('Calculadora de notas - Beta')
master.geometry('700x400+0+0') #L,A

Label(master, text='= N1').grid(row=0, column=3) 
result = Label(master, text='').grid(row=3, column=2) 

cat_nt = Entry(master) 
cat_nt.grid(row=0, column=1)
n_nt = Entry(master) 
n_nt.grid(row=0, column=2)
data_nt = Entry(master)
data_nt.grid(row=0, column=3)
val_nt = Entry(master)  
val_nt.grid(row=0, column=4) 

somabt = Button(master, text='Somar', command=soma)
somabt.grid(row=3, column=0)





master.mainloop()
