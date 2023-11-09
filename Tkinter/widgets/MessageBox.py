from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Welcome")
window.minsize(width=200,height=400)
window.maxsize(width=400,height=800)
v=StringVar()
def message():
    if v.get()=="":
        messagebox.showwarning("caution","It's Empty please fill it")
     
    else:
        messagebox.showinfo("successfull",v.get())

e1=Entry(window,font=("Algerian",20),width=20,textvariable=v)
e1.pack()
b1=Button(window,text="Enter",command=message)
b1.pack()
window.mainloop()        