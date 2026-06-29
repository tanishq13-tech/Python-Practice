from tkinter import *
tk = Tk()
tk.geometry("800x800")
tk.title("Canvas")

c = Canvas(tk, bg="lightYellow", height=500, width=500, bd=5, relief="groove")
l = c.create_oval(10, 10, 400, 400, fill="green", width=5)
a = c.create_line(390, 10, 0, 400, fill="green", width=5)
b = c.create_line(390, 10, 0, 400, fill="green", width=5)
c.pack()
tk.mainloop()