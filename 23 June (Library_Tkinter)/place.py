from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("400x500")
top.title("My Form")

def function1():
    messagebox.showinfo("Info", "Submitted!!!")

l1 = Label(top, text="Username", fg="red").place(x=100, y=100)
e1 = Entry(top, bg="lightPink").place(x=200, y=100)
l2 = Label(top, text="Id", fg="red").place(x=100, y=150)
e2 = Entry(top, bg="lightPink").place(x=200, y=150)
l3 = Label(top, text="Department", fg="red").place(x=100, y=200)
e3 = Entry(top, bg="lightPink").place(x=200, y=200)
l4 = Label(top, text="Division", fg="red").place(x=100, y=250)
e4 = Entry(top, bg="lightPink").place(x=200, y=250)
b1 = Button(top, text="Sumbit", fg="red", bg="black", activebackground="blue", border=5, command= function1).place(x=150, y=350)

top.mainloop()