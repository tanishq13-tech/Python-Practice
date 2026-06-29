from tkinter import *
tk = Tk()
tk.geometry("800x800")
tk.title("Canvas")

c = Canvas(tk, bg="lightYellow", height=500, width=500, bd=500)
c.pack()
tk.mainloop()