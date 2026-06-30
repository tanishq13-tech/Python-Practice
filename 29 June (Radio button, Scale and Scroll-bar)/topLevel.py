from tkinter import *
root = Tk()
root.geometry("1000x1000")
root.title("Radio Button")

def open():
    top = Toplevel()
    top.geometry("500x500")
    top.title("New Window")
    l = Label(top, text="This is a new window").pack()

b = Button(root, text="Open New Window", command=open).pack()
root.mainloop()