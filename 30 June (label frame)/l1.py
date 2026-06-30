from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
root.title("Label Frame")

def confirm():
    response = messagebox.askquestion("Confirm", "Are you sure to submit?")
    if response == "yes":
        comfimation()
    else:
        pass
def comfimation():
    messagebox.showinfo("Confirmation", "Your details are submitted!!!")
f = LabelFrame(root, text="Main Settings", font=(1), bg="lightgreen")
f.pack(fill="both", expand="yes")

lb1 = LabelFrame(f, text="Personal Information", height= "10", width= "100", font=(1))
lb1.pack(padx=20,pady=20, fill="both", expand="yes")
l1 = Label(lb1, text="First name")
e1 = Entry(lb1, width=40, bg="white", relief="groove")
l2 = Label(lb1, text="Last name")
e2 = Entry(lb1, width=40, bg="white", relief="groove")
l1.place(x=20,y=20)
e1.place(x=90,y=20)
l2.place(x=20,y=50)
e2.place(x=90,y=50)

lb2 = LabelFrame(f, text="Address", height= "40", width= "100",  font=(1))
lb2.pack(padx=20,pady=20, fill="both", expand="yes")
l3 = Label(lb2, text="Street")
e3 = Entry(lb2, width=40, bg="white", relief="groove")
l4 = Label(lb2, text="City")
e4 = Entry(lb2, width=40, bg="white", relief="groove")
l5 = Label(lb2, text="Zip Code")
e5 = Entry(lb2, width=40, bg="white", relief="groove")
l3.place(x=30,y=20)
e3.place(x=90,y=20)
l4.place(x=35,y=50)
e4.place(x=90,y=50)
l5.place(x=20,y=80)
e5.place(x=90,y=80)

lb3 = LabelFrame(f, text="Preferences", height= "10", width= "100",  font=(1))
lb3.pack(padx=20,pady=20, fill="both", expand="yes")
c1 = Checkbutton(lb3,text="Enable Notifications" )
c2 = Checkbutton(lb3,text="Enable Dark Mode" )
c1.place(x=20,y=20)
c2.place(x=20,y=40)

b = Button(f, text="Submit", relief="groove", command=confirm).pack( anchor="se")

root.mainloop()
