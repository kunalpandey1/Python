from tkinter import *
window=Tk()
window.title("Welcome")
window.minsize(width=200,height=400)
window.maxsize(width=400,height=800)
lb=Listbox(window,width=20)
lb.pack()
l1=["Tony","Edwin","Kirtika","eepsa"]
for i in l1:
    lb.insert(END,i)

def remove_from_list():
    lb.delete(ANCHOR)
    

b1=Button(window,text="Remove from the list",bg="red",command=remove_from_list)    
b1.pack()
window.mainloop()