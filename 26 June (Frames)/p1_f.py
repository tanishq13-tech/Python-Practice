from tkinter import *
tk = Tk()
tk.geometry("1000x1000")
tk.title("Frames")

f1 = Frame(tk, height=500, width=1000, bg="blue").place(x=0,y=0)
f2 = Frame(f1, height=233, width=980, bg="green").place(x=10,y=10)
f3 = Frame(f1, height=233, width=980, bg="red").place(x=10,y=255)
l3 = Label(f2, text="A Label in a top frame", fg="black", bg="green").place(x=20, y=20)
l4 = Label(f3, text="A Label in a bottom frame", fg="black", bg="red").place(x=830, y=450)

tk.mainloop()
