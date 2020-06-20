from tkinter import*
a=Tk()
a.title("this is what u r lonking for")
a.geometry('360x360')
def getval():
    with open("record.txt","a") as t:
        t.write(f"DETAILS\nname={l1.get()}\ngender={l2.get()}\ncourse={l3.get()}\ncollage={l4.get()}\n\n")
    Label(a, text="\nDETAILS").grid()
    Label(a,text=l1.get()).grid()
    Label(a,text=l2.get()).grid()
    Label(a,text=l2.get()).grid()
    Label(a,text=l2.get()).grid()


Label(a,text="Internship form",padx=80).grid(row=0,column=1)
Label(a,text="NAME").grid(row=1,column=0)
Label(a,text="GENDER").grid(row=2,column=0)
Label(a,text="COURSE").grid(row=3,column=0)
Label(a,text="COLLAGE").grid(row=4,column=0)
Checkbutton(a,text="confirms and submit").grid(column=1)

l1=StringVar()
l2=StringVar()
l3=StringVar()
l4=StringVar()

Entry(a,textvariable=l1).grid(row=1,column=1)
Entry(a,textvariable=l2).grid(row=2,column=1)
Entry(a,textvariable=l3).grid(row=3,column=1)
Entry(a,textvariable=l4).grid(row=4,column=1)

Button(text='submit',command=getval).grid(column=1)

a.mainloop()