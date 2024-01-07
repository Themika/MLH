import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import webbrowser

root = tk.Tk()
root.title("NASA API")
def openURL(url):
   webbrowser.open_new_tab(url)
#function for creating a card has all teh fetures of a card.
def create_card(parent, title, esitmated_Diameter_Meter_Max, esitmated_Diameter_Meter_Min, esitmated_Diameter_KM_Max, esitmated_Diameter_KM_Min, absolute_Magnitude, Potential_Danger_Level, Date_Of_Nearest_Approach,URL_For_Astroid, image_path, width, height):
    card_frame = ttk.Frame(parent, borderwidth=60, height=500, relief='raised')
    card_frame.grid(row=0, column=0, padx=10, pady=10)
    
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
def show_card():
    image_path = "Nasa API/16098389109815.jpg"
    width = 250
    height = 250
    
    card = create_card(root, "Astroid:Change", "", "", "", "", "", "", "","", image_path, width, height)
    card.place(relx=0.5, rely=0.5, anchor='center')  

 
root.configure(background='black')
root.title("Card Example")

# Configure the style for the light grey background
style = ttk.Style(root)
style.configure('LightGrey.TFrame', background='#8a8883')  

btn = Button(root, text='Generate new Card !', bd='5', command=show_card)
btn.place(relx=0.3, rely=0.5, anchor='center')  
 

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()
