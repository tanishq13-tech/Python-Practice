from tkinter import *
root = Tk()
root.geometry("1000x1000")
root.title("Radio Button")

s = Spinbox(root, from_=0, to=25)
s.pack()
root.mainloop()