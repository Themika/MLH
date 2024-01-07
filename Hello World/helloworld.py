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
Hello_World = tk.Label(root,text="Hello, World!", font=("Helvetica"))
Hello_World.pack()

root.mainloop()