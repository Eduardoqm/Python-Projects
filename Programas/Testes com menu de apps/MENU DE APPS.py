import os, sys, subprocess
import tkinter as tk

def page():
    os.system('start root.html')

def tortuga():
    os.system('start Turtle-Race.py')

root = tk.Tk()
canvas = tk.Canvas(root, height = 300, width = 300, bg = "white")
canvas.pack()

img = tk.PhotoImage(file = 'logo1.png')
img_label = tk.Label(root, image = img)
img_label.place(relx=0.3, rely=0.1, relheight = 0.55, relwidth = 0.55)

button = tk.Button(root, text = 'Turtle', fg = "white", bg = 'green', command = tortuga)
button.place(relx=0.1, rely=0.1)

button2 = tk.Button(root, text = 'Page', fg = "white", bg = 'blue', command = page)
button2.place(relx=0.1, rely=0.3)

root.mainloop()