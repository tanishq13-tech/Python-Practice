from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Label Frame")


def add():
    a = int(e1.get())
    b = int(e2.get())
    c = str(a+b)
    E1.insert(1,c)

w1 = PanedWindow(root)
w1.pack(fill=BOTH, expand=True)

E1 = Entry(w1, bd=5)
w1.add(E1)

w2 = PanedWindow(w1, orient=VERTICAL)
w1.add(w2)

e1 = Entry(w2)
e2 = Entry(w2)
b = Button(w2, text="Add", command=add)
w2.add(e1)
w2.add(e2)
w2.add(b)

root.mainloop()