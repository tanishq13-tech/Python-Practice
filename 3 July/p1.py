from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import pyttsx3

root = Tk()
root.geometry("1000x1000")
root.title("Python Guides")


def function1():
        messagebox.showinfo("Info", "Submitted!!!")
        if __name__ == '__main__':
            engine = pyttsx3.init()
            engine.say("You are registerted. Now you can start your work. All the best.")
            engine.runAndWait()


countries = [
   "Afghanistan",
   "Albania",
   "Algeria",
   "Andorra",
   "Angola",
   "Argentina",
   "Australia",
   "Austria",
   "Bangladesh",
   "Belgium",
   "Brazil",
   "Canada",
   "China",
   "Denmark",
   "Egypt",
   "France",
   "Germany",
   "India",
   "Italy",
   "Japan",
   "Mexico",
   "Netherlands",
   "Nigeria",
   "Norway",
   "Pakistan",
   "Russia",
   "South Africa",
   "Spain",
   "Sweden",
   "United Kingdom",
   "United States"
]

f1 = Frame(root, height=780, width=1000, bg="DeepSkyBlue4")
f1.pack()
f2 = Frame(f1, height=740, width=960, bg="grey55")
f2.place(x=20,y=20)

l1 = Label(f2, text="Enter Name", bg="grey55", font=("TimesNewRoman", 15)).place(x=30,y=20)
e1 = Entry(f2, bg="white", width=45, font=("TimesNewRoman", 15)).place(x=250,y=20)

l1 = Label(f2, text="Enter Email", bg="grey55", font=("TimesNewRoman", 15)).place(x=30,y=70)
e1 = Entry(f2, bg="white", width=45, font=("TimesNewRoman", 15)).place(x=250,y=70)

l1 = Label(f2, text="Contact Number", bg="grey55", font=("TimesNewRoman", 15)).place(x=30,y=120)
e1 = Entry(f2, bg="white", width=45, font=("TimesNewRoman", 15)).place(x=250,y=120)

l1 = Label(f2, text="Select Gender", bg="grey55", font=("TimesNewRoman", 15)).place(x=30,y=170)
f3 = Frame(f1, height=10, width=45, bg="grey55")
f3.place(x=270,y=190)
r = IntVar()
radio1 = Radiobutton(f3, text="Male                        ", variable=r, value=1, font=("TimesNewRoman", 13), bg="white").pack(side=LEFT)
radio2 = Radiobutton(f3, text="Female                         ", variable=r, value=2, font=("TimesNewRoman", 13), bg="white").pack(side=LEFT)
radio3 = Radiobutton(f3, text="Other       ", variable=r, value=3, font=("TimesNewRoman", 13), bg="white").pack(side=LEFT)

l1 = Label(f2, text="Select Country", bg="grey55", font=("TimesNewRoman", 15)).place(x=30,y=230)
country_var = StringVar()
b1 = Combobox(f2, textvariable=country_var, values=countries, font=("TimesNewRoman", 15), width=42, state="readonly")
b1.set("Select")
b1.place(x=250, y=220)

l1 = Label(f2, text="Enter Password", bg="grey55", font=("TimesNewRoman", 15)).place(x=30,y=270)
e1 = Entry(f2, bg="white", width=45, font=("TimesNewRoman", 15)).place(x=250,y=270)

l1 = Label(f2, text="Re-Enter Password", bg="grey55", font=("TimesNewRoman", 15)).place(x=30,y=320)
e1 = Entry(f2, bg="white", width=45, font=("TimesNewRoman", 15)).place(x=250,y=320)

b2 = Button(f2, text="Register", bd=2, relief="solid", font=("TimesNewRoman", 15), width=45, command=function1).place(x=250, y=370)
root.mainloop()