# In Tkinter, an Entry is a widget used to display a single-line text field that allows the user to input text or data. It provides a simple way to accept textual input from the user in a GUI application. An Entry widget typically appears as a rectangular box where the user can type or edit text.

from tkinter import *
window=Tk()
e1=Entry(window,width=20,bd=5,font=("Algerian",20))
e1.pack()
window.mainloop()
