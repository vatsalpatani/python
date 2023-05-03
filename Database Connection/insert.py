import pymysql

def conn():
    return pymysql.connect(host="localhost",database="pydb",user="root",password="",port=3306)

def InsertData(name,email,city):
    con = conn()
    cursor = con.cursor()
    args = (name,email,city)
    sql = "insert into stud (name,email,city) values(%s,%s,%s)"
    cursor.execute(sql,args)
    con.commit()
    print("data inserted")
    con.close()

n = input("enter your name : ")
e = input("enter your email : ")
c = input("enter your city : ")

InsertData(n,e,c)

# output  :   
#     enter your name : vatsal
#     enter your email : vatsalpatani@mail.com
#     enter your city : rajkot
#     data inserted