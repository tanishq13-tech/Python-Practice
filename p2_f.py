from tkinter import *
tk = Tk()
tk.geometry("1000x1000")
tk.title("Frames")

f1 = Frame(tk, height=500, width=120, bg="lightGreen").place(x=0,y=0)
f2 = Frame(f1, height=500, width=120, bg="skyblue").place(x=880,y=0)
f3 = Frame(f1, height=100, width=760, bg="red").place(x=120,y=0)
f4 = Frame(f1, height=400, width=760, bg="yellow").place(x=120,y=100)
f5 = Frame(f1, height=50, width=760, bg="blue").place(x=120,y=450)
l1 = Label(f3, text="Left", fg="black", bg="grey", font="TimesNewRoman").place(x=150, y=10)
l2 = Label(f3, text="Center", fg="black", bg="grey", font="TimesNewRoman").place(x=470, y=10)
l3 = Label(f3, text="Right", fg="black", bg="grey", font="TimesNewRoman").place(x=800, y=10)

tk.mainloop()
