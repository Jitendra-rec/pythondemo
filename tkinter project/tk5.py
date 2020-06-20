from tkinter import*
a=Tk()
a.title("this is what u r lonking for")
a.geometry('360x360')

f1=Frame(a,bg="red",border=10)
f1.pack(fill='x')
f2=Frame(a,bg="blue",border=10)
f2.pack(fill='x')
l1=Label(f1,text="project  tkinter-Pycharm",bg='black',fg='white')
l1.pack()
l1=Label(f2,text="project  tkinter-Pycharm",bg="yellow")
l1.pack()
a.mainloop()