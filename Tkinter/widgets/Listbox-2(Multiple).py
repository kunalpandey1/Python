from tkinter import *
def add():
    res=inp.get()
    lb.insert(END,res)

def delitems():
    lb.delete(lb.curselection())

def upditems():
    selecteditem=lb.curselection()
    lb.delete(selecteditem)
    updtext=inp.get()
    lb.insert(selecteditem)

def display():
    selecteditem=lb.curselection()
    for i in selecteditem:
        print(lb.get(i))


win=Tk()
res=StringVar()
label=Label(win,text="Enter the item to add in the list")
inp = Entry(win,textvariable=res)
lb=Listbox(win,selectmode=MULTIPLE)

add=Button(win,text="Add",command=add)
delete=Button(win,text="Delete",command=delitems)
update=Button(win,text="Update",command=upditems)
disp=Button(win,text="Display",command=display)

label.pack()
inp.pack()
lb.pack()
add.pack()
delete.pack()
update.pack()
disp.pack()
win.mainloop()
