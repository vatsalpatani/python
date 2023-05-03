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

def deldata(id1):
    con = conn()
    cursor = con.cursor()
    args = (id1)
    sql = "delete from stud where id = %s"
    cursor.execute(sql,args)
    con.commit()
    con.close()

showdata()
id1 = int(input("enter id for delete data : "))
deldata(id1)
showdata()

# output  :
#     (1, 'rajubhai', 'rajubhai@mail.com', 'surat')
#     (2, 'vatsal', 'vatsalpatani@mail.com\t', 'rajkot')
#     enter id for delete data : 1
#     (2, 'vatsal', 'vatsalpatani@mail.com\t', 'rajkot')