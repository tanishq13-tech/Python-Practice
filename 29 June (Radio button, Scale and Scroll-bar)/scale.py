from tkinter import *
root = Tk()
root.geometry("1000x1000")
root.title("Scale")
root.config(bg="grey")

def selection():
    sel = "You selected the option " + str(v.get())
    l.config(text=sel)

v = IntVar()
s = Scale(root, variable=v, from_=1, to=50, orient=HORIZONTAL, bg="grey").pack()
b = Button(root, text="Value", command=selection, bg="grey")
b.pack(anchor=CENTER)
l = Label(root, bg="grey")
l.pack()
root.mainloop()