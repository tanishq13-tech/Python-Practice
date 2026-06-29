from tkinter import *
from tkinter import PhotoImage
tk = Tk()
tk.geometry("600x600")
tk.title("Canvas")

c = Canvas(tk, bg="lightpink", height=500, width=450, bd=50, relief="groove")
#file2= PhotoImage(file="25 June (Python Canvas - Tkinter)\cute-happy-excited-cat-gx339xf5f5zewrju.gif") ## relative path
file2= PhotoImage(file="25 June (Python Canvas - Tkinter)\www_bing_com__images_search.png")
im = c.create_image(25,30, image=file2)
c.pack()
tk.mainloop()