# adding widgets in tkinter window 

from tkinter import *
import pymysql
import tkinter.messagebox as msb

# connection function
def conn():
    return pymysql.connect(host="localhost",database="pydb2",user="root",password="",port=3306)

#insert function 
def InsertData():
    r = ern.get()
    f = efn.get()
    l = eln.get()
    e = eem.get()

    if(r=="" or f=="" or l=="" or e==""):
        msb.showinfo("Insert Status","pls fill all data")
    else:
        try:
            con = conn()
            cursor = con.cursor()
            args = (r,f,l,e)
            sql = "insert into stud (rollno,fname,lname,email) values(%s,%s,%s,%s)"
            cursor.execute(sql,args)
            con.commit()
            msb.showinfo("Insert Status","insert data successfully")
            con.close()
        except Exception as ex:
            print("insert not success ",ex)
            

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

b1 = Button(r,text="Insert",bg="yellow",command=InsertData)
b1.place(x=20,y=220)

mainloop()