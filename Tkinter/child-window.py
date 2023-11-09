from tkinter import *
m = Tk()
m.title("Main Window")
m.configure(bg="blue") # to change the background color of the window
m.geometry('500x200') #geometry function to make the size of the window

m1=Toplevel(m)
m1.title("Child Window")
#setting the window for 200 width and 150 height and  x-axis 1000 and y-axis as 150 this is generally used for positoning the window
m1.geometry('200x150+1000+150')

m.mainloop()