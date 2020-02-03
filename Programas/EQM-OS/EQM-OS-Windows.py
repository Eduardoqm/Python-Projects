#EQM - OS
#Demo start
#By Eduardo Q Marques  29-dez-2019

import time
import os, sys, subprocess
import webbrowser
from tkinter import *
import turtle
from turtle import Turtle
from random import randint

#Python apps
def kalk():
    def iCalc(source, side):
        storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
        storeObj.pack(side=side, expand =YES, fill =BOTH)
        return storeObj
     
    def button(source, side, text, command=None):
        storeObj = Button(source, text=text, command=command)
        storeObj.pack(side=side, expand = YES, fill=BOTH)
        return storeObj
     
    class app(Frame):
        def __init__(self):
            Frame.__init__(self)
            self.option_add('*Font', 'arial 20 bold')
            self.pack(expand = YES, fill =BOTH)
            self.master.title('Calculator')
     
            display = StringVar()
            Entry(self, relief=RIDGE, textvariable=display,
              justify='right'
              , bd=30, bg="powder blue").pack(side=TOP,
                                              expand=YES, fill=BOTH)
     
            for clearButton in (["C"]):
                erase = iCalc(self, TOP)
                for ichar in clearButton:
                    button(erase, LEFT, ichar, lambda
                        storeObj=display, q=ichar: storeObj.set(''))
     
            for numButton in ("789/", "456*", "123-", "0.+"):
             FunctionNum = iCalc(self, TOP)
             for iEquals in numButton:
                button(FunctionNum, LEFT, iEquals, lambda
                    storeObj=display, q=iEquals: storeObj
                       .set(storeObj.get() + q))
     
            EqualButton = iCalc(self, TOP)
            for iEquals in "=":
                if iEquals == '=':
                    btniEquals = button(EqualButton, LEFT, iEquals)
                    btniEquals.bind('<ButtonRelease-1>', lambda e,s=self,
                                    storeObj=display: s.calc(storeObj), '+')
     
     
                else:
                    btniEquals = button(EqualButton, LEFT, iEquals,
                                        lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                        (storeObj.get() + s))
     
        def calc(self, display):
                try:
                    display.set(eval(display.get()))
                except:
                    display.set("ERROR")
     
     
    if __name__=='__main__':
     app().mainloop()

def jog1():
    #Turtle race
    #EQM - Games
    #Eduardo Q Marques
    #29/03/2019

    #Janela
    window = turtle.Screen()
    window.title("Turtle Race")
    turtle.bgcolor("forestgreen")
    turtle.color("white")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-140, 200)
    turtle.write("Turtle Race", font=("Arial", 30, "bold"))
    turtle.penup()

    #DIRT
    turtle.setpos(-400, -180)
    turtle.color("chocolate")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(300)
    turtle.end_fill()

    #Final line
    stamp_size = 20
    square_size = 15
    finish_line = 200

    turtle.color("black")
    turtle.shape("square")
    turtle.shapesize(square_size / stamp_size)
    turtle.penup()

    for i in range (10):
            turtle.setpos(finish_line, (150 - (i * square_size * 2)))
            turtle.stamp()

    for j in range(10):
            turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
            turtle.hideturtle()

    #Jabuti 1
    turtle1 = Turtle()
    turtle1.speed(0)
    turtle1.color("black")
    turtle1.shape("turtle")
    turtle1.penup()
    turtle1.goto(-250, 100)
    turtle1.pendown()

    #Jabuti 2
    turtle2 = Turtle()
    turtle2.speed(0)
    turtle2.color("cyan")
    turtle2.shape("turtle")
    turtle2.penup()
    turtle2.goto(-250, 50)
    turtle2.pendown()

    #Jabuti 3
    turtle3 = Turtle()
    turtle3.speed(0)
    turtle3.color("magenta")
    turtle3.shape("turtle")
    turtle3.penup()
    turtle3.goto(-250, 0)
    turtle3.pendown()

    #Jabuti 4
    turtle4 = Turtle()
    turtle4.speed(0)
    turtle4.color("yellow")
    turtle4.shape("turtle")
    turtle4.penup()
    turtle4.goto(-250, -50)
    turtle4.pendown()

    #Jabuti 5
    turtle5 = Turtle()
    turtle5.speed(0)
    turtle5.color("white")
    turtle5.shape("turtle")
    turtle5.penup()
    turtle5.goto(-250, -100)
    turtle5.pendown()

    time.sleep(2) #pause in seconds before race

    #Move the jabutis
    for i in range(145):
            turtle1.forward(randint(1,5))
            turtle2.forward(randint(1,5))
            turtle3.forward(randint(1,5))
            turtle4.forward(randint(1,5))
            turtle5.forward(randint(1,5))
            
    turtle.exitonclick()


#Ask name
os.system('clr')
print('Welcome to EQM Operation System')
time.sleep(1)
print('Version alpha - 2019')
print(' ')
time.sleep(1)
user = input('What is your name? ')
print('Hi {}!'.format(user))

#List apps
app = 0
while True:
    time.sleep(1)
    os.system('clr')
    print(' ')
    print('=-=-=-=-=-=-=-=-=-=MENU-=-=-=-=-=-=-=-=-=-=')
    print('''{}, choose a app:
        1-Text Editor
        2-Calculator
        3-Tabulate
        4-Games
        5-Internet
        6-Shutdown'''.format(user))

    app = int(input('What you need?' ))
    
    if app == 1:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, '/C:/Users/Eduardo Q Marques/Documents/My Jobs/Programas/Python/Python-Projects/Programas/EQM-OS/Softwares-starts/New text.odt'])
        
    elif app == 2:
        kalk()
        
    elif app == 3:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, '/home/apocalipse/Documents/Programas/EQM-OS/Softwares-starts/New Table.ods'])
        
    elif app == 4:
        jog1()
        
    elif app == 5:
        webbrowser.open('http://www.duckduckgo.com')
        
    elif app == 6:
        os.system('clr')
        print('Thank you {} for use EQM-OS...Bye!'.format(user))
        time.sleep(2)
        quit()
        
    else:
        os.system('clr')
        print('App not find!')
        time.sleep(2)
