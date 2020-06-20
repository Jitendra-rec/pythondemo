from tkinter import *
a=Tk()
n=0
def run():
    globals()['n']+=1
    n1=globals()['n']
    st="button"+str(n1)
    b3 = Button(a, fg='red', text=st, command=run)
    if n1<=13:
        b3.pack( ipadx=20, anchor="w")
    else :
        b3.pack(ipadx=20, anchor="w", side=RIGHT)

a.geometry("360x360")
f1=Frame(a,bg="blue",border=60,relief=SUNKEN)
f1.pack(anchor="w")

b1=Button(a,fg='red',text="print",command=run)
b1.pack(side=LEFT,ipadx=20,anchor="w")

a.mainloop()