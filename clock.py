from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")

def time():
    string = strftime('%H:%M:%S\n%A, %d %B %Y')
    label.config(text=string)
    label.after(1000,time)

label = Label(root, font=("Calibri", 80), background = "white", foreground = "red")
label.pack(anchor='center')
time()

mainloop()

