# -*- coding: utf-8 -*-
"""
Money Balance
Created on 26-06-2020

@author: Eduardo Q Marques
"""
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.dates as mdates

#Functions ================================================================================================
def opn():
    global df
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    
    Label(master, text = df, fg = "black", bg = "white",
    font = "Verdana 10", justify = CENTER).place(relx=.8, rely=.9, anchor=S)

    resmean = df['values'].mean()
    resmax = df['values'].max()
    resmin = df['values'].min()
    ressum = df['values'].sum()

    Label(master, text = 'The total amount is:', fg = "black", bg = "snow",
    font = "Verdana 15", justify = LEFT).place(relx=.3, rely=.55, anchor=S)
    Label(master, text = '                                           ', fg = "black", bg = "snow",
    font = "Verdana 15 bold", justify = LEFT).place(relx=.3, rely=.6, anchor=S)
    Label(master, text = ressum, fg = "red", bg = "snow",
    font = "Verdana 15 bold", justify = LEFT).place(relx=.3, rely=.6, anchor=S)

    Label(master, text = 'To see more information click on Graphic Report!', fg = "black", bg = "snow",
    font = "Verdana 15", justify = LEFT).place(relx=.3, rely=.65, anchor=S)

def new():
    global df
    df =  pd.DataFrame({'category':[],
        'number_id':[],
        'date':[],
        'values':[],
        'notes':[]
        })

    export_file_path = filedialog.asksaveasfilename(title = "Create your new file name", defaultextension='.csv')
    df.to_csv (export_file_path, index = None, header=True)

    import_file_path = filedialog.askopenfilename(title = "Select your new file")
    df = pd.read_csv (import_file_path)
    Label(master, text = df, fg = "black", bg = "white",
    font = "Verdana 10", justify = CENTER).place(relx=.8, rely=.9, anchor=S)

def salve():
    global df
    export_file_path = filedialog.asksaveasfilename(title = "Select your file to save and replace", defaultextension='.csv')
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
    df_master = pd.concat(df_add, ignore_index=True)
    df = df_master
    Label(master, text = df, fg = "black", bg = "white",
    font = "Verdana 10", justify = CENTER).place(relx=.8, rely=.9, anchor=S)

    resmean = df['values'].mean()
    resmax = df['values'].max()
    resmin = df['values'].min()
    ressum = df['values'].sum()

    Label(master, text = 'The total amount is:', fg = "black", bg = "snow",
    font = "Verdana 15", justify = LEFT).place(relx=.3, rely=.55, anchor=S)
    Label(master, text = '                                           ', fg = "black", bg = "snow",
    font = "Verdana 15 bold", justify = LEFT).place(relx=.3, rely=.6, anchor=S)
    Label(master, text = ressum, fg = "red", bg = "snow",
    font = "Verdana 15 bold", justify = LEFT).place(relx=.3, rely=.6, anchor=S)

    Label(master, text = 'To see more information click on Graphic Report!', fg = "black", bg = "snow",
    font = "Verdana 15", justify = LEFT).place(relx=.3, rely=.65, anchor=S)

def plott():
    global df
   
    #Pieplot
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 2, 1)
    df.groupby('category')['values'].sum().plot(kind='pie')
    plt.ylabel(' ')
    plt.xlabel(' ')
    plt.title('Size of Category')
   
    #Barplot
    plt.subplot(2, 2, 2)
    df.groupby('category')['values'].sum().plot(kind='bar', color = ['green','y','orange','yellow', 'red', 'darkgreen', 'blue'])
    plt.ylabel('Total in money')
    plt.xlabel(' ')
    plt.title('Values by category')
    plt.xticks(rotation='45')

    #Lineplot
    plt.subplot(2, 2, 3)
    plt.plot(df.groupby('date')['values'].sum(), color = 'orange')
    mdates.DateFormatter("%Y-%m-%d")
    plt.title('Spending over time')
    plt.ylabel('Total in money')
    plt.xticks(rotation='45')
    plt.show()

def about():
    messagebox.showinfo("About Spending Calculator 1.0", "This software was developed by Eduardo Q. Marques (2019). \n"
     "For more information and get manual access the link: https://github.com/Eduardoqm/EQM-Softwares/tree/master/Spending%20Calculator%201.0")

#Window =================================================================================================
import sys
master = Tk()
master.title('Money Balance 1.0')
master.geometry('1200x680+0+0') #L,A
#master.attributes('-fullscreen',True)
master.configure(background='snow')

#Menu
menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0, font = "Verdana 10")
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=opn)
filemenu.add_command(label="Salve", command=salve)
filemenu.add_command(label="Exit", command=master.quit)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_separator()

helpmenu = Menu(menubar, tearoff=0, font = "Verdana 10")
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="About", menu=helpmenu)

master.config(menu=menubar)

#Labels (texts)
Label(master, text='                     Data Bank                    ',
fg = "black", bg = "lavender", font = "Verdana 15 bold").place(relx=.8, rely=.95, anchor=CENTER)

Label(master, text = '       Summarized report        ', fg = "black", bg = "lavender",
font = "Verdana 25 bold", justify = LEFT).place(relx=.3, rely=.25, anchor=S)

Label(master, text='Category', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=2) 
Label(master, text='Number ID', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=3) 
Label(master, text='Date', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=4) 
Label(master, text='Value', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=5)
Label(master, text='Notes', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=6)  
Label(master, text='            ', bg = "snow",).grid(row=1, column=1) 

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

addbt = Button(master, text='  Submit  ⇨', fg = "white", bg = "green", font = "Verdana 10 bold", command=add)
addbt.place(relx=.50, rely=.1, anchor=CENTER)

salvebt = Button(master, text='   Salve/Export   ', fg = "white", bg = "purple1", font = "Verdana 10 bold", command=salve)
salvebt.place(relx=.40, rely=.1, anchor=CENTER)

plotbt = Button(master, text='Graphic Report', fg = "white", bg = "blue", font = "Verdana 10 bold", command=plott)
plotbt.place(relx=.29, rely=.1, anchor=CENTER)

master.mainloop()