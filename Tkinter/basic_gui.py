from tkinter import *
window=Tk()
window.title("I am learning python")
window.minsize(width=200,height=400)
window.maxsize(width=400,height=800)
l1=Label(window,text="employee name",fg="blue",bg="red")
l1.place(x=0,y=10)

v=StringVar()
def show():
    x=v.get()
    print(x)
    l2.config(text=x,bg="yellow",fg="black")
    

e1=Entry(window,font=("corbel",18),bd=5,textvariable=v)
e1.place(x=80,y=10)
b1=Button(window,text="Enter",fg="yellow",bg="green",command=show)
b1.place(x=120,y=60)
l2=Label(window,text="nothing",fg="black",bg="brown")
l2.place(x=120,y=100)
window.mainloop()

