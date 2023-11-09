from tkinter import *
window=Tk()
window.title("welcome")
window.minsize(width=200,height=400)
window.maxsize(width=400,height=800)
v=IntVar()
def value():
    print(v.get())

rb1=Radiobutton(window,text="yes",value=1,variable=v)
rb2=Radiobutton(window,text="No",value=0,variable=v)
rb1.pack()
rb2.pack()

b1=Button(window,text="Enter",command=value)
b1.pack()
window.mainloop()