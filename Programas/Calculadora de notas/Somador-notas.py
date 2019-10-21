# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:28:43 2019

@author: Eduardo Q Marques
"""
import pandas as pd
from pandas import DataFrame
from tkinter import *
from tkinter import filedialog
from tkinter import ttk

#Functions 
def opn():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    Label(master, text = df, fg = "black", bg = "white",
    font = "Verdana 10", justify = LEFT).place(relx=.5, rely=.2, anchor=CENTER)

def new():
    global df
    df =  pd.DataFrame({'category':[],
        'number_id':[],
        'date':[],
        'values':[],
        'notes':[]
        })

    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = None, header=True)

    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    Label(master, text = df, fg = "black", bg = "white",
    font = "Verdana 10", justify = LEFT).place(relx=.5, rely=.2, anchor=CENTER)

def salve():
    global df
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = None, header=True)

def expbt():
    global df
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = None, header=True)

def add():
    global df
    df_input = pd.DataFrame({'category':[cat_nt.get()],
        'number_id':[float(n_nt.get())],
        'date':[data_nt.get()],
        'values':[float(val_nt.get())],
        'notes':[note_nt.get()]
        })

    df_add = [df, df_input]
    df_master = pd.concat(df_add)
    df = df_master
    Label(master, text = df, fg = "black", bg = "white",
    font = "Verdana 10", justify = LEFT).place(relx=.5, rely=.2, anchor=CENTER)

#Window
master = Tk()
master.title('Calculadora de notas - Beta')
master.geometry('1200x650+0+0') #L,A

#Labels (texts)
Label(master, text='Data Bank', fg = "black", bg = "yellow", font = "Verdana 20 bold").place(relx=.5, rely=.05, anchor=CENTER)

Label(master, text='Category').grid(row=3, column=1) 
Label(master, text='Number ID').grid(row=5, column=1) 
Label(master, text='Date').grid(row=7, column=1) 
Label(master, text='Value').grid(row=9, column=1)
Label(master, text='Notes').grid(row=11, column=1)  

#Inputs
cat_nt = Entry(master) 
cat_nt.grid(row=3, column=2)
n_nt = Entry(master) 
n_nt.grid(row=5, column=2)
data_nt = Entry(master)
data_nt.grid(row=7, column=2)
val_nt = Entry(master)  
val_nt.grid(row=9, column=2)
note_nt = Entry(master)  
note_nt.grid(row=11, column=2)

#Buttons
openbt = Button(master, text='Open', command=opn)
openbt.grid(row=3, column=3)

newbt = Button(master, text='New', command=new)
newbt.grid(row=5, column=3)

expbt = Button(master, text='Export', command=expbt)
expbt.grid(row=7, column=3)

addbt = Button(master, text='Submit', fg = "white", bg = "green", font = "Verdana 10 bold", command=add)
addbt.grid(row=12, column=2)

salvebt = Button(master, text='Salve', command=salve)
salvebt.grid(row=11, column=3, columnspan=2)

master.mainloop()
