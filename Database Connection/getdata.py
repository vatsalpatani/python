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

showdata()

# output  :
#     (1, 'vatsal', 'vatsal@mail.com', 'rajkot')
#     (2, 'vatsal', 'vatsalpatani@mail.com\t', 'rajkot')