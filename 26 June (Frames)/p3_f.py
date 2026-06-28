from tkinter import *
tk = Tk()
tk.geometry("600x1000")
tk.title("Frames")

f1 = Frame(tk, height=1000, width=600, bg="lightgreen").place(x=0,y=0)
l1 = Label(f1, text="Enter Your Task", font="TimesNewRoman", bg="lightgreen").place(x=230,y=5)
e1 = Entry(f1, width=96).place(x=10,y=40)
b1 = Button(f1, text="Submit", bg="red", font="TimesNewRoman").place(x=270,y=65)
l2 = Label(f1, bg="white", height=20, width=82).place(x=10,y=110)
l3 = Label(f1, text="Delete Task Numbers", bg="blue", font="TimesNewRoman").place(x=210,y=430)
e2 = Entry(f1, width=10).place(x=280,y=470)
b1 = Button(f1, text="Delete", bg="red", font="TimesNewRoman").place(x=270,y=500)
b1 = Button(f1, text="Exit", bg="red", font="TimesNewRoman").place(x=280,y=550)

tk.mainloop()