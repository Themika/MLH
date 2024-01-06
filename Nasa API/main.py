import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def create_card(parent, title, content, image_path, width, height):
    global img
    
    card_frame = ttk.Frame(parent, borderwidth=60, height=500, relief='raised')
    card_frame.grid(column=0, row=0, padx=10, pady=10)

    title_label = ttk.Label(card_frame, text=title, font=('Helvetica', 14, 'bold'))
    title_label.grid(column=0, row=0, columnspan=2, sticky='w')

    content_label = ttk.Label(card_frame, text=content, wraplength=200)
    content_label.grid(column=0, row=1, columnspan=2, pady=10, sticky='w')

    img = Image.open(image_path)
    img = img.resize((width, height), Image.AFFINE)  
    img = ImageTk.PhotoImage(img)

    image_label = ttk.Label(card_frame, image=img)
    image_label.grid(column=0, row=2, columnspan=2, pady=10, sticky='w')

root = tk.Tk()
root.title("Card Example")

image_path = "C:/Users/Owner/Pictures/16098389109815.jpg"
width = 150  
height = 150  

create_card(root, "Card 1", "This is the content of Card 1.", image_path, width, height)

root.mainloop()
