from tkinter import *
root=Tk()
root.geometry('360x360')

def size():
    root.geometry(f"{l1.get()}x{l2.get()}")


l1=StringVar()
l2=StringVar()
Label(text='SIZE CHANGE').grid(row=0,column=0)
Label(text='LENGTH').grid(row=1,column=0)
Label(text='BREATH').grid(row=2,column=0)
Entry(root,textvariable=l2).grid(row=1,column=1)
Entry(root,textvariable=l1).grid(row=2,column=1)
b=Button(text="change",command=size).place(x=90,y=75)
root.mainloop()