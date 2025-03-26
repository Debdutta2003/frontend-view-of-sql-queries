import oracledb
def select_operation(sql):
    conn=oracledb.connect(
        user="c##scott",
        password="tiger",
        dsn="localhost/XE")
    
    cursor=conn.cursor()
    d=cursor.execute(sql)
    Lst=list(d)
    print(Lst,type(Lst))
    return Lst 
