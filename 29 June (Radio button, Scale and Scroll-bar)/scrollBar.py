from tkinter import *
root = Tk()
root.geometry("300x300")
root.title("Scroll Bar")
root.config(bg="lightgrey")

sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

list = Listbox(root, yscrollcommand= sb.set, height=100, width=10)

for i in range(50):
    list.insert(END, "Number" + str(i))

list.pack(side=LEFT)
sb.config(command=list.yview)
root.mainloop()