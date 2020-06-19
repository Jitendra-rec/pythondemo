from tkinter import *
from PIL import ImageTk,Image
sc=Tk()
sc.geometry("360x360")
pic=PhotoImage(file="1.png")

sc=Label(image=pic)
sc.pack()
sc.mainloop()