# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:28:43 2019

@author: Eduardo Q Marques
"""
import pandas as pd
from pandas import DataFrame
from tkinter import *
from tkinter import filedialog

#Functions
path = ()
def add():
    a=float(e1.get())
    b=17.07
    c = a + b
    Label(master, text='                                ',).grid(row=3, column=1, columnspan=5)
    Label(master, text=c,).grid(row=3, column=1, columnspan=5)
    b = c

def opn():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    print (df)

def new():
    df =  pd.DataFrame({'category':[],
        'number_id':[],
        'date':[],
        'values':[],
        'notes':[]
        })

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = None, header=True)

def salve():
    df = DataFrame(cupon, columns= ['category', 'number_id', 'date', 'values', 'notes'])
    print (df)

def expbt():
    global df
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = None, header=True)


#Window
master = Tk()
master.title('Calculadora de notas - Beta')
master.geometry('700x250+0+0') #L,A

#Labels (texts)
Label(master, text='Category').grid(row=0, column=2) 
Label(master, text='Number ID').grid(row=0, column=3) 
Label(master, text='Date').grid(row=0, column=4) 
Label(master, text='Value').grid(row=0, column=5)
Label(master, text='Notes').grid(row=0, column=6)  
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
note_nt = Entry(master)  
note_nt.grid(row=1, column=6) 

#Buttons
addbt = Button(master, text='Add', command=add)
addbt.grid(row=3, column=2, columnspan=2)

salvebt = Button(master, text='Salve', command=salve)
salvebt.grid(row=3, column=3, columnspan=2)

openbt = Button(master, text='Open', command=opn)
openbt.grid(row=0, column=1)

newbt = Button(master, text='New', command=new)
newbt.grid(row=1, column=1)

expbt = Button(master, text='Export', command=expbt)
expbt.grid(row=2, column=1)

master.mainloop()
