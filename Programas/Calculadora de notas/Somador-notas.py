# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:28:43 2019

@author: Eduardo Q Marques
"""

from tkinter import *

#Functions
def add():
    a=float(e1.get())
    b=17.07
    c = a + b
    Label(master, text='                                ',).grid(row=3, column=1, columnspan=5)
    Label(master, text=c,).grid(row=3, column=1, columnspan=5)
    b = c

def opn():
    a=float(e1.get())

def salve():
    a=float(e1.get())

def new():
    a=float(e1.get())


#Window
master = Tk()
master.title('Calculadora de notas - Beta')
master.geometry('700x250+0+0') #L,A

#Labels (texts)
Label(master, text='Category').grid(row=0, column=2) 
Label(master, text='Number ID').grid(row=0, column=3) 
Label(master, text='Date').grid(row=0, column=4) 
Label(master, text='Value').grid(row=0, column=5) 
result = Label(master, text='').grid(row=3, column=5) 

#Inputs
cat_nt = Entry(master) 
cat_nt.grid(row=1, column=2)
n_nt = Entry(master) 
n_nt.grid(row=1, column=3)
data_nt = Entry(master)
data_nt.grid(row=1, column=4)
val_nt = Entry(master)  
val_nt.grid(row=1, column=5) 

#Buttons
addbt = Button(master, text='Add', command=add)
addbt.grid(row=3, column=2, columnspan=2)

salvebt = Button(master, text='Salve', command=salve)
salvebt.grid(row=3, column=3, columnspan=2)

openbt = Button(master, text='Open', command=opn)
openbt.grid(row=0, column=1)

newbt = Button(master, text='New', command=new)
newbt.grid(row=1, column=1)

master.mainloop()
