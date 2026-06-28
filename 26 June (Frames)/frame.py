from tkinter import *
tk = Tk()
tk.geometry("10000x1000")
tk.title("Frames")

def login():
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

f1 = Frame(tk, height=50, width=1000, bg="black").place(x=0,y=0)
t1 = Label(f1, text="Hello Tanishq", fg="white", bg="black", font="TimesRoman").place(x=5,y=7)
b1 = Button(f1, text="Login", fg="white", bg="red", font="TimesNewRoman", command=login).place(x=925,y=6)

f2 = Frame(tk, height=500, width=1000, bg="blue").place(x=0,y=100)
e1 = Entry(f2, bg="white", width= 100).place(x=5, y=110)
b2 = Button(f2, text="Add Task", fg="white", bg="Green", font="TimesNewRoman", command=login).place(x=875,y=108)
l2 = Label(f2, text="Division", fg="white", height=20, width=130).place(x=40, y=180)
b3 = Button(f2, text="Remone Task", fg="white", bg="red", font="TimesNewRoman", width=50, command=login).place(x=5,y=515)
b4 = Button(f2, text="Complete Task", fg="white", bg="Yellow", font="TimesNewRoman", width=25, command=login).place(x=675,y=515)

tk.mainloop()
