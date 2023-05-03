import pymysql

def conn():
    return pymysql.connect(host="localhost",database="pydb",user="root",password="",port=3306)

def showdatabyid(id1):
    con = conn()
    cursor = con.cursor()
    args = (id1)
    sql = "select * from stud where id = %s"
    cursor.execute(sql,args)
    res = cursor.fetchall()
    for i in res:
        print(i)

i = int(input("enter id : "))
showdatabyid(i)

# output  :
#     enter id : 2
#     (2, 'vatsal', 'vatsalpatani@mail.com\t', 'rajkot')