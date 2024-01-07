import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk



def create_card(parent, title, esitmated_Diameter_Meter_Max, esitmated_Diameter_Meter_Min, esitmated_Diameter_KM_Max, esitmated_Diameter_KM_Min, absolute_Magnitude, Potential_Danger_Level, Date_Of_Nearest_Approach, image_path, width, height):
    card_frame = ttk.Frame(parent, borderwidth=60, height=500, relief='raised')
    card_frame.grid(row=0, column=0, padx=10, pady=10)

    title_label = ttk.Label(card_frame, text=title, font=('Helvetica', 14, 'bold'))
    title_label.grid(column=0, row=0, columnspan=2, sticky='w')
    title_label.place(relx=0.5, rely=-0.03, anchor='center')

    img = Image.open(image_path)
    img = img.resize((width, height), Image.ADAPTIVE)
    img = ImageTk.PhotoImage(img)

    card_frame.img = img

    image_label = ttk.Label(card_frame, image=img)
    image_label.grid(column=0, row=1, columnspan=2, pady=10, sticky='w')

    esitmatedDiameterMeterMax = ttk.Label(card_frame, text=f"Estimated Diameter Max (Meter): {esitmated_Diameter_Meter_Max}", wraplength=200)
    esitmatedDiameterMeterMax.grid(column=0, row=2, columnspan=2, pady=10, sticky='w')

    esitmatedDiameterMeterMin = ttk.Label(card_frame, text=f"Estimated Diameter Min (Meter): {esitmated_Diameter_Meter_Min}", wraplength=200)
    esitmatedDiameterMeterMin.grid(column=0, row=3, columnspan=2, pady=10, sticky='w')

    esitmatedDiameterKMMax1 = ttk.Label(card_frame, text=f"Estimated Diameter Max (KM): {esitmated_Diameter_KM_Max}", wraplength=200)
    esitmatedDiameterKMMax1.grid(column=0, row=4, columnspan=2, pady=10, sticky='w')

    esitmatedDiameterKMMin1 = ttk.Label(card_frame, text=f"Estimated Diameter Min (KM): {esitmated_Diameter_KM_Min}", wraplength=200)
    esitmatedDiameterKMMin1.grid(column=0, row=5, columnspan=2, pady=10, sticky='w')

    Maggnitude = ttk.Label(card_frame, text=f"Absolute Magnitude: {absolute_Magnitude}", wraplength=200)
    Maggnitude.grid(column=0, row=6, columnspan=2, pady=10, sticky='w')

    PotentialDanger = ttk.Label(card_frame, text=f"Potential Danger Level: {Potential_Danger_Level}", wraplength=200)
    PotentialDanger.grid(column=0, row=7, columnspan=2, pady=10, sticky='w')

    Date = ttk.Label(card_frame, text=f"Date of Nearest Approach: {Date_Of_Nearest_Approach}", wraplength=200)
    Date.grid(column=0, row=8, columnspan=2, pady=10, sticky='w')

    return card_frame

def show_card():
    image_path = "C:/Users/Owner/Pictures/16098389109815.jpg"
    width = 250
    height = 250

    card = create_card(root, "", "", "","", "", "","", "", image_path, width, height)
    card.grid(row=1, column=0, padx=10, pady=10)
    card.place(relx=0.5, rely=0.5, anchor='center')  

root = tk.Tk()

root.configure(background='black')
root.title("Card Example")

btn = Button(root, text='Generate new Card !', bd='5', command=show_card)
btn.place(relx=0.3, rely=0.5, anchor='center')  
 

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()
