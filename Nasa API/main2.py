import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import filedialog

win = tk.Tk()
win.title("NASA API")
win.configure(bg='black')
win.geometry('1920x1080')

title = ttk.Label(win, text='Asteroid Tracking', font=('Arial Black', 40, 'bold'), background='black', foreground='white')

title.place(relx = 0.5, rely = 0, anchor = N)

win.mainloop()