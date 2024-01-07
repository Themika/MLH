import tkinter as tk
from tkinter import ttk
from tkinter import *

#Basic Way
print ('Hello, World!')

#Array
array = ["H", "e", "l", "l", "o", ", ", "W", "o", "r", "l", "d", "!"]
print(''.join(array))

#Visual in python
root = tk.Tk()
root.title("Hello World")
root.geometry('500x500')
root.configure(bg='black')
Hello_World = tk.Label(root,text="Hello, World!", font=("Helvetica", 50, 'bold'), background='black', foreground='white')
Hello_World.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()