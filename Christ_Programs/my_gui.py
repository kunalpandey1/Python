# from tkinter import *

# top = Tk()
# c = Canvas(top, bg="orange", height=300, width=100)
# c.pack()
# top.mainloop()



# import tkinter as tk
# root =tk.Tk()
# label = tk.Label(root,text="Hello Python")
# label.pack()
# root.mainloop()


# import tkinter as tk
# top = tk.Tk()
# label1 = tk.Label(top,text="Name").grid(row=0)
# label2 = tk.Label(top,text="RegNum").grid(row=1)
# label3 = tk.Label(top,text="RefBook").grid(row=2)

# e1 = tk.Entry(top)
# e2 = tk.Entry(top)
# e3 = tk.Entry(top)

# e1.grid(row=0,column=10)
# e2.grid(row=1,column=10)
# e3.grid(row=2,column=10)
# top.mainloop()



# # How to enter the multi line text in the textbox

# import tkinter as tk
# top = tk.Tk()
# T =tk.Text(top,height=2,width=30)
# T.pack()
# T.insert(tk.END,"more information on GUI can be referred at realPython website")
# top.mainloop()


# from tkinter import *

# Top = Tk()
# Top.geometry("200x100")

# # Corrected color value in "#RRGGBB" format
# b = Button(Top, text="Simple", fg="#445b59", height=2, width=15, bd=10)
# b.pack()

# Top.mainloop()  






from tkinter import *
import tkinter as tk
top= tk.Tk()
top.title("Sample GUI")
def letStart():
    print("get set go")
def letPause():
    print("Wait!!")
def letStop():
    print("Bye")
B1= tk.Button(top,text="Start", command=letStart, width=30, height=5)
B1.pack()
B2= tk.Button(top, text="Pause", command=letPause, width=30, height=5)
B2.pack()
B3= tk.Button(top, text="Stop", command=letStop, width=30, height=5)
B3.pack()
top.mainloop()




from tkinter import *
from tkinter import messagebox as MB
import tkinter
top=tkinter.Tk()
def helloCallBack():
    MB.showinfo("Heloo Python", "Heloo World")
B=tkinter.Button(top, text="Heloo", command= helloCallBack)
B.pack()
B.place(bordermode= OUTSIDE, height=100, width=100)
top.mainloop()




from tkinter import *
import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
name_var=tk.StringVar()
passw_var=tk.StringVar()
def submit():
    name=name_var.get()
    password=passw_var.get()
    print("The name is:"+name)
    print("The password is "+password)
    name_var.set("")
    passw_var.set("")
name_label=tk.Label(root, text='Username', font=('calibre',10,'bold'))
name_entry=tk.Entry(root, textvariable= name_var,font=('calibre',10,'normal'))
passw_label= tk.Label(root,text = 'Password', font=('calibre', 10, 'bold'))
passw_entry=tk.Entry(root, textvariable= passw_var, show='*', font=('calibre', 10, 'normal'))
sub_btn=tk.Button(root, text='Submit', command=submit)
name_label.grid(row=0,column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)
root.mainloop()
