import sqlite3 as sql
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
global panel
def image():
 conn=sql.connect('ATMdata.db')
 cursor=conn.execute("SELECT IMAGE FROM IMAGES WHERE ID="+str(e1.get()))
 img_data=cursor.fetchone()[0]
 with open('sathish1.png','wb') as file:
     file.write(img_data)
     conn.close()
     path="sathish1.png"
 img=ImageTk.PhotoImage(Image.open(path))
 panel.configure(image=img)
 panel.image=img
win = Tk()
win.geometry("700x500")
l3=Label(win,text='ID',font=("ArialGreek 15"),bg='#8DFC04')
l3.pack()
e1=tk.Entry(win,show=None,font=('Arial',15),bg='#8DFC04')
e1.pack()
img = ImageTk.PhotoImage(Image.open("White_full.jpg"))
panel=tk.Label(win,image=img)
panel.image=img
panel.pack()
subtn=Button(win,text="SUBMIT",width=20,height=0,command=image).pack()
win.mainloop()

