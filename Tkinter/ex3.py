# adding widgets in tkinter window 

from tkinter import *

r = Tk()

r.geometry("300x300")
r.title("My Title")
r.configure(bg="lightgreen")

# add label

rn = Label(r,text="roll number")
rn.place(x=20,y=20)

fn = Label(r,text="first name")
fn.place(x=20,y=70)

ln = Label(r,text="last name")
ln.place(x=20,y=120)

em = Label(r,text="email")
em.place(x=20,y=170)

# add entry box

ern = Entry()
ern.place(x=100,y=20)

efn = Entry()
efn.place(x=100,y=70)

eln = Entry()
eln.place(x=100,y=120)

eem = Entry()
eem.place(x=100,y=170)

# add buttons

b1 = Button(r,text="Button",bg="yellow")
b1.place(x=20,y=220)

mainloop()