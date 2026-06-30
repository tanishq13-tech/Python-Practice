from tkinter import *
root = Tk()
root.geometry("1000x1000")
root.title("Radio Button")
root.config(bg="grey")
def selection():
    sel = "You selected the option " + str(radio.get())
    l2.config(text=sel)
    
radio = IntVar()
l1 = Label(root, text="Favourite programing language:", bg="grey").pack()

r1 = Radiobutton(root, text="C", variable=radio, value=1, command=selection, bg="grey", activebackground="grey").pack()
r2 = Radiobutton(root, text="C++", variable=radio, value=2, command=selection, bg="grey", activebackground="grey").pack()
r3 = Radiobutton(root, text="Java", variable=radio, value=3, command=selection, bg="grey", activebackground="grey").pack()

l2 = Label(root, bg="grey")
l2.pack()
root.mainloop()