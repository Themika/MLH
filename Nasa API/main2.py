import tkinter as tk
from tkinter import ttk 
from tkinter import *
from tkinter.ttk import Combobox
import webbrowser
from PIL import Image, ImageTk

from back_end import *

win = tk.Tk()
win.title("NASA API")
win.configure(background='black')
win.geometry('1920x1080')

image = Image.open(r'Nasa API\galaxy.jpg')
image = ImageTk.PhotoImage(image)

image_label2 = tk.Label(win, image=image)
image_label2.pack()

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
st.place(relx= 0.2, rely= 0.253)

et = Entry (win, bg='white',font=('Arial', 14, 'bold'), width=10, bd=5 )
et.place(relx= 0.2, rely= 0.3)


def openURL(url):
   webbrowser.open_new_tab(url)
#function for creating a card has all teh fetures of a card.
def create_card(parent, title, esitmated_Diameter_Meter_Max, esitmated_Diameter_Meter_Min, esitmated_Diameter_KM_Max, esitmated_Diameter_KM_Min, absolute_Magnitude, Potential_Danger_Level, Date_Of_Nearest_Approach,URL_For_Astroid, image_path, width, height):
    card_frame = ttk.Frame(parent, borderwidth=60, height=500, relief='raised')
    
    card_frame.configure(style='LightGrey.TFrame')

    title_label = ttk.Label(card_frame, text=title, font=('Helvetica', 14, 'bold'), background='#8a8883', foreground='white')  
    title_label.grid(column=0, row=0, columnspan=2, sticky='n')  

    img = Image.open(image_path)
    img = img.resize((width, height), Image.ADAPTIVE)
    img = ImageTk.PhotoImage(img)

    card_frame.img = img

    image_label = ttk.Label(card_frame, image=img, background='#8a8883')  
    image_label.grid(column=0, row=1, columnspan=2, pady=10, sticky='w')

    esitmatedDiameterMeterMax = ttk.Label(card_frame, text=f"Estimated Diameter Max (Meter): {esitmated_Diameter_Meter_Max}", wraplength=200, background='#8a8883', foreground='white') 
    esitmatedDiameterMeterMax.grid(column=0, row=2, columnspan=2, pady=10, sticky='w')

    esitmatedDiameterMeterMin = ttk.Label(card_frame, text=f"Estimated Diameter Min (Meter): {esitmated_Diameter_Meter_Min}", wraplength=200, background='#8a8883', foreground='white') 
    esitmatedDiameterMeterMin.grid(column=0, row=3, columnspan=2, pady=10, sticky='w')

    esitmatedDiameterKMMax1 = ttk.Label(card_frame, text=f"Estimated Diameter Max (KM): {esitmated_Diameter_KM_Max}", wraplength=200, background='#8a8883', foreground='white')  
    esitmatedDiameterKMMax1.grid(column=0, row=4, columnspan=2, pady=10, sticky='w')

    esitmatedDiameterKMMin1 = ttk.Label(card_frame, text=f"Estimated Diameter Min (KM): {esitmated_Diameter_KM_Min}", wraplength=200, background='#8a8883', foreground='white')  
    esitmatedDiameterKMMin1.grid(column=0, row=5, columnspan=2, pady=10, sticky='w')

    Maggnitude = ttk.Label(card_frame, text=f"Absolute Magnitude: {absolute_Magnitude}", wraplength=200, background='#8a8883', foreground='white')  
    Maggnitude.grid(column=0, row=6, columnspan=2, pady=10, sticky='w')

    PotentialDanger = ttk.Label(card_frame, text=f"Potential Danger Level: {Potential_Danger_Level}", wraplength=200, background='#8a8883', foreground='white')
    PotentialDanger.grid(column=0, row=7, columnspan=2, pady=10, sticky='w')

    Date = ttk.Label(card_frame, text=f"Date of Nearest Approach: {Date_Of_Nearest_Approach}", wraplength=200, background='#8a8883', foreground='white')  
    Date.grid(column=0, row=8, columnspan=2, pady=10, sticky='w')

    URl = ttk.Label(card_frame, text=f"Read More: {URL_For_Astroid}", wraplength=200, background='#8a6883', foreground='white')
    URl.grid(column=0,row=9,columnspan=2,pady=10, sticky='w')
    URl.bind("<Button-1>", lambda e: openURL(f"{URL_For_Astroid}"))

    return card_frame

#Function for showing the card 
def show_card(a, b, c, d, e, f, g, h, i):
    image_path = "Nasa API/16098389109815.jpg"
    width = 250
    height = 250
    
    card = create_card(win, f"{a}", f"{b}", f"{c}", f"{d}", f"{e}", f"{f}", f"{g}", f"{h}",f"{i}", image_path, width, height)
    card.place(relx=0.5, rely=0.5, anchor='center')   

def generateData():
    start_date = list(map(int, st.get().split("-")))
    end_date = list(map(int, et.get().split("-")))

    global extracted_data 
    extracted_data = Data_Extraction(date(start_date[0], start_date[1], start_date[2]),
                                          date(end_date[0], end_date[1], end_date[2]))
    extracted_data.load_data()
    extracted_data.get_asteriods()

    combo.config(values=extracted_data.asteriod_names)

def selection_change(e):
    index = extracted_data.asteriod_names.index(combox_value.get())
    data = extracted_data.asteriods[index]

    show_card(data.name, data.est_dia_max_m, data.est_dia_min_m, data.est_dia_max_km, data.est_dia_min_km, data.magnitude, data.pot_danger_level, data.date, data.nasa_jpl_url)

combox_value = tk.StringVar()
combo = Combobox(win, state='readonly', font=('Arial', 17), width=10, textvariable=combox_value)
combo.bind("<<ComboboxSelected>>", selection_change)
combo.place(relx = 0.11, rely=0.35)


# Configure the style for the light grey background
style = ttk.Style(win)
style.configure('LightGrey.TFrame', background='#8a8883')  # Use hex code for light grey

#button is used to pull the data for those asteriods
btn = Button(win, text='Generate Asteroid', bd='5', command=generateData)
btn.place(relx= 0.05, rely=0.35) 
 

win.grid_columnconfigure(0, weight=1)
win.grid_rowconfigure(0, weight=1)

win.mainloop()