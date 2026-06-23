from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("400x500")
top.title("My Form")

def function1():
    messagebox.showinfo("Info", "Red is clicked!!!")
def function2():
    messagebox.showinfo("Info", "Blue is clicked!!!")
def function3():
    messagebox.showinfo("Info", "Green is clicked!!!")
def function4():
    messagebox.showinfo("Info", "Black is clicked!!!")

b1 = Button(top, text= "Red", fg="Red", bg="Black", command= function1)
b1.pack(side= LEFT)
b2 = Button(top, text= "Blue", fg="Blue", bg="Pink", command= function2)
b2.pack(side= RIGHT)
b3 = Button(top, text= "Green", fg="Green", bg="Yellow", command= function3)
b3.pack(side= TOP)
b4 = Button(top, text= "Black", fg="Black", bg="White", command= function4)
b4.pack(side= BOTTOM)
top.mainloop()