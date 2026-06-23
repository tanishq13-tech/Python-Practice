from tkinter import *
top = Tk()
top.geometry("400x500")
top.title("My Form")

l1 = Label(top, text="Username", fg="red").grid(row=0, column=0)
e1 = Entry(top, bg="lightPink").grid(row=0, column=1)
l2 = Label(top, text="Id", fg="red").grid(row=1, column=0)
e2 = Entry(top, bg="lightPink").grid(row=1, column=1)
l3 = Label(top, text="Department", fg="red").grid(row=2, column=0)
e3 = Entry(top, bg="lightPink").grid(row=2, column=1)
l4 = Label(top, text="Division", fg="red").grid(row=3, column=0)
e4 = Entry(top, bg="lightPink").grid(row=3, column=1)

top.mainloop()