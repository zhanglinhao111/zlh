import pymysql
host = "localhost"
database = "bk"
user = "root"
password = "root"
def update(sql, param):
    con = pymysql.connect(host=host, database=database,user=user,password=password)
    cursor =con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def select (sql, param, mode="many", size=0):
    con = pymysql.connect (host=host,database=database,user=user,password=password)
    cursor =con.cursor ()
    cursor.execute(sql, param)
    con. commit()
    if mode == "all":
        return cursor.fetchall ()
    elif mode == "one":
        return cursor.fetchone ()
    elif mode == "many" :
        return cursor.fetchmany (size)
    cursor.close ()
    con.close()