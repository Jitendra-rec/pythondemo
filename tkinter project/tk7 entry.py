from tkinter import*
a=Tk()
a.title("this is what u r lonking for")
a.geometry('360x360')
def getval():
    print(f"user name is={uid.get()}and passward={psw.get()}")
    Label(text=f"user name={uid.get()}").grid()
    Label(text=f"passward={psw.get()}\n").grid()


Label(a,text="USERNAME").grid()
Label(a,text="PASSWORD").grid()
uid=StringVar()
psw=StringVar()

Entry(a,textvariable=uid).grid(row=0,column=1)
Entry(a,textvariable= psw).grid(row=1,column=1)
Button(text="summit",command=getval).grid()

a.mainloop()