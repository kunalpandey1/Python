from tkinter import *

def display():
    print(sp1.get())


def delete():
    sp2.delete(0,END)


def insertvalues():
    sp2.delete(0,END)
    sp2.insert(3,"Extra")

def display_selected():
    lb3.config(
        text=f'you selected {sp1.get()}',
        font=('Algerian',14),
        bg='#D97904'
    )


win=Tk()
win.geometry("500x300")
lb1=Label(win,text="Enter your roll number")
sp1=Spinbox(win,from_=1,to=30,increment=2,wrap=True,command=display_selected)

lb2=Label(win,text="Enter the size of the shirt")
sp2=Spinbox(win,values=('s','m','l','xl','xxl'))

lb1.pack()
sp1.pack()

lb2.pack()
sp2.pack()

b1=Button(win,text="Extract",command=display)
b1.pack()
b2=Button(win,text="Delete",command=delete)
b2.pack()
b3=Button(win,text="Insert",command=insertvalues)
b3.pack()


lb3=Label(win,text="Selected value is")
lb3.pack()
win.mainloop()
