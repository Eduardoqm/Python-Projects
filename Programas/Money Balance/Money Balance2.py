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
    font = "Verdana 10", justify = LEFT).place(relx=.8, rely=.9, anchor=S)

def new():
    global df
    df =  pd.DataFrame({'nu':[],
        'mp':[],
        'bb':[],
        'bens':[],
        'tdr':[],
        'tds':[],
        'dt':[],
        'nt':[]
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
    df_input = pd.DataFrame({'nu':[float(nu.get())],
        'mp':[float(mp.get())],
        'bb':[float(bb.get())],
        'bens':[float(bens.get())],
        'tdr':[float(tdr.get())],
        'tds':[float(tds.get())],
        'dt':[dt.get()],
        'nt':[nt.get()]
        })


    df_add = [df, df_input]
    df_master = pd.concat(df_add, ignore_index=True)
    df = df_master
    Label(master, text = df, fg = "black", bg = "white",
    font = "Verdana 10", justify = CENTER).place(relx=.8, rely=.9, anchor=S)


def plott():
    global df
   
    plt.figure(figsize=(10, 6))
    #Pieplot
    #plt.subplot(2, 2, 1)
    #df.groupby('category')['values'].sum().plot(kind='pie')
    #plt.ylabel(' ')
    #plt.xlabel(' ')
    #plt.title('Size of Category')
   
    #Barplot
    plt.subplot(2, 2, 2)
    df.groupby('dt')['bens'].sum().plot(kind='bar', color = ['darkblue'])
    plt.ylabel('Total in money')
    plt.xlabel(' ')
    plt.title('Total in Staff')
    plt.xticks(rotation='45')

    #Lineplot
    plt.subplot(2, 2, 1)
    plt.plot(df.groupby('dt')['tdr'].sum(), color = 'red')
    plt.plot(df.groupby('dt')['tds'].sum(), color = 'green')
    mdates.DateFormatter("%Y-%m-%d")
    plt.title('Money total')
    plt.ylabel('Total in money')
    plt.xticks(rotation='45')

    plt.subplot(2, 2, 3)
    plt.plot(df.groupby('dt')['nu'].sum(), color = 'purple')
    plt.plot(df.groupby('dt')['mp'].sum(), color = 'blue')
    plt.plot(df.groupby('dt')['bb'].sum(), color = 'yellow')
    mdates.DateFormatter("%Y-%m-%d")
    plt.title('Money in Bank')
    plt.ylabel('Total in money')
    plt.xticks(rotation='45')
    plt.show()

def about():
    messagebox.showinfo("???")




#Window =================================================================================================
import sys
master = Tk()
master.title('Money Balance 1.0')
master.geometry('1200x680+0+0') #L,A
#master.attributes('-fullscreen',True)
master.configure(background='snow')

#Menu ---------------------------------------------------------------------------------------
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

#Labels (texts) -----------------------------------------------------------------------------
Label(master, text='                     Data Bank                    ',
fg = "black", bg = "lavender", font = "Verdana 15 bold").place(relx=.8, rely=.95, anchor=CENTER)

Label(master, text = '       Total Money        ', fg = "black", bg = "lavender",
font = "Verdana 25 bold", justify = LEFT).place(relx=.3, rely=.25, anchor=S)

Label(master, text='NU Bank', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=2) 
Label(master, text='Merc Pago', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=3) 
Label(master, text='Banco do Brasil', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=4)
Label(master, text='Bens', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=5)
Label(master, text='Total R$', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=6)
Label(master, text='Total $', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=7)
Label(master, text='Date', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=8)
Label(master, text='Notes', bg = "snow", font = "Verdana 10 bold").grid(row=0, column=9)  
Label(master, text='            ', bg = "snow",).grid(row=1, column=1) 

#Inputs
nu = Entry(master, bg = "lavender") 
nu.grid(row=1, column=2)
mp = Entry(master, bg = "lavender") 
mp.grid(row=1, column=3)
bb = Entry(master, bg = "lavender")
bb.grid(row=1, column=4)
bens = Entry(master, bg = "lavender")  
bens.grid(row=1, column=5)
tdr = Entry(master, bg = "lavender")  
tdr.grid(row=1, column=6) 
tds = Entry(master, bg = "lavender")  
tds.grid(row=1, column=7) 
dt = Entry(master, bg = "lavender")  
dt.grid(row=1, column=8) 
nt = Entry(master, bg = "lavender")  
nt.grid(row=1, column=9) 

addbt = Button(master, text='  Submit  ⇨', fg = "white", bg = "green", font = "Verdana 10 bold", command=add)
addbt.place(relx=.50, rely=.1, anchor=CENTER)

salvebt = Button(master, text='   Salve/Export   ', fg = "white", bg = "purple1", font = "Verdana 10 bold", command=salve)
salvebt.place(relx=.40, rely=.1, anchor=CENTER)

plotbt = Button(master, text='Graphic Report', fg = "white", bg = "blue", font = "Verdana 10 bold", command=plott)
plotbt.place(relx=.29, rely=.1, anchor=CENTER)

master.mainloop()