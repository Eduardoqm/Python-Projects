# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:28:43 2019

@author: Eduardo Q Marques
"""
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import filedialog

#Functions 
def opn():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    Label(master, text = df, fg = "black", bg = "white",
    font = "Verdana 10", justify = CENTER).place(relx=.8, rely=.9, anchor=S)
    res = df['4'].describe()
    Label(master, text = res, fg = "black", bg = "white",
    font = "Verdana 10", justify = CENTER).place(relx=.3, rely=.9, anchor=S)

    

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
    font = "Verdana 10", justify = CENTER).place(relx=.8, rely=.9, anchor=S)

def salve():
    global df
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    df.to_csv (export_file_path, index = None, header=True)

def add():
    global df
    df_input = pd.DataFrame({'category':[cat_nt.get()],
        'number_id':[float(n_nt.get())],
        'date':[float(data_nt.get())],
        'values':[float(val_nt.get())],
        'notes':[note_nt.get()]
        })

    df_add = [df, df_input]
    df_master = pd.concat(df_add, ignore_index=True)
    df = df_master
    Label(master, text = df, fg = "black", bg = "white",
    font = "Verdana 10", justify = CENTER).place(relx=.8, rely=.9, anchor=S)
    res = df['4'].describe()
    Label(master, text = res, fg = "black", bg = "white",
    font = "Verdana 10", justify = CENTER).place(relx=.3, rely=.9, anchor=S)

def plott():
    df.plot()
    plt.ylabel('Value')
    box = plt.show()
    Label(master, image = box).place(relx=.8, rely=.9, anchor=CENTER)

#Window
master = Tk()
master.title('Calculadora de notas - Beta')
master.geometry('1250x650+0+0') #L,A
master.configure(background='snow')

#Labels (texts)
Label(master, text='                     Data Bank                    ',
fg = "black", bg = "lavender", font = "Verdana 15 bold").place(relx=.8, rely=.95, anchor=CENTER)

Label(master, text='Category', bg = "white", font = "Verdana 10 bold").grid(row=0, column=2) 
Label(master, text='Number ID', bg = "white", font = "Verdana 10 bold").grid(row=0, column=3) 
Label(master, text='Date', bg = "white", font = "Verdana 10 bold").grid(row=0, column=4) 
Label(master, text='Value', bg = "white", font = "Verdana 10 bold").grid(row=0, column=5)
Label(master, text='Notes', bg = "white", font = "Verdana 10 bold").grid(row=0, column=6)  

#Inputs
cat_nt = Entry(master, bg = "lavender") 
cat_nt.grid(row=1, column=2)
n_nt = Entry(master, bg = "lavender") 
n_nt.grid(row=1, column=3)
data_nt = Entry(master, bg = "lavender")
data_nt.grid(row=1, column=4)
val_nt = Entry(master, bg = "lavender")  
val_nt.grid(row=1, column=5)
note_nt = Entry(master, bg = "lavender")  
note_nt.grid(row=1, column=6) 

#Buttons
openbt = Button(master, text='Open', bg = "white", font = "Verdana 10 bold", command=opn)
openbt.grid(row=1, column=1)

newbt = Button(master, text='New  ', bg = "white", font = "Verdana 10 bold", command=new)
newbt.grid(row=0, column=1)

addbt = Button(master, text='  Submit  ⇨', fg = "white", bg = "green", font = "Verdana 10 bold", command=add)
addbt.place(relx=.50, rely=.1, anchor=CENTER)

salvebt = Button(master, text='   Salve/Export   ', fg = "white", bg = "purple1", font = "Verdana 10 bold", command=salve)
salvebt.place(relx=.40, rely=.1, anchor=CENTER)

plotbt = Button(master, text='Graphic Report', fg = "white", bg = "blue", font = "Verdana 10 bold", command=plott)
plotbt.place(relx=.29, rely=.1, anchor=CENTER)

master.mainloop()
