from tkinter import *
tk = Tk()
tk.geometry("500x500")
tk.title("Canvas")

c = Canvas(tk, bg="lightYellow", height=400, width=400, bd=5, relief="groove")
c.create_arc((50, 100, 300, 300), start=0, extent=135, fill="Red", style="pieslice", width=2 )
c.create_arc((250, 300, 200, 200), start=50, extent=270, fill="blue", style="chord", width=2 )
c.create_arc((50, 50, 200, 200), start=0, extent=30, fill="green", style="arc", width=2 )
c.create_text(245, 180, text="Style: Pieslice")
c.pack()

tk.mainloop()