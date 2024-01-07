import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from tkinter import filedialog


win = tk.Tk()
win.title("NASA API")

win.geometry('1920x1080')

title = ttk.Label(text='Asteroid Search', font=('Arial Black', 40, 'bold'), background='black', foreground='white')
title.place(relx = 0.5, rely = 0, anchor = N)

des = ttk.Label (text='Enter a start and end date to see what asteroids were close to earth during that period', font=('Arial', 15), background='black', foreground='white')
des.place(relx = 0.5, rely = 0.09, anchor= CENTER)












win.mainloop()