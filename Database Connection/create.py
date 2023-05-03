import pymysql

def conn():
    return pymysql.connect(host="localhost",database="pydb",user="root",password="",port=3306)

def createTb():
    con = conn()
    cursor = con.cursor()
    sql = "create table stud(id int primary key auto_increment , name varchar(50) , email varchar(50) , city varchar(50))"
    cursor.execute(sql)
    con.commit()
    print("table created")
    con.close() 

createTb()

# output  :   table created