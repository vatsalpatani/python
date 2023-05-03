import pymysql

def conn():
    return pymysql.connect(host="localhost",database="pydb",user="root",password="",port=3306)

def showdata():
    con = conn()
    cursor = con.cursor()
    sql = "select * from stud"
    cursor.execute(sql)
    res = cursor.fetchall()
    for i in res:
        print(i)

def updatedata(name,email,city,id1):
    con = conn()
    cursor = con.cursor()
    args = (name,email,city,id1)
    sql = "update stud set name=%s , email=%s , city=%s where id=%s"
    cursor.execute(sql,args) 
    con.commit()
    print("data updated")
    con.close()

showdata()

id1 = int(input("enter id to update : "))
n = input("enter name : ")
e = input("enter email : ")
c = input("enter city : ")

updatedata(n,e,c,id1)

showdata()

# output  :
#     (1, 'vatsal', 'vatsal@mail.com', 'rajkot')
#     (2, 'vatsal', 'vatsalpatani@mail.com\t', 'rajkot')
#     enter id to update : 1
#     enter name : rajubhai
#     enter email : rajubhai@mail.com
#     enter city : surat
#     data updated
#     (1, 'rajubhai', 'rajubhai@mail.com', 'surat')
#     (2, 'vatsal', 'vatsalpatani@mail.com\t', 'rajkot')

# output  :
#     (1, 'vatsal', 'vatsal@mail.com', 'rajkot')
#     (2, 'vatsal', 'vatsalpatani@mail.com\t', 'rajkot')