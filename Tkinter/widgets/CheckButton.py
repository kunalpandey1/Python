from tkinter import *
window=Tk()
window.title("Hey I am learning Tkinter")
window.minsize(width=200,height=400)
window.maxsize(width=400,height=800)
cb=Checkbutton(window,text="Male")
cb.pack()
window.mainloop()