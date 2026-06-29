from tkinter import *
tk = Tk()
tk.geometry("300x300")
tk.title("Check Button")

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()

l = Label(tk, text="Select option/s below is/are your favourite language/s:", fg="Red")
check1 = Checkbutton(tk, text="I like Java", variable=c1, onvalue=1, offvalue=0, height=3, width=30)
check2 = Checkbutton(tk, text="I like Python", variable=c2, onvalue=1, offvalue=0, height=3, width=30)
check3 = Checkbutton(tk, text="I like C++", variable=c3, onvalue=1, offvalue=0, height=3, width=30)
l.pack()
check1.pack()
check2.pack()
check3.pack()

tk.mainloop()