from ctypes import resize
from termios import VMIN
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog, Text, Label
import tkinter
from turtle import left
from PIL import ImageTk, Image
import os
from httplib2 import WsseAuthentication
from matplotlib.ft2font import BOLD
import random

root = tk.Tk()
root.title('PaperRPG')

#window size
root.geometry("1250x760")
table = tk.Canvas(root, height=700, width=1250, bg="#756754")
table.pack()
img= ImageTk.PhotoImage(Image.open("table.jpeg"))
table.create_image(1500,200,anchor=E,image=img)

#dot frame
dotframe =tk.Frame(root,bg="#756754")
dotframe.place(relwidth=0.001,relheight=0.001, relx =0.03, rely=0.05)

dotframe1 =tk.Frame(root,bg="#756754")
dotframe1.place(relwidth=0.001,relheight=0.001, relx =0.03, rely=0.05)


#map image
mapimage = ImageTk.PhotoImage (file = "Map.jpg")
mapimge = table.create_image(290, 190, anchor=tk.NW, image=mapimage)

#charimg
charimage = ImageTk.PhotoImage (file = "scroll.png")
charimge = table.create_image(1, 0, anchor=tk.NW, image=charimage)

#coins image
coinsimage = ImageTk.PhotoImage (file = "coins.png")
coinsimge = table.create_image(0, 410, anchor=tk.NW, image=coinsimage)


#dot image
image = Image.open("dot.png")
dotimage = ImageTk.PhotoImage(image.resize((540, 610), Image.Resampling.LANCZOS))
label = Label(dotframe, image=dotimage, bg='#4a4135')
label.image = dotimage
label.pack()


image4 = Image.open("dot.png")
dotimage4 = ImageTk.PhotoImage(image.resize((760, 610), Image.Resampling.LANCZOS))
label4 = Label(dotframe1, image=dotimage4, bg='#4a4135')
label4.image = dotimage4
label4.pack()

#Dice buttons
image5 = Image.open("D20.png")
D20button = ImageTk.PhotoImage(image5.resize((50, 50), Image.Resampling.LANCZOS))
label = Label(dotframe, image=D20button, bg='#4a4135')
label.image = D20button
label.pack()

def D20_win():
   new1= Toplevel(root, bg="#756754")
   new1.geometry("500x250")
   new1.title("D20Roll")
   #Create a Label in New window
   Label(new1, text="choose dice", bg="#ffffff").pack(pady=10)
   #d20choice button
   
   def D20DICE(): 
    x= random.randint(1,20)
    m.set(x) 
 
   m=StringVar() 
   b1=Button(new1, text="D20", command=D20DICE).pack() 
   

   def D12DICE(): 
    x= random.randint(1,12)
    m.set(x) 
    
   m=StringVar() 
   b1=Button(new1, text="D12", command=D12DICE).pack() 
   

   def D6DICE(): 
    x= random.randint(1,6)
    m.set(x)
 
   m=StringVar() 
   b1=Button(new1, text="D6", command=D6DICE).pack() 
   lb1=Label(new1, text="_________", textvariable=m).pack() 


Dice_frame = tk.Frame(root, bg="#4a4135")
Dice_frame.pack(fill=tk.X, side=tk.RIGHT)

S20button = ttk.Button(Dice_frame, text="D20",image = D20button, width=85, command=D20_win).pack(side=tkinter.TOP)

############################################################################################

#inventory button
image2 = Image.open("inventoryimg.png")
inventory_button_image1 = ImageTk.PhotoImage(image2.resize((595, 50), Image.Resampling.LANCZOS))
label = Label(dotframe, image=inventory_button_image1, bg='#4a4135')
label.image = inventory_button_image1
label.pack()
#logs button
image3 = Image.open("logs.png")
Logs_button_image1 = ImageTk.PhotoImage(image3.resize((595, 50), Image.Resampling.LANCZOS))
label = Label(dotframe, image=Logs_button_image1, bg='#4a4135')
label.image = Logs_button_image1
label.pack()

###WINDOWS###
def inventory_win():
   new= Toplevel(root, bg="#756754")
   new.geometry("700x700")
   new.title("Inventory")
   #Create a Label in New window
   Label(new, text="Inventory", bg="#756754").pack(pady=30)

   logframe = Frame(new)
   logframe.pack(pady=5)
   #text box
   logtext = Text(logframe, width=97, height=120, font = ("Helvetica", 16), selectbackground="#807a71", selectforeground="white", undo = True)
   logtext.pack()

def Logs_win():
   new2= Toplevel(root, bg="#756754")
   new2.geometry("700x700")
   new2.title("Logs")
   #scrollbar
   text_scroll = Scrollbar(new2)
   text_scroll.pack(side=RIGHT, fill=Y)
   #frame
   logframe = Frame(new2)
   logframe.pack(pady=5)


   #text box
   logtext = Text(logframe, width=97, height=120, font = ("Helvetica", 16), selectbackground="#807a71", selectforeground="white", undo = True, yscrollcommand= text_scroll.set)
   logtext.pack()

   #
   text_scroll.config(command=logtext.yview)


   #Create a Label in New window
   
#Create a label
####TOOLBAR bottom####

button_frame = tk.Frame(root, bg="#4a4135")
button_frame.pack(fill=tk.X, side=tk.BOTTOM)

InventoryButton = ttk.Button(button_frame, text="Inventory",image = inventory_button_image1, width=85, command=inventory_win).pack(side=tkinter.LEFT)

LogsButton = ttk.Button(button_frame, text="Logs",image = Logs_button_image1, width=85, command=Logs_win).pack(side=tkinter.RIGHT)

#################################################

#draggable coursor
pointer = ImageTk.PhotoImage (file = "draggable.png")
pointerimge = table.create_image(300, 220, anchor=tk.NW, image=pointer)
def move(event):
    """Move the sprite image with a d w and s when click them"""
    if event.char == "a":
        table.move(pointerimge, -10, 0)
    elif event.char == "d":
        table.move(pointerimge, 10, 0)
    elif event.char == "w":
        table.move(pointerimge, 0, -10)
    elif event.char == "s":
        table.move(pointerimge, 0, 10)
 
# movement
root.bind("<Key>", move)

root.mainloop()
