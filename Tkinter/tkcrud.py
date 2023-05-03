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
            
# delete function
def deldata():
    id1 = ern.get()
    if(id1==""):
        msb.showinfo("Delete Status","pls enter roll number for delete")
    else:
        con = conn()
        cursor = con.cursor()
        args = (id1)
        sql = "delete from stud where rollno = %s"
        cursor.execute(sql,args)
        con.commit()
        msb.showinfo("Delete Status","delete data successfully")
        con.close()


# search function
def showdatabyid():
    id1 = ern.get()
    if(id1==""):
        msb.showinfo("earch Status","pls enter roll number for select")
    else:
        con = conn()
        cursor = con.cursor()
        args = (id1)
        sql = "select * from stud where rollno = %s"
        cursor.execute(sql,args)
        res = cursor.fetchall()
        msb.showinfo("Search Status",res)
        con.close()

# update function
def updatedata():
    r = ern.get()
    f = efn.get()
    l = eln.get()
    e = eem.get()

    if(r=="" or f=="" or l=="" or e==""):
        msb.showinfo("Update Status","pls fill all data")
    else:
        con = conn()
        cursor = con.cursor()
        args = (f,l,e,r)
        sql = "update stud set fname=%s , lname=%s , email=%s where rollno=%s"
        cursor.execute(sql,args) 
        con.commit()
        msb.showinfo("Update Status","data updated")
        con.close()


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

b2 = Button(r,text="Delete",bg="yellow",command=deldata)
b2.place(x=70,y=220)

b3 = Button(r,text="Update",bg="yellow",command=updatedata)
b3.place(x=120,y=220)

b4 = Button(r,text="Select",bg="yellow",command=showdatabyid)
b4.place(x=175,y=220)

mainloop()