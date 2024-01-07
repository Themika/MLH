import tkinter as tk
from tkinter import ttk 
from tkinter import *

win = tk.Tk()
win.title("NASA API")
win.configure(background='black')
win.geometry('1920x1080')

title = ttk.Label(text='Asteroid Search', font=('Arial Black', 40, 'bold'), background='black', foreground='white')
title.place(relx = 0.5, rely = 0, anchor = N)

des = ttk.Label (text='Enter a start and end date to see what asteroids were close to earth during that period', font=('Arial', 15), background='black', foreground='white')
des.place(relx = 0.5, rely = 0.09, anchor= CENTER)

inst = ttk.Label (text = 'Enter date in YYYY-MM-DD format', font=('Arial', 15), background='black', foreground='white')
inst.place(relx = 0.5, rely = 0.12, anchor= CENTER)

sdate = ttk.Label (text = 'Start Date:', font=('Arial', 20, 'bold'), background='black', foreground='white')
sdate.place(relx = 0.05, rely = 0.25)

edate = ttk.Label (text = 'End Date:', font=('Arial', 20, 'bold'), background='black', foreground='white')
edate.place(relx = 0.05, rely = 0.3)


st = Entry (win, bg='white',font=('Arial', 14, 'bold'), width=10, bd=5 )
st.place(relx= 0.13, rely= 0.253)

et = Entry (win, bg='white',font=('Arial', 14, 'bold'), width=10, bd=5 )
et.place(relx= 0.125, rely= 0.3)

btn = Button(win, text='Generate Asteroid', bd='5')
btn.place(relx= 0.05, rely=0.35)


win.mainloop()