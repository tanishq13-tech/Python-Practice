from tkinter import *
root = Tk()
root.geometry("1000x1000")
root.title("Radio Button")

lb1 = LabelFrame(root, text="Positive Comments", labelanchor="se")
lb1.pack(fill="both", expand="yes")
l = Label(lb1, text="Hello")
l.pack()
root.mainloop()

# abelanchor options:

   # "n" - Center top (what we just set)
    #"nw" - Top-left (default)
    #"ne" - Top-right
    #"s" - Center bottom
    #"sw" - Bottom-left
    #"se" - Bottom-right