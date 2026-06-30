from tkinter import *
tk = Tk()
tk.geometry("300x300")
tk.title("Check Button")

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()

l = Label(tk, text="Select option/s below is/are your favourite language/s:", fg="Red")
check1 = Radiobutton(tk, text="I like Java", variable=c1,  height=30,  width=30, relief="groove")
check2 = Radiobutton(tk, text="I like Python", variable=c2,  height=3, width=30)
check3 = Radiobutton(tk, text="I like C++", variable=c3, height=3, width=30)
l.pack()
check1.pack()
check2.pack()
check3.pack()

tk.mainloop()